import os
from io import BytesIO

import requests
from deta import Deta
from dotenv import load_dotenv


def pinToIPFS():
  # load_dotenv()  # take environment variables from .env.
  # API_KEY = os.getenv("API_KEY")
  # deta = Deta("b0f571t2_7WegmFsVjsimbaHQPhZvpn9aZYv74M3E")
  # drive = deta.Drive('certificate')
  # content = drive.get('Certificate.png')
  # bytes_certificate = content.read()
  # content.close()

  FILENAME="tmp/minted-certificate.png"
  url = "https://api.estuary.tech/content/add"
  # print(bytes_certificate)
  name = 'faewfaw'

  payload={}
  files=[
    ('data',(f'{name}',open(FILENAME, 'rb'),'application/octet-stream'))
  ]
  headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ESTf4be2f1c-dd16-4813-a6d5-0dad7ec0b0d3ARY'
  }


  response = requests.request("POST", url, headers=headers, data=payload, files=files)


  return response.text

print(pinToIPFS())