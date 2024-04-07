import qrcode
from PIL import Image
import qrcode.constants

def generateQR():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=4
    )

    qr.add_data("https://github.com/IMRANDIL")
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="white")
    img.save("imrandil_github.png")

if __name__ == "__main__":
    generateQR()
