#!/usr/bin/env python3

import qrcode
from PIL import Image


def create_qr(data, filename="qrcode.png"):
    """
    Create a QR code from arbitrary text or a URL.

    Args:
        data (str): The text or URL to encode.
        filename (str): Output PNG filename.
    """

    qr = qrcode.QRCode(
        version=None,  # Automatically choose the required QR size
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    alpha = image.getchannel("R")
    alpha = alpha.point(lambda x: 255 - x)

    # Create black RGB channels
    black = Image.new("L", image.size, 0)

    # Merge into RGBA
    image = Image.merge("RGBA", (black, black, black, alpha))

    image.save(filename, "PNG")

    print(f"QR code saved as: {filename}")


if __name__ == "__main__":
    print("QR Code Generator")
    print("-----------------")

    data = input("Enter text or URL: ").strip()

    if not data:
        print("Error: No text or URL provided.")
    else:
        filename = input("Output filename [qrcode.png]: ").strip() or "qrcode.png"

        # Add .png automatically if omitted
        if not filename.lower().endswith(".png"):
            filename += ".png"

        create_qr(data, filename)
