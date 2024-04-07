# QR Code Generator

This Python script generates QR codes from input data. It uses the `qrcode` library to create the QR code images and the `Pillow` library to handle image processing.

## Installation

1. Make sure you have Python installed on your system.
2. Install the required libraries by running `pip install qrcode[pil]` in your terminal or command prompt.

## Usage

1. Clone this repository to your local machine.
2. Navigate to the directory containing the `customized_generate_qr.py` file.
3. Run the script using `python customized_generate_qr.py`.
4. Follow the prompts to enter the data to encode, filename to save the QR code, fill color, background color, box size, and border size.
5. After running the script, the specified QR code image will be generated in the same directory.

## Customization

You can customize the QR code by modifying the input data and parameters passed to the `generateQR` function in the script. Here are the customizable parameters:
- Data to encode: This is the text or URL you want the QR code to represent.
- Filename: Name of the file to save the QR code image. Default is `qr_code.png`.
- Fill color: Color of the QR code modules (black by default).
- Background color: Color of the QR code background (white by default).
- Box size: Size of each QR code module (20 by default).
- Border size: Size of the QR code border (4 by default).

## Dependencies

- qrcode
- Pillow (Python Imaging Library)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Made with ❤️
