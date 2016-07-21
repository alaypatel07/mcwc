from unittest import TestCase
from ns2_tr_extractor import file_extractor, get_pdr, get_throughput


class TestNS2Extractor(TestCase):
    def test_file_extractor(self):
        data = file_extractor("testOut.tr")
        with open("testOut.tr") as f:
            for datum in data:
                line = " ".join(datum)
                self.assertEqual(line, f.readline().rstrip("\n"))