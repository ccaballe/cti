# Python 2

from implementation.data_sources.MBR import MBR
from implementation.detection.detection import Detection


class T1067Bootkit(Detection):

    def analysis(self):
        tech = self.get_technique_by_name("Bootkit")
        print(tech[0])
        return True

    # TODO correlate with more data sources
    # If some lines are different, it means that the mbr has been altered
    def detect(self):
        mbrdata = self.get_data_sources_info()[0]
        return len(set(mbrdata["data"])) > 1

    def get_data_sources(self):
        return [
            # TODO API Monitoring
            # TODO VBR
            MBR(self.input_config)
        ]
