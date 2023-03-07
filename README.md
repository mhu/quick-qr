# Quick QR

Quick QR is a utility that lets you create a QR code from the contents of your clipboard or from custom input to the command line.

## Getting Started

Create a virtual environment and install the dependencies.

```bash
cd quick-qr/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Additionally, the [qqr](qqr) file can be moved to `/usr/local/bin/` and made executable to enable functionality system-wide.

```bash
cp qqr /usr/local/bin/qqr
chmod + x /usr/local/bin/qqr
```

## Usage

You can call the Python script directly or install the utility globally (by making [qqr](qqr) executable and moving it to e.g. `/usr/local/bin/`).

The following examples will create QR codes containing the given strings:

```bash
qqr some text
qqr https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Alternatively, you can call the utility without providing an input, which will create a QR code for your current clipboard contents.

```bash
qrr
```

## Built With

* [qrcode](https://github.com/lincolnloop/python-qrcode) - Python QR Code image generator
* [Pillow](https://github.com/python-pillow/Pillow) - Python Imaging Library
* [xclip](https://github.com/astrand/xclip) - Command line interface to the X11 clipboard
