from deta import Deta

# Initialize with a Project Key
deta = Deta("b0f571t2_7WegmFsVjsimbaHQPhZvpn9aZYv74M3E")

# with open("/Users/edisonqu/PycharmProjects/certuary/assets/Certificate.png", "rb") as image:
    # f = image.read()

# create and use as many Drives as you want!
photos = deta.Drive("certificate")

photos.put("/font/Certificate.png","/Users/edisonqu/PycharmProjects/certuary/fonts/general.ttf")