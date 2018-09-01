import os
import unittest

from implementation.detection.technique_T1100WebShell import T1100WebShell


class TestT1100_WebShell(unittest.TestCase):

    def test_detection(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        input_config = {
            'PCAP_FILE': dir_path + '/input_T1100_WebShell/output_test/testcontainer.pcap',
            'SCAP_FILE': dir_path + '/input_T1100_WebShell/output_test/testcontainer.scap.gz'
        }
        t1100 = T1100WebShell(input_config)
        self.assertEqual(True, t1100.detect())


if __name__ == '__main__':
    unittest.main()
