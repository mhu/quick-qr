#!/usr/bin/env python3
import sys

import pyperclip
import qrcode


def get_message():
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])

    clipboard_content = pyperclip.paste()

    if len(clipboard_content) == 0:
        print("No message specified")
        sys.exit(1)

    return clipboard_content


qr_code = qrcode.QRCode()
qr_code.add_data(get_message())
qr_code.make(fit=True)

img = qr_code.make_image(fill_color="black", back_color="white")
img.show()
