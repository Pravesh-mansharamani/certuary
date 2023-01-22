from PIL import Image, ImageFont, ImageDraw
import datetime
import textwrap



qr_img = Image.open('assets/sampleqrcode.png')
# 996, 1166 pixel

# fonts and image Variables
img = Image.open('assets/Certificate.png')

fnt_company = ImageFont.truetype(r'fonts/name.ttf', 45)
fnt_description = ImageFont.truetype(r'fonts/general.ttf', 30)
fnt_name = ImageFont.truetype(r'fonts/name.ttf', 45)
fnt_date = ImageFont.truetype(r'fonts/name.ttf', 35)
fnt_sign = ImageFont.truetype(r'fonts/sign.ttf', 45)
fnt_role = ImageFont.truetype(r'fonts/name.ttf', 30)

#Current date
d = datetime.datetime.now()
current_date = d.strftime("%d") + " " + d.strftime("%B") + ", " + d.strftime("%Y")


#Input Variable
name = input("Enter Name: ")
sign = input("Enter Signature: ")
desc = input("Enter Description: ")
company = input("Enter Company Name: ")
role = input("Enter Role: ")

# Wrap text at a maximum line width of 80 characters
formatted_description = textwrap.fill(desc, width=80)


# main function
def createCertificate(name, sign, description, company, role ):
    draw = ImageDraw.Draw(img)

    # Date
    draw.text((377, 1143), current_date, font=fnt_date, fill=(0, 0, 0))

    # Role
    draw.text((1433, 1135), role, font=fnt_role, fill=(0, 0, 0))

    # Company
    if len(company) > 5:
        draw.text((896, 977), company, font=fnt_company, fill=(0, 0, 0))
    else:
        draw.text((946, 977), company, font=fnt_company, fill=(0, 0, 0))

    # Description
    draw.text((422, 770), description, font=fnt_description, fill=(0, 0, 0))

    # Name
    if len(name) > 16:
        draw.text((753, 682), name, font=fnt_name, fill=(0, 0, 0))
    else:
        draw.text((840, 682), name, font=fnt_name, fill=(0, 0, 0))

    # Signature
    if len(sign) >= 14:
        draw.text((1353, 1060), sign, font=fnt_sign, fill=(0, 0, 0))
    else:
        draw.text((1426, 1060), sign, font=fnt_sign, fill=(0, 0, 0))

    #QR Code
    img.paste(qr_img, (894, 1070))
    img.save('tmp/minted-certificate.png')
    return 0





createCertificate(name, sign, formatted_description, company, role)