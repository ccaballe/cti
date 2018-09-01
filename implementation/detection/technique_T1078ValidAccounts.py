# Python 2
from implementation.data_sources.ProcessMonitoring import ProcessMonitoring
from implementation.detection.detection import Detection


class T1078ValidAccounts(Detection):
    def analysis(self):
        tech = self.get_technique_by_name("Valid Accounts")
        print(tech[0])


    # If there are some processes of adduser, useradd, or usermod, groupmod... detection is true
    def detect(self):
        for event in self.get_data_sources_info():
            if event["name"] == "Process Monitoring" and event["data"] != "":
                return True

        return False

    def get_data_sources(self):
        result = list()
        #     # TODO commands in a list instead of one method for each
        for command in self.tech_config["command_list"]:
            result.append(ProcessMonitoring(self.input_config, command))
        return result

