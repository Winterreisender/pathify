import unittest
import pathify
from pathlib import Path
import os

class Test(unittest.TestCase):
    def test_simple(self):
        src_file = Path("sample.mp4")
        dst_folder = Path("sample.mp4.d")
        reconstructed_file = Path("sample_reconstructed.mp4")

        #shutil.rmtree(dst_folder)
        os.makedirs(dst_folder)

        pathify.encode(src_file, dst_folder)
        pathify.decode(dst_folder, reconstructed_file)