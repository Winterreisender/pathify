import os
from pathlib import Path
import base64
import re

CHUNK_SIZE = 72
RE_SPLIT_ID_CONTENT = re.compile(r"([0-9a-f]+)_(\S+)")

def encode(src_file :Path, dst_folder :Path):
    with open(src_file, 'rb') as f:
        fileiter = iter(lambda: f.read(CHUNK_SIZE), b'')
        for i,chunk in enumerate(fileiter):
            encoded = base64.urlsafe_b64encode(chunk).decode()
            os.mkdir(dst_folder/ f"{i:x}_{encoded}")


def decode(src_folder :Path, dst_file :Path):
    f = open(dst_file, 'wb')
    for i in src_folder.iterdir():
        m = re.match(RE_SPLIT_ID_CONTENT, i.name)
        _chunck_id_hex, _chunk_b64 = m.groups()
        chunck_id = int(_chunck_id_hex, base=16)
        chunck_content = base64.urlsafe_b64decode(_chunk_b64)

        f.seek(chunck_id*CHUNK_SIZE)
        f.write(chunck_content)

    f.close()
