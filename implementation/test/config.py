INPUT_CONFIG = {
    'EXTENSIONS_FILE': '/home/ccaballero/output_test/newbrowserextensions.txt',
    'SCAP_FILE': '/home/ccaballero/output_test/testcontainer.scap.gz',
    'PCAP_FILE': '/home/ccaballero/output_test/testcontainer.pcap',
    'HASH_FILE': '/home/ccaballero/output_test/mbr.sha'

}

T1156_BASHRC_CONFIG = {
    'bashrcfile':  '/home/developer/.bashrc'
}

T1078_VALID_ACCOUNT_CONFIG = {
    'command_list': ['useradd', 'adduser', 'usermod', 'groupmod', 'groupadd']
}
T1136_CREATE_ACCOUNT_CONFIG = {
    'command_list': ['useradd', 'adduser']
}
T1215_KERNEL_MODULES_CONFIG = {
    'command_list': ['apt-get', 'modprobe', 'insmod', 'lsmod', 'rmmod', 'modinfo']
}
T1168_LOCAL_JOB_SCHEDULING_CONFIG = {
    'command_list': ['cron', 'crontab', 'at'],
    'file_list': ['/etc/crontab'],
    'dir_list': ['/etc/cron.d/']
}







