#!/bin/bash
# usage: grab.sh url...  -> prints emails + first headings per url
for u in "$@"; do
  h=$(curl -sL --max-time 20 -A "Mozilla/5.0" "$u" 2>/dev/null)
  em=$(echo "$h" | grep -oiE '[a-z0-9._%+-]+(@|&#64;|\[at\]| at )[a-z0-9.-]+\.[a-z]{2,}' | sed 's/&#64;/@/;s/\[at\]/@/;s/ at /@/' | grep -viE 'png|jpg|sentry|example|wixpress|domain\.' | sort -u | head -5 | tr '\n' ' ')
  hd=$(echo "$h" | grep -oiE '<(h1|h2|h3)[^>]*>[^<]{8,140}' | sed 's/<[^>]*>//' | head -6 | tr '\n' '|')
  dt=$(echo "$h" | grep -oE '\b(1[0-9]|2[0-9]|0?[1-9])[./ -](11|nov[a-z]*)[./ -]?(2026)?' -i | head -3 | tr '\n' ' ')
  echo "== $u | EMAIL: $em | DATES: $dt | H: ${hd:0:500}"
done
