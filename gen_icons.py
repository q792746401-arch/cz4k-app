# -*- coding: utf-8 -*-
"""生成 PWA 图标：icon-512 / icon-192 / apple-touch-icon(180)"""
from PIL import Image, ImageDraw, ImageFont

S = 512
img = Image.new('RGBA', (S, S), (0, 0, 0, 0))
px = img.load()
# 对角渐变：左上 #161d26 -> 右下 #0a0e14
top = (22, 29, 38)
bot = (10, 14, 20)
for y in range(S):
    t = y / (S - 1)
    r = int(top[0] + (bot[0] - top[0]) * t)
    g = int(top[1] + (bot[1] - top[1]) * t)
    b = int(top[2] + (bot[2] - top[2]) * t)
    for x in range(S):
        px[x, y] = (r, g, b, 255)

d = ImageDraw.Draw(img)

# 金色播放三角（居中偏上，整体落在 maskable 安全区内）
cx, cy = S / 2, S / 2 - 30
tri = [(cx - 48, cy - 58), (cx - 48, cy + 58), (cx + 80, cy)]
d.polygon(tri, fill=(240, 180, 41, 255))
# 三角细高光
d.line([(cx - 46, cy - 54), (cx - 46, cy + 54)], fill=(255, 210, 90, 255), width=3)

def load_font(size):
    for p in [r"C:\Windows\Fonts\msyhbd.ttc",
              r"C:\Windows\Fonts\msyh.ttc",
              r"C:\Windows\Fonts\simhei.ttf"]:
        try:
            return ImageFont.truetype(p, size, index=0)
        except Exception:
            continue
    return ImageFont.load_default()

# "长资源" 白色文字，位于三角下方
font = load_font(92)
text = "长资源"
bbox = d.textbbox((0, 0), text, font=font)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
tx = (S - tw) / 2 - bbox[0]
ty = cy + 82
d.text((tx, ty), text, font=font, fill=(242, 245, 248, 255))

img.save(r"C:\Users\Administrator\Doubao\chats\2026-10-12\new-chat-2\cz4k-app\icon-512.png")
img.resize((192, 192), Image.LANCZOS).save(r"C:\Users\Administrator\Doubao\chats\2026-10-12\new-chat-2\cz4k-app\icon-192.png")
img.resize((180, 180), Image.LANCZOS).save(r"C:\Users\Administrator\Doubao\chats\2026-10-12\new-chat-2\cz4k-app\apple-touch-icon.png")
print("icons done")
