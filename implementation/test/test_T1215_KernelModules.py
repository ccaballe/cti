import os
import unittest

from implementation.detection.technique_T1215KernelModulesAndExtensions import T1215KernelModulesAndExtensions


class TestT1215_KernelModule(unittest.TestCase):

    def test_detection(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        input_config = {
            'PCAP_FILE': dir_path + '/input_T1215_KernelModulesAndExtensions/output_test/testcontainer.pcap',
            'SCAP_FILE': dir_path + '/input_T1215_KernelModulesAndExtensions/output_test/testcontainer.scap.gz'
        }
        t1215_kernel_modules_config = {
            'command_list': ['apt-get', 'modprobe', 'insmod', 'lsmod', 'rmmod', 'modinfo']
        }
        t1215 = T1215KernelModulesAndExtensions(input_config, t1215_kernel_modules_config)

        self.assertEqual(True, t1215.detect())


if __name__ == '__main__':
    unittest.main()
