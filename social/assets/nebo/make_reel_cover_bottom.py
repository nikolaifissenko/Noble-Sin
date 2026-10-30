import sys
from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageFilter
import numpy as np
src,out,cx,lines=sys.argv[1],sys.argv[2],float(sys.argv[3]),sys.argv[4:]
ref=np.asarray(Image.open('/home/user/Noble-Sin/releases/nebo/artwork/NEBO_cover_DISTROKID_3000.jpg').convert('RGB').resize((600,600))).astype(float)/255
rm,rs=ref.reshape(-1,3).mean(0),ref.reshape(-1,3).std(0)
im=ImageOps.fit(Image.open(src).convert('RGB'),(1080,1920),Image.LANCZOS,centering=(cx,0.5))
a=np.asarray(im).astype(float)/255; m,s=a.reshape(-1,3).mean(0),a.reshape(-1,3).std(0)
a=a*0.7+((a-m)/s*rs+rm)*0.3; lum=(a*[0.299,0.587,0.114]).sum(2,keepdims=True); a=lum+(a-lum)*0.82
a=np.clip((a-0.5)*1.1+0.5,0,1); a+=(1-lum)**2*np.array([-0.01,0,0.02])+lum**2*np.array([0.02,0.008,-0.012])
h,w=a.shape[:2]; yy,xx=np.mgrid[0:h,0:w]; r=np.sqrt(((xx-w/2)/(w/2))**2+((yy-h/2)/(h/2))**2); a*=(1-0.25*np.clip(r-0.6,0,1))[...,None]
a+=np.random.default_rng(7).normal(0,0.012,(h,w,1))
im=Image.fromarray((np.clip(a,0,1)*255).astype('uint8'))
ov=Image.new('L',(1080,1920),0); d=ImageDraw.Draw(ov)
for y in range(1180,1920): d.line([(0,y),(1080,y)],fill=int(190*min(1,(y-1180)/420)))
im.paste((8,10,16),(0,0),ov)
txt=Image.new('L',(1080,1920),0); dt=ImageDraw.Draw(txt)
for spec in lines:
    t,size,y,font,track=spec.split('|'); size,y,track=int(size),int(y),int(track)
    f=ImageFont.truetype(f'fonts/{font}.ttf',size,layout_engine=ImageFont.Layout.RAQM)
    ws=[dt.textbbox((0,0),c,font=f) for c in t]; wid=[b[2]-b[0] if c!=' ' else size*0.28 for c,b in zip(t,ws)]
    x=540-(sum(wid)+track*(len(t)-1))/2
    for c,b,wd in zip(t,ws,wid):
        if c!=' ': dt.text((x-b[0],y),c,font=f,fill=255)
        x+=wd+track
im.paste((0,0,0),(0,0),txt.filter(ImageFilter.GaussianBlur(6)).point(lambda v:int(v*0.8)))
im.paste((240,236,228),(0,0),txt)
im.save(out,quality=94)
