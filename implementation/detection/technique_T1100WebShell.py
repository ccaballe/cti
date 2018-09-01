# Python 2
from implementation.data_sources.FileMonitoring import FileMonitoring
from implementation.data_sources.NetworkProtocolAnalysis import NetworkProtocolAnalysis
from implementation.data_sources.ProcessMonitoring import ProcessMonitoring
from implementation.detection.detection import Detection


class T1100WebShell(Detection):

    def analysis(self):
        tech = self.get_technique_by_name("Web Shell")
        print(tech[0])

    # if process apache exist, then find if there are file creation outside process space
    def detect(self):
        data_sources = self.get_data_sources_info()
        if data_sources[0]["data"] != "":
            lines = data_sources[1]["data"].split("\n")
            # filter allowed files when apache process can write
            write_lines = [line for line in lines if " W " in line and
                           "/var/run/apache2/apache2.pid" not in line and
                           "/var/log/apache2/access.log" not in line and
                           "/var/log/apache2/error.log" not in line and
                           "/var/www/html/" not in line and
                           "/dev/null" not in line]
            return len(write_lines) > 1
        return False

    def get_data_sources(self):
        return [
            # Anti-virus(),
            # AuthenticationLogs(),
            # Netflow/Enclave netflow
            ProcessMonitoring(self.input_config, "apache2"),
            FileMonitoring(self.input_config),
            NetworkProtocolAnalysis(self.input_config)
        ]
