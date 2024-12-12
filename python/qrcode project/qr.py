import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=50,
                   border=1)

qr.add_data('https://www.youtube.com/watch?v=o-YBDTqX_ZU&ab_channel=MusRest')
qr.make(fit=True)

img = qr.make_image(fill_color="pink", back_color="white")
img.save("mycode.png")