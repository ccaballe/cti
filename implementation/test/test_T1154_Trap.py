import os
import unittest

from implementation.detection.technique_T1154Trap import T1154Trap


class TestT1154_Trap(unittest.TestCase):

    def test_detection(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        input_config = {
            'PCAP_FILE': dir_path + '/input_T1154_Trap/output_test/testcontainer.pcap',
            'SCAP_FILE': dir_path + '/input_T1154_Trap/output_test/testcontainer.scap.gz'
        }
        t1154 = T1154Trap(input_config)
        self.assertEqual(True, t1154.detect())


if __name__ == '__main__':
    unittest.main()
