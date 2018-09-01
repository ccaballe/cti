# Python 2

from implementation.data_sources.FileMonitoring import FileMonitoring
from implementation.data_sources.ProcessCommandLineParameters import ProcessCommandLineParameters
from implementation.data_sources.ProcessMonitoring import ProcessMonitoring
from implementation.data_sources.ProcessUseOfNetwork import ProcessUseOfNetwork
from implementation.detection.detection import Detection


class T1156_bashrc(Detection):


    def analysis(self):
        tech = self.get_technique_by_name(".bash_profile and .bashrc")
        print(tech[0].x_tfm_commands_allowed)

    # TODO correlate with other data sources
    def detect(self):
        # .bashrc monitoring
        bashrc_monitoring = self.get_data_sources_info()[0]
        if bashrc_monitoring["data"] != "":
            return True
        return False

    def get_data_sources(self):
        return [
            FileMonitoring(self.input_config, self.tech_config["bashrcfile"]),
            ProcessMonitoring(self.input_config, process="bash"),
            ProcessCommandLineParameters(self.input_config),
            ProcessUseOfNetwork(self.input_config, "bash")
        ]
