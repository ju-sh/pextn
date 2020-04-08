import unittest

from pextn import pextn, UnknownExtension

class TestPextn(unittest.TestCase):
    def test_known_extensions(self):
        test_data = [
            "gz",   # lowercase
            ".o",   # lowercase with dot
            ".DB",  # uppercase with dot
            "PL",   # multiple results
        ] 
        for extension in test_data:
            result = pextn(extension)
            self.assertIsNotNone(result)

    def test_unknown_extensions(self):
        test_data = ["TVM", "HEY", "JOHN"]
        for tdata in test_data:
            with self.assertRaises(UnknownExtension):
                pextn(tdata)
