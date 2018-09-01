# Python 2

from implementation.detection.detection import Detection


class T1205PortKnocking(Detection):

    def analysis(self):
        tech = self.get_technique_by_name("Port Knocking")
        print(tech[0])

    # TODO
    def detect(self):
        for event in self.get_data_sources_info():
            print (event)
        return False

    def get_data_sources(self):
        return [
            # TODO no data sources defined in MITRE
        ]
