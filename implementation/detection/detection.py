# Python 2
import os
from abc import ABCMeta, abstractmethod

from stix2 import Filter


class Detection:
    __metaclass__ = ABCMeta

    def __init__(self, input_config, tech_config=None):
        self.input_config = input_config
        self.tech_config = tech_config

    def get_technique_by_name(self, name):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        from stix2 import FileSystemStore
        fs = FileSystemStore(dir_path + "/../enterprise-attack")
        filt = [
            Filter('type', '=', 'attack-pattern'),
            Filter('name', '=', name)
        ]
        return fs.query(filt)

    @abstractmethod
    def get_data_sources(self):
        pass

    @abstractmethod
    def detect(self):
        pass

    @abstractmethod
    def analysis(self):
        pass

    def get_data_sources_info(self):
        result = list()
        data_sources = self.get_data_sources()
        for data_source in data_sources:
            data_source_element = dict()
            data_source_element["name"] = data_source.name
            data_source_element["data"] = data_source.filter_data
            result.append(data_source_element)
        return result
