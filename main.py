#!/usr/bin/env python3
"""Front Page — 21 November 2026.

Six verified stories from Saturday 21 November 2026, laid out as a
newspaper front page: Russian missiles hit Poland, the first
Trump–Xi–Putin trilateral summit ends, Wall Street slumps into
correction, deadly Russian strikes pound Kyiv, the World Court rules
Myanmar committed genocide against the Rohingya, and Cyclone Akvan
slams India's east coast.

Copies the front-page image (entry.png) into the output directory and
verifies the copy before reporting success. Pure standard library, no
network access, fully deterministic — the output is a byte-for-byte copy
of the image shipped with this entry.
"""

import hashlib
import os
import shutil
import sys

SOURCE = "entry.png"
MAX_BYTES = 1_048_576
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def fail(message):
    print("ERROR: " + message, file=sys.stderr)
    sys.exit(1)


def jpeg_dimensions(data):
    """Read width and height from the JPEG start-of-frame marker.

    Scans segment markers until it finds a SOF marker (0xC0-0xCF
    excluding 0xC4, 0xC8 and 0xCC) and returns (width, height).
    """
    pos = 2  # skip the SOI marker (FF D8)
    while pos + 9 <= len(data):
        if data[pos] != 0xFF:
            fail("corrupt JPEG: expected marker at offset %d" % pos)
        marker = data[pos + 1]
        if marker == 0xD8 or marker == 0x01 or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        seg_len = (data[pos + 2] << 8) | data[pos + 3]
        if seg_len < 2 or pos + 2 + seg_len > len(data):
            fail("corrupt JPEG: bad segment length at offset %d" % pos)
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                      0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            height = (data[pos + 5] << 8) | data[pos + 6]
            width = (data[pos + 7] << 8) | data[pos + 8]
            return width, height
        pos += 2 + seg_len
    fail("corrupt JPEG: no start-of-frame marker found")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, SOURCE)

    if not os.path.isfile(source):
        fail("source image %s not found" % source)

    shutil.copyfile(source, dest)

    with open(dest, "rb") as fh:
        data = fh.read()

    if len(data) == 0:
        fail("output file is empty")
    if len(data) > MAX_BYTES:
        fail("output is %d bytes, over the %d byte limit" % (len(data), MAX_BYTES))
    if data[0:2] != b"\xff\xd8":
        fail("output does not start with JPEG magic bytes FF D8")
    if data[-2:] != b"\xff\xd9":
        fail("output does not end with JPEG magic bytes FF D9")
    width, height = jpeg_dimensions(data)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        fail("dimensions are %dx%d, expected %dx%d"
             % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT))

    digest = hashlib.sha256(data).hexdigest()
    print("wrote %s (%d bytes, sha256 %s)" % (dest, len(data), digest))


if __name__ == "__main__":
    main()
