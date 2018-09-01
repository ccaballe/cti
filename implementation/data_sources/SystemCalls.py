# Python 2


from implementation.data_sources.DataSource import DataSource


class SystemCalls(DataSource):

    def name(self):
        return "System calls"

    def filter_data(self):
        return self.get_syscall_monitor_info()
