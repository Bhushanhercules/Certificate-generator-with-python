
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
data = pd.read_excel(r'C:\******\******\*******\Book1.xlsx')#Enter your own path 

name_list = data["Name"].tolist()

for i in name_list:
    im = Image.open(r'C:\****\*****\*****\images.jpeg')
    d = ImageDraw.Draw(im)
    location = (198, 183)
    text_color = (0, 137, 209)
    font = ImageFont.truetype("ds_digital", 120)
    d.text(location,i,fill=text_color,font=font)
    im.save("certificate_" + i + ".pdf")
