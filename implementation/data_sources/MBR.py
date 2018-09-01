# Python 2


from implementation.data_sources.DataSource import DataSource


class MBR(DataSource):

    def name(self):
        return "MBR"

    def filter_data(self):
        return self.get_boot_record_monitor_info()
