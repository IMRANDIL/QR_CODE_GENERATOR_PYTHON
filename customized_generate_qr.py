import qrcode
from PIL import Image
import qrcode.constants

def generateQR(data, filename="qr_code.png", fill_color="black", back_color="white", box_size=20, border=4):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border
    )

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Add a logo or image overlay here if desired
    # Example: img.paste(logo_image, (x, y))

    img.save(filename)

if __name__ == "__main__":
    data = input("Enter the data to encode: ")
    filename = input("Enter the filename to save the QR code (optional, default: qr_code.png): ") or "qr_code.png"
    fill_color = input("Enter the fill color for the QR code (optional, default: black): ") or "black"
    back_color = input("Enter the background color for the QR code (optional, default: white): ") or "white"
    box_size = input("Enter the box size for the QR code (optional, default: 20): ")
    box_size = int(box_size) if box_size else 20
    border = input("Enter the border size for the QR code (optional, default: 4): ")
    border = int(border) if border else 4

    generateQR(data, filename, fill_color, back_color, box_size, border)
