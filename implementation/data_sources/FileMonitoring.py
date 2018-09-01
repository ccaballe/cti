# Python 2
from implementation.data_sources.DataSource import DataSource


class FileMonitoring(DataSource):

    def __init__(self, config, file = None):
        self.file = file
        super(FileMonitoring, self).__init__(config)

    def name(self):
        return "File Monitoring"

    def filter_data(self):
        return self.get_file_monitor_info(self.file)
