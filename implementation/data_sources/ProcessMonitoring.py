# Python 2
from implementation.data_sources.DataSource import DataSource


class ProcessMonitoring(DataSource):

    def __init__(self, config, process=None):
        self.process = process
        super(ProcessMonitoring, self).__init__(config)

    def name(self):
        return "Process Monitoring"

    def filter_data(self):
        return self.get_process_monitor_info(process=self.process)
