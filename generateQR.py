import qrcode
import qrcode.image.svg
from PIL import Image

from verify_cid import verify_cid


def generateQR(CID):
        # input_data = f"https://{CID}.ipfs.dweb.link/"

        input_data= f"https://nf9dlh.deta.dev/verify/{CID}"
        #Creating an instance of qrcode
        qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5)
        qr.add_data(input_data)
        qr.make(fit=True)

        # factory = qrcode.image.svg.SvgPathImage
        # img = qrcode.make(input_data, image_factory = factory)

        img = qr.make_image(fill='black', back_color='white')
        img.save('assets/qr.png')
        return input_data

print(generateQR("bafybeidr6g2jm64uv4gzdtg4ukun6fqg4df2vg6zdvgcllmt7qfi3wry5i"))