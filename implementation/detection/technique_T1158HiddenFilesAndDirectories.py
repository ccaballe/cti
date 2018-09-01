# Python 2
from implementation.data_sources.FileMonitoring import FileMonitoring
from implementation.data_sources.ProcessCommandLineParameters import ProcessCommandLineParameters
from implementation.data_sources.ProcessMonitoring import ProcessMonitoring
from implementation.detection.detection import Detection


class T1158HiddenFilesAndDirectories(Detection):

    def analysis(self):
        tech = self.get_technique_by_name("Hidden Files and Directories")
        print(tech[0])

    # TODO correllate with more events
    def detect(self):
        for event in self.get_data_sources_info():
            if event["name"] == "File Monitoring":
                lines = event["data"].split("\n")
                # Find creation of hidden files
                filtered = [line for line in lines if "/." in line and "W" in line]
                print filtered
                if len(filtered) is not 0:
                    return True

        return False

    def get_data_sources(self):
        return [
            FileMonitoring(self.input_config),
            ProcessMonitoring(self.input_config),
            ProcessCommandLineParameters(self.input_config)
        ]
