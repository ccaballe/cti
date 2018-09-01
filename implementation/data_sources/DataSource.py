# Python 2
from abc import ABCMeta, abstractmethod
from scapy.all import *
import subprocess


class DataSource:
    __metaclass__ = ABCMeta

    def __init__(self, config):
        self.config = config
        self.name = self.name()
        self.filter_data = self.filter_data()


    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def filter_data(self):
        pass

    def get_network_monitor_info(self):
        packets = rdpcap(self.config["PCAP_FILE"])
        # packets.display()
        return packets
        # for packet in packets:
        #     packet.
        #     # We're only interested packets with a DNS Round Robin layer
        #     if packet.haslayer(DNSRR):
        #         # If the an(swer) is a DNSRR, print the name it replied with.
        #         if isinstance(packet.an, DNSRR):
        #             print(packet.an.rrname)
        # pass

    def get_file_monitor_info(self, file=None):
        if file:
            command = 'sysdig -r ' + self.config["SCAP_FILE"] + ' -c spy_file "RW ' + file + '" 2>/dev/null'
        else:
            command = 'sysdig -r ' + self.config["SCAP_FILE"] + ' -c spy_file 2>/dev/null'
        return self.__get_output_command(command)

    def get_process_monitor_info(self, process=None, command_lines=None, proc_net=None):
        if process:
            command = 'sysdig -r ' + self.config["SCAP_FILE"] + ' proc.name=' + process + ' 2>/dev/null'
            return self.__get_output_command(command)
        if command_lines:
            command = 'sysdig -r ' + self.config["SCAP_FILE"] + ' -c spy_users 2>/dev/null'
            return self.__get_output_command(command)
        if proc_net:
            command = 'sysdig -r ' + self.config["SCAP_FILE"] + ' -c netstat "proc.name="' + proc_net + '  2>/dev/null'
            return self.__get_output_command(command)
        else:
            command = 'sysdig -r ' + self.config["SCAP_FILE"] + '  2>/dev/null'
            return self.__get_output_command(command)

    def get_syscall_monitor_info(self):
        command = 'sysdig -r ' + self.config["SCAP_FILE"] + ' -c topscalls 2>/dev/null'
        return self.__get_output_command(command)

    def get_browser_extensions_monitor_info(self):
        return self.__read_file__(self.config["EXTENSIONS_FILE"])

    def get_boot_record_monitor_info(self):
        return self.__read_file__(self.config["HASH_FILE"])

    @staticmethod
    def __read_file__(file):
        with open(file) as f:
            my_lines = f.readlines()
            return my_lines

    @staticmethod
    def __get_output_command(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        out, err = process.communicate()
        return out


