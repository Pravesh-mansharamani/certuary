import os

import dotenv
import requests
from PIL import Image

from generateQR import generateQR


def pasteQR(CID):
    dotenv.load_dotenv()

    generateQR(CID)
    img  = Image.open('tmp/minted-certificate.png')
    qr_img = Image.open('assets/qr.png')
    qr_img = qr_img.resize((220,220))
    img.paste(qr_img, (894, 1070))
    img.save('tmp/minted-certificate.png')


    with open("tmp/minted-certificate.png", 'rb') as f:
        file = f.read()

    url = "https://api.estuary.tech/content/add"
    # print(bytes_certificate)
    name = 'faewfaw'

    payload = {}
    files = [
        ('data', (f'{name}', file, 'application/octet-stream'))
    ]
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ESTf4be2f1c-dd16-4813-a6d5-0dad7ec0b0d3ARY'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response


