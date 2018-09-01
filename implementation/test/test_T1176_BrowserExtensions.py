import os
import unittest

from implementation.detection.technique_T1176BrowserExtensions import T1176BrowserExtensions


class TestT1176BrowserExtensions(unittest.TestCase):

    # TODO this tests fails unless manually install a extension in the firefox from ubuntu docker
    def test_detection(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        input_config = {
            'EXTENSIONS_FILE': dir_path + '/input_T1176/BrowserExtensions/output_test/newbrowserextensions.txt',
            'PCAP_FILE': dir_path + '/input_T1176/BrowserExtensions/output_test/testcontainer.pcap',
            'SCAP_FILE': dir_path + '/input_T1176/BrowserExtensions/output_test/testcontainer.scap.gz'
        }
        t1176 = T1176BrowserExtensions(input_config)
        self.assertEqual(True, t1176.detect())


if __name__ == '__main__':
    unittest.main()
