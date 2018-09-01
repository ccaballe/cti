# Python 2
from implementation.data_sources.DataSource import DataSource


class ProcessUseOfNetwork(DataSource):

    def __init__(self, config, process=None):
        self.process = process
        super(ProcessUseOfNetwork, self).__init__(config,)

    def name(self):
        return "Process use of network"

    def filter_data(self):
        return self.get_process_monitor_info(proc_net=self.process)
