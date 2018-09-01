# Python 2


from implementation.data_sources.DataSource import DataSource


class NetworkProtocolAnalysis(DataSource):

    def name(self):
        return "Network Protocol Analysis"

    def filter_data(self):
        packets = self.get_network_monitor_info()
        # TODO is needed filter for network protocol analysis
        return packets
