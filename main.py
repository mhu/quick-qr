#!/usr/bin/env python3
import sys

import qrcode


if len(sys.argv) < 2:
    print("No message specified")
    sys.exit(1)

message = " ".join(sys.argv[1:])

qr_code = qrcode.QRCode()
qr_code.add_data(message)
qr_code.make(fit=True)

img = qr_code.make_image(fill_color="black", back_color="white")
img.show()
