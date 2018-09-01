import os
import unittest

from implementation.detection.technique_T1067Bootkit import T1067Bootkit


class TestT1067_Bootkit(unittest.TestCase):

    def test_detection(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        input_config = {
            'HASH_FILE': dir_path + '/input_T1067_Bootkit/output_test/mbr.sha'
        }
        t1067 = T1067Bootkit(input_config)
        self.assertEqual(True, t1067.detect())


if __name__ == '__main__':
    unittest.main()
