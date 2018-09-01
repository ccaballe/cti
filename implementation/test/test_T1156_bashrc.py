import os
import unittest

from implementation.detection.technique_T1156_bashrc import T1156_bashrc


class TestT1156_bashrc(unittest.TestCase):

    def test_detection(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        input_config = {
            'PCAP_FILE': dir_path + '/input_T1156_.bashrc/output_test/testcontainer.pcap',
            'SCAP_FILE': dir_path + '/input_T1156_.bashrc/output_test/testcontainer.scap.gz'
        }
        t1156_bashrc_config = {
            'bashrcfile': '/home/developer/.bashrc'
        }
        t1156 = T1156_bashrc(input_config, t1156_bashrc_config)

        self.assertEqual(True, t1156.detect())


if __name__ == '__main__':
    unittest.main()
