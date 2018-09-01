import os
import unittest

from implementation.detection.technique_T1078ValidAccounts import T1078ValidAccounts


class TestT1078_ValidAccounts(unittest.TestCase):

    def test_detection(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        input_config = {
            'SCAP_FILE': dir_path + '/input_T1078_ValidAccounts/output_test/testcontainer.scap.gz'
        }
        t1078_valid_account_config = {
            'command_list': ['useradd', 'adduser', 'usermod', 'groupmod', 'groupadd']
        }
        t1078 = T1078ValidAccounts(input_config, t1078_valid_account_config)
        self.assertEqual(True, t1078.detect())


if __name__ == '__main__':
    unittest.main()
