import io
import os

import dotenv
import requests
import requests as requests
from PIL import Image, ImageFont, ImageDraw
import datetime
import textwrap

from deta import Deta

from generateQR import generateQR
from pasteQR import pasteQR
from pinToIPFS import pinToIPFS



# Wrap text at a maximum line width of 80 characters


# main function
def createCertificate(name, sign, desc, company, role):
    dotenv.load_dotenv()

    description = textwrap.fill(desc, width=80)

    deta = Deta("b0f571t2_7WegmFsVjsimbaHQPhZvpn9aZYv74M3E")
    drive = deta.Drive('certificate')
    content = drive.get('Certificate.png')
    bytes_certificate = content.read()
    content.close()


    # qr_img = Image.open('assets/qr.png')

    img = Image.open(io.BytesIO(bytes_certificate))

    fnt_company = ImageFont.truetype(r'fonts/name.ttf', 45)
    fnt_description = ImageFont.truetype(r'fonts/general.ttf', 30)
    fnt_name = ImageFont.truetype(r'fonts/name.ttf', 45)
    fnt_date = ImageFont.truetype(r'fonts/name.ttf', 35)
    fnt_sign = ImageFont.truetype(r'fonts/sign.ttf', 45)
    fnt_role = ImageFont.truetype(r'fonts/name.ttf', 30)

    #Current date
    d = datetime.datetime.now()
    current_date = d.strftime("%d") + " " + d.strftime("%B") + ", " + d.strftime("%Y")
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
    # img.paste(qr_img, (894, 1070))
    img.save('tmp/minted-certificate.png')

    # create and use as many Drives as you want!
    photos = deta.Drive("certificate")


    with open("tmp/minted-certificate.png", 'rb') as f:
        file = f.read()

    url = "https://api.estuary.tech/content/add"
    # print(bytes_certificate)
    name = 'faewfaw'

    payload = {}
    files = [
        (('data', (f'{name}', file), 'application/octet-stream'))
    ]
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ESTf4be2f1c-dd16-4813-a6d5-0dad7ec0b0d3ARY'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)


    # print(res)

    photos.put("/works/minted-certificate.png", img_bytes)

    return response





