# Python 2
from abc import ABCMeta, abstractmethod

from implementation.data_sources.BrowserExtensions import BrowserExtensions
from implementation.data_sources.NetworkProtocolAnalysis import NetworkProtocolAnalysis
from implementation.data_sources.PacketCapture import PacketCapture
from implementation.data_sources.ProcessMonitoring import ProcessMonitoring
from implementation.data_sources.ProcessUseOfNetwork import ProcessUseOfNetwork
from implementation.data_sources.SystemCalls import SystemCalls
from implementation.detection.detection import Detection


class T1176BrowserExtensions(Detection):

    def analysis(self):
        tech = self.get_technique_by_name("Browser Extensions")
        print(tech[0])

    # TODO correlate with more datasources
    # Detection is based on browser extensions directory. If there are some write events on the directory,
    # detection is true
    # Each line have the following structure:
    # <Event dir=True mask=0x40000100 maskname=IN_CREATE|IN_ISDIR name=[name] path=[path] pathname=[pathname] wd=1 >
    def detect(self):
        print "Starting detection Browser extensions"
        for datasource in self.get_data_sources_info():
            print datasource
        for event in self.get_data_sources_info()[0]["data"]:
            if event.find("maskname=IN_CREATE|IN_ISDIR"):
                print "A new extension found"
                return True
        return False

    def get_data_sources(self):
        return [
            BrowserExtensions(self.input_config),
            PacketCapture(self.input_config),
            SystemCalls(self.input_config),
            ProcessMonitoring(self.input_config, "chrome"),
            ProcessUseOfNetwork(self.input_config, "chrome"),
            NetworkProtocolAnalysis(self.input_config)
        ]
