from PIL import Image, ImageFont, ImageDraw
import datetime


# fonts and image Variables
img = Image.open('assets/Certuary.png')
fnt_company = ImageFont.truetype(r'fonts/general.ttf', 14)
fnt_description = ImageFont.truetype(r'fonts/general.ttf', 14)
fnt_name = ImageFont.truetype(r'fonts/name.ttf', 45)
fnt_date = ImageFont.truetype(r'fonts/name.ttf', 30)
fnt_sign = ImageFont.truetype(r'fonts/sign.ttf', 45)

#Current date
date = datetime.datetime.now()
current_date = date.strftime("%d") + " " + date.strftime("%B") + " , " + date.strftime("%Y")


#Input Variable
name = input("Enter Name: ")
sign = input("Enter Signature: ")
description = input("Enter Description: ")
company = input("Enter Company Name: ")
role = input("Enter Role: ") # 1433, 1135



#main function
def createCertificate(name, sign, description, company, ):
    draw = ImageDraw.Draw(img)
    #Date
    draw.text((440, 1143), current_date, font=fnt_date, fill=(0, 0, 0))
    #Name
    if len(name) >= 14:
        draw.text((753, 682), name, font=fnt_name, fill=(0, 0, 0))
    else:
        draw.text((753, 682), name, font=fnt_name, fill=(0, 0, 0))

    #Signature
    if len(sign) >= 14:
        draw.text((1353, 1060), sign, font=fnt_sign, fill=(0, 0, 0))
    else:
        draw.text((1405, 1060), sign, font=fnt_sign, fill=(0, 0, 0))

    #

    #Description
    if
    draw.text((1353, 1060), description, font=fnt_description, fill=(0, 0, 0))
    return img.show('minted-certificate.jpg')




createCertificate(name, sign, description)