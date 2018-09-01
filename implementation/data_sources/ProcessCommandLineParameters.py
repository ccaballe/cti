# Python 2
from implementation.data_sources.DataSource import DataSource


class ProcessCommandLineParameters(DataSource):

    def __init__(self, config, full_dump = None):
        self.full_dump = full_dump
        super(ProcessCommandLineParameters, self).__init__(config)

    def name(self):
        return "Process command-line parameters"

    def filter_data(self):
        if self.full_dump:
            return self.get_process_monitor_info()
        return self.get_process_monitor_info(command_lines=True)
