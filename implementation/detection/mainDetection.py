from implementation.config.config import INPUT_CONFIG, T1156_BASHRC_CONFIG
from implementation.detection.technique_T1156_bashrc import T1156_bashrc


class MainDetection(object):

    def run(self):
        config = INPUT_CONFIG
        # t1176 = T1176BrowserExtensions(config)
        # print (t1176.detect())
        t1156_config = T1156_BASHRC_CONFIG
        # print (t1176.analysis())
        t1156 = T1156_bashrc(config, t1156_config)
        print (t1156.detect())
        # print (t1156.analysis())
        # t1067 = T1067Bootkit(config)
        # print (t1067.detect())
        # print (t1067.analysis())
        # t1136_config = T1136_CREATE_ACCOUNT_CONFIG
        #
        # t1136 = T1136CreateAccount(config, t1136_config)
        # print (t1136.detect())
        # print (t1136.analysis())
        # t1158 = T1158HiddenFilesAndDirectories(config)
        # print (t1158.detect())
        # print (t1158.analysis())
        # t1215_config = T1215_CONFIG
        # t1215 = T1215KernelModulesAndExtensions(config, t1215_config)
        # print (t1215.detect())
        # print (t1215.analysis())
        # t1168_config = T1168_CONFIG
        # t1168 = T1168LocalJobScheduling(config, t1168_config)
        # print (t1168.detect())
        # print (t1168.analysis())
        # t1205 = T1205PortKnocking(config)
        # print (t1205.detect())
        # print (t1205.analysis())
        # t1108 = T1108RedundantAccess(config)
        # print (t1108 .detect())
        # print (t1108.analysis())
        # t1154 = T1154Trap(config)
        # print (t1154.detect())
        # print (t1154.analysis())
        # t1078_config = T1078_VALID_ACCOUNT_CONFIG
        # t1078 = T1078ValidAccounts(config, t1078_config)
        # print (t1078.detect())
        # print (t1078.analysis())
        # t1100 = T1100WebShell(config)
        # print (t1100.detect())
        # print (t1100.analysis())
        # print "END"


if __name__ == '__main__':
    MainDetection().run()
