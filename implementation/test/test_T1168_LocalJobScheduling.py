import os
import unittest

from implementation.detection.technique_T1168LocalJobScheduling import T1168LocalJobScheduling


class TestT1168_LocalJobScheduling(unittest.TestCase):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    t1168_local_job_scheduling_config = {
        'command_list': ['cron', 'crontab', 'at'],
        'file_list': ['/etc/crontab'],
        'dir_list': ['/etc/cron.d/']
    }

    def test_detection_at(self):
        input_config = {
            'PCAP_FILE': self.dir_path + '/input_T1168_LocalJobScheduling_at/output_test/testcontainer.pcap',
            'SCAP_FILE': self.dir_path + '/input_T1168_LocalJobScheduling_at/output_test/testcontainer.scap.gz'
        }

        t1168 = T1168LocalJobScheduling(input_config, self.t1168_local_job_scheduling_config)
        self.assertEqual(True, t1168.detect())

    def test_detection_cron(self):
        input_config = {
            'PCAP_FILE': self.dir_path + '/input_T1168_LocalJobScheduling_cron/output_test/testcontainer.pcap',
            'SCAP_FILE': self.dir_path + '/input_T1168_LocalJobScheduling_cron/output_test/testcontainer.scap.gz'
        }

        t1168 = T1168LocalJobScheduling(input_config, self.t1168_local_job_scheduling_config)
        self.assertEqual(True, t1168.detect())


if __name__ == '__main__':
    unittest.main()
