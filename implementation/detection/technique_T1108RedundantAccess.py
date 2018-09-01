# Python 2
from implementation.data_sources.FileMonitoring import FileMonitoring
from implementation.data_sources.NetworkProtocolAnalysis import NetworkProtocolAnalysis
from implementation.data_sources.PacketCapture import PacketCapture
from implementation.data_sources.ProcessMonitoring import ProcessMonitoring
from implementation.data_sources.ProcessUseOfNetwork import ProcessUseOfNetwork
from implementation.detection.detection import Detection


class T1108RedundantAccess(Detection):

    def analysis(self):
        tech = self.get_technique_by_name("Redundant Access")
        print(tech[0])

    # TODO
    def detect(self):
        # for event in self.get_data_sources_info():
            # print (event)
        return False

    def get_data_sources(self):
        return [
            ProcessMonitoring(self.input_config),
            ProcessUseOfNetwork(self.input_config),
            PacketCapture(self.input_config),
            NetworkProtocolAnalysis(self.input_config),
            FileMonitoring(self.input_config),
            # BinaryFileMetadata(),
            # AuthenticationLogs
            # TODO no data sources defined in MITRE
        ]
