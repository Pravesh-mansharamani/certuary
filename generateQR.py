import qrcode
import qrcode.image.svg
from PIL import Image


input_data = "https://bafkreigbd5f56mztpwnlkghlkxb7r2fmmpdky3prbroxpqcxdkiqqaq6wu.ipfs.dweb.link/"
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
img.save('qr.png')

