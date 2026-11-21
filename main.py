#!/usr/bin/env python3
"""Ship the 21 November 2026 front page.

The entry is one picture, entry.png, a 1024 by 1024 JPEG of the day's
front page. Running this file drops an exact copy of that picture into
the output folder and refuses to finish unless the copy checks out:
right size on disk, JPEG opening and closing markers, and 1024 by 1024
pixels read from the frame header. Only the standard library is used,
nothing is fetched from the network, and the same input always gives
the same output.
"""

from hashlib import sha256
from os import environ, makedirs
from os.path import abspath, dirname, isfile, join
from shutil import copyfile
from struct import unpack
from sys import exit as finish, stderr

PICTURE = "entry.png"
CEILING = 1048576
SIDE = 1024


def abort(text):
    stderr.write("refused: " + text + "\n")
    finish(1)


def frame_size(blob):
    """Pull (width, height) out of a JPEG byte string.

    Walk the marker segments from the start; the first start-of-frame
    segment carries the height and then the width as big-endian pairs.
    """
    cursor = 2
    while cursor + 9 <= len(blob):
        head = blob[cursor]
        if head != 0xFF:
            abort("marker expected at byte %d" % cursor)
        code = blob[cursor + 1]
        if code in (0xD8, 0x01) or 0xD0 <= code <= 0xD7:
            cursor += 2
            continue
        (span,) = unpack(">H", blob[cursor + 2:cursor + 4])
        if span < 2 or cursor + 2 + span > len(blob):
            abort("segment at byte %d has a bad length" % cursor)
        if code in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                    0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            (tall,) = unpack(">H", blob[cursor + 5:cursor + 7])
            (wide,) = unpack(">H", blob[cursor + 7:cursor + 9])
            return wide, tall
        cursor += 2 + span
    abort("no frame header in this file")


def run():
    folder = dirname(abspath(__file__))
    origin = join(folder, PICTURE)
    target_dir = environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    makedirs(target_dir, exist_ok=True)
    target = join(target_dir, PICTURE)
    if not isfile(origin):
        abort("missing picture: " + origin)
    copyfile(origin, target)
    with open(target, "rb") as handle:
        blob = handle.read()
    if not blob:
        abort("the copy came out empty")
    if len(blob) > CEILING:
        abort("copy is %d bytes, over the %d limit" % (len(blob), CEILING))
    if blob[:2] != b"\xff\xd8":
        abort("copy lacks the JPEG opening bytes")
    if blob[-2:] != b"\xff\xd9":
        abort("copy lacks the JPEG closing bytes")
    wide, tall = frame_size(blob)
    if (wide, tall) != (SIDE, SIDE):
        abort("picture is %d by %d, wanted %d by %d"
              % (wide, tall, SIDE, SIDE))
    print("wrote %s (%d bytes, sha256 %s)"
          % (target, len(blob), sha256(blob).hexdigest()))
    # Success: the copy is byte-for-byte the picture this entry ships.


if __name__ == "__main__":
    run()
