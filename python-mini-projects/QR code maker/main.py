import qrcode

link=input("Enter the URL: ")
qr=qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(link)
qr.make()

img=qr.make_image(fill_color="white", back_color="green")
save_as=input("Save as: ")
img.save(f"{save_as}.png")