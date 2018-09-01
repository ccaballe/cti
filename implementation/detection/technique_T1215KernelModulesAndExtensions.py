# Python 2

from implementation.data_sources.ProcessCommandLineParameters import ProcessCommandLineParameters
from implementation.data_sources.ProcessMonitoring import ProcessMonitoring
from implementation.data_sources.SystemCalls import SystemCalls
from implementation.detection.detection import Detection


class T1215KernelModulesAndExtensions(Detection):

    def analysis(self):
        tech = self.get_technique_by_name("Kernel Modules and Extensions")
        print(tech[0])

    # TODO correlate more events
    def detect(self):
        # Look for correlation between apt-get process and kernel processes (modprobe insmod lsmod rmmod modinfo)
        apt_get = False
        kernel_command = False
        for event in self.get_data_sources():
            if event.name == "Process Monitoring":
                if event.process == "apt-get":
                    apt_get = "" != event.filter_data
                if (event.process == "modprobe" or
                        event.process == "insmod" or
                        event.process == "lsmod" or
                        event.process == "rmmod" or
                        event.process == "modinfo"):
                    kernel_command = "" != event.filter_data
        return apt_get and kernel_command

    def get_data_sources(self):
        result = list()
        #  TODO commands in a list instead of one method for each
        for command in self.tech_config["command_list"]:
            result.append(ProcessMonitoring(self.input_config, command))

        result.append(SystemCalls(self.input_config))
        result.append(ProcessCommandLineParameters(self.input_config))
        return result
