#!/usr/bin/env python3

import qrcode
import qrcode.image.svg


def generate_qrcode(url, filepath=None):
    if filepath is None:
        filepath = "figures/qr_code.svg"
    factory = qrcode.image.svg.SvgFillImage
    img = qrcode.make(url, image_factory=factory)
    img.save(filepath)


def main():
    generate_qrcode(
        url="https://github.com/scikit-hep/pyhf", filepath="figures/github_qr_code.svg"
    )


if __name__ == "__main__":
    main()
