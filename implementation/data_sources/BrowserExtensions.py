# Python 2
from implementation.config.config import INPUT_CONFIG
from implementation.data_sources.DataSource import DataSource


class BrowserExtensions(DataSource):

    def name(self):
        return "Browser Extensions"

    def filter_data(self):
        return self.get_browser_extensions_monitor_info()
