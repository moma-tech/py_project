import datetime

from PIL import Image, ImageDraw, ImageFont

# importing the image
img = Image.open("gfg.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("LXGWWenKaiScreen.ttf", 50)
left = 100
with open("text.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        draw.text((70, left), line, (255, 255, 255), font=font)
        left = left + 70
draw.text((700, 888), "@何地似彼方", (255, 255, 255), font=font)
today = datetime.date.today()
formatted_time = today.strftime('%y%m%d')
# saving the image
img.save(formatted_time+'.jpg')