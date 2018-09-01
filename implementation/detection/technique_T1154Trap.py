# Python 2
from implementation.data_sources.FileMonitoring import FileMonitoring
from implementation.data_sources.ProcessCommandLineParameters import ProcessCommandLineParameters
from implementation.data_sources.ProcessMonitoring import ProcessMonitoring
from implementation.detection.detection import Detection


class T1154Trap(Detection):

    def analysis(self):
        tech = self.get_technique_by_name("Trap")
        print(tech[0])

    # Find trap commands in command line
    def detect(self):
        for event in self.get_data_sources_info():
            if event["name"] == "Process command-line parameters" and "trap" in event["data"]:
                return True
        return False

    def get_data_sources(self):
        return [
            FileMonitoring(self.input_config),
            ProcessMonitoring(self.input_config),
            ProcessCommandLineParameters(self.input_config, full_dump=True)
        ]
