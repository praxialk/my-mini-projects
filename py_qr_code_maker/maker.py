import sys

try:
    import qrcode
except ImportError:
    print("Error: The 'qrcode' package is not installed.")
    print("Please install it using: pip install qrcode[pil]")
    sys.exit(1)

def generate_qr(data, filename="qrcode.png"):
    print(f"Generating QR Code for: {data}")
    # Provide basic configurations for the QR Code
    qr = qrcode.QRCode(
        version=1, # size of the QR Code (1 to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"Success! Saved to '{filename}'")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python maker.py <string_or_url> [output_filename.png]")
    else:
        text_data = sys.argv[1]
        out_file = sys.argv[2] if len(sys.argv) > 2 else "qrcode.png"
        generate_qr(text_data, out_file)
