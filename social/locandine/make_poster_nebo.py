from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageChops
import numpy as np
R='/home/user/Noble-Sin/'; W,H=2480,3508
ref=np.asarray(Image.open(R+'releases/nebo/artwork/NEBO_cover_DISTROKID_3000.jpg').convert('RGB').resize((600,600))).astype(float)/255
rm,rs=ref.reshape(-1,3).mean(0),ref.reshape(-1,3).std(0)
im=ImageOps.fit(Image.open(R+'press/noblesin_nebo_press_vertical.jpg').convert('RGB'),(W,H),Image.LANCZOS,centering=(0.5,0.12))
a=np.asarray(im).astype(float)/255; m,s=a.reshape(-1,3).mean(0),a.reshape(-1,3).std(0)
a=a*0.7+((a-m)/s*rs+rm)*0.3; lum=(a*[0.299,0.587,0.114]).sum(2,keepdims=True); a=lum+(a-lum)*0.82
a=np.clip((a-0.5)*1.1+0.5,0,1); a+=(1-lum)**2*np.array([-0.01,0,0.02])+lum**2*np.array([0.02,0.008,-0.012])
yy,xx=np.mgrid[0:H,0:W]; r=np.sqrt(((xx-W/2)/(W/2))**2+((yy-H/2)/(H/2))**2); a*=(1-0.25*np.clip(r-0.6,0,1))[...,None]
a+=np.random.default_rng(7).normal(0,0.012,(H,W,1))
im=Image.fromarray((np.clip(a,0,1)*255).astype('uint8'))
# top + bottom dark gradients (Nebo reel-cover style)
ov=Image.new('L',(W,H),0); d=ImageDraw.Draw(ov)
for y in range(H):
    t=max(0,(1150-y)/600) if y<1150 else max(0,(y-2250)/600)
    d.line([(0,y),(W,y)],fill=int(235*min(1,t)))
im.paste((8,10,16),(0,0),ov)
# logo (white on black) screen-blended
lg=Image.open(R+'brand/logo_wordmark_white_on_black.jpg').convert('RGB'); lw=1900; lg=lg.resize((lw,int(lg.height*lw/lg.width)),Image.LANCZOS)
x0,y0=(W-lw)//2,60; box=(x0,y0,x0+lw,y0+lg.height)
im.paste(ImageChops.screen(im.crop(box),lg),box)
C=(240,236,228); dt=ImageDraw.Draw(im)
def line(t,size,y,track,fill=C):
    f=ImageFont.truetype(R+'social/assets/nebo/fonts/CG.ttf',size)
    ws=[dt.textbbox((0,0),c,font=f) for c in t]; wid=[b[2]-b[0] if c!=' ' else size*0.28 for c,b in zip(t,ws)]
    x=(W-(sum(wid)+track*(len(t)-1)))/2
    for c,b,w in zip(t,ws,wid):
        if c!=' ': dt.text((x-b[0],y),c,font=f,fill=fill)
        x+=w+track
line('LIVE',64,890,48)
line('PIGNOLA (PZ)',230,2780,24)
line('SABATO 12 GIUGNO 2027  ·  ORE 21:00',92,3080,14)
line('@NOBLESIN_OFFICIAL',46,3300,14,(170,168,162))
im.save(R+'social/locandine/locandina_pignola_2027-06-12.png')
p=im.copy(); p.thumbnail((620,877)); p.save('/tmp/claude-0/-home-user-Noble-Sin/424a8918-5573-5479-82c8-6fc887e2d8a1/scratchpad/prev.png')
