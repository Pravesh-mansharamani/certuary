from deta import Deta

# Initialize with a Project Key
deta = Deta("b0f571t2_7WegmFsVjsimbaHQPhZvpn9aZYv74M3E")


# create and use as many Drives as you want!
photos = deta.Drive("certificate")
photos.put("mintedcertificate", "minted-certificate.png", content_type='text')





