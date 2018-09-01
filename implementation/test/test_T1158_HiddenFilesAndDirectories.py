import os
import unittest

from implementation.detection.technique_T1158HiddenFilesAndDirectories import T1158HiddenFilesAndDirectories


class TestT1158_HiddenFilesAndDirectories(unittest.TestCase):

    def test_detection(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        input_config = {
            'PCAP_FILE': dir_path + '/input_T1158_HiddenFiles/output_test/testcontainer.pcap',
            'SCAP_FILE': dir_path + '/input_T1158_HiddenFiles/output_test/testcontainer.scap.gz'
        }
        t1158 = T1158HiddenFilesAndDirectories(input_config)
        self.assertEqual(True, t1158.detect())


if __name__ == '__main__':
    unittest.main()
