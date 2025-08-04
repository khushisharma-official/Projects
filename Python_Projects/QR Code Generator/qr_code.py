import qrcode as qr

img = qr.make("https://www.youtube.com/@Formula1")

img.save("Formula1_Youtube.png")