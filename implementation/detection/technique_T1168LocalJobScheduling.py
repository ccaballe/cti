# Python 2

from implementation.data_sources.FileMonitoring import FileMonitoring
from implementation.data_sources.ProcessCommandLineParameters import ProcessCommandLineParameters
from implementation.data_sources.ProcessMonitoring import ProcessMonitoring
from implementation.data_sources.SystemCalls import SystemCalls
from implementation.detection.detection import Detection


class T1168LocalJobScheduling(Detection):

    # TODO
    def analysis(self):
        tech = self.get_technique_by_name("Local Job Scheduling")
        print(tech[0])


    def detect(self):
        # if at is used, detection is true
        # if crond/crontab processes are executed and also /etc/crontab or /etc/cron.d are altered, detection is true
        at = False
        cron = False
        process_monitoring_events = [event for event in self.get_data_sources() if event.name == "Process Monitoring" ]
        file_monitoring_events = [event for event in self.get_data_sources() if event.name == "File Monitoring" ]
        for event in process_monitoring_events:
            if event.process == "at":
                at = "" != event.filter_data
            if event.process == "crond" or event.process == "crontab":
                cron = "" != event.filter_data
        if at:
            return True
        if cron:
            for event in file_monitoring_events:
                if event.file == "/etc/crontab" and event.filter_data != "":
                    return True
                # TODO check also if /etc/crond.d directories (regex in sysdig)?
        return False


    def get_data_sources(self):
        result = list()
        # TODO commands in a list instead of one method for each
        for command in self.tech_config["command_list"]:
            result.append(ProcessMonitoring(self.input_config, command))
        for file in self.tech_config["file_list"]:
            result.append(FileMonitoring(self.input_config, file))
        return result

