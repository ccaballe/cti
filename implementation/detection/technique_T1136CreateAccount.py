# Python 2

from implementation.data_sources.ProcessCommandLineParameters import ProcessCommandLineParameters
from implementation.data_sources.ProcessMonitoring import ProcessMonitoring
from implementation.data_sources.SystemCalls import SystemCalls
from implementation.detection.detection import Detection


class T1136CreateAccount(Detection):

    def analysis(self):
        tech = self.get_technique_by_name("Create Account")
        print(tech[0])

    # TODO correlate with more datasources
    # If there are some processes of adduser, useradd... detection is true
    def detect(self):
        for datasource in self.get_data_sources_info():
            if datasource["name"] == "Process Monitoring" and datasource["data"] != "":
                return True
            if datasource["name"] == "Process command-line parameters" \
                    and ("useradd" in datasource["data"]
                         or "adduser" in datasource["data"]):
                return True
        return False

    def get_data_sources(self):
        result = list()
        #     # TODO commands in a list instead of one method for each
        for command in self.tech_config["command_list"]:
            result.append(ProcessMonitoring(self.input_config, command))
        result.append(ProcessCommandLineParameters(self.input_config))
        result.append(SystemCalls(self.input_config))
        return result
