import os
import unittest

from implementation.detection.technique_T1136CreateAccount import T1136CreateAccount


class TestT1136CreateAccount(unittest.TestCase):

    def test_detection(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        input_config = {
            'PCAP_FILE': dir_path + '/input_T1136_CreateAccount/output_test/testcontainer.pcap',
            'SCAP_FILE': dir_path + '/input_T1136_CreateAccount/output_test/testcontainer.scap.gz'
        }
        t1136_create_account_config = {
            'command_list': ['useradd', 'adduser']
        }
        t1136 = T1136CreateAccount(input_config, t1136_create_account_config)
        self.assertEqual(True, t1136.detect())


if __name__ == '__main__':
    unittest.main()
