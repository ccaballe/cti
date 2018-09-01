# Python 2


from implementation.data_sources.DataSource import DataSource


class PacketCapture(DataSource):

    def name(self):
        return "Packet Capture"

    def filter_data(self):
        packets = self.get_network_monitor_info()
        return packets
