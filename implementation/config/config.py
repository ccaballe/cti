INPUT_CONFIG = {
    'EXTENSIONS_FILE': '/path/to/newbrowserextensions.txt',
    'SCAP_FILE': '/path/to/ccaballero/test.scap.gz',
    'PCAP_FILE': '/path/to/ccaballero/capturepackets.pcap',
    'HASH_FILE': '/path/to/ccaballero/mbr.sha',

}

T1156_BASHRC_CONFIG = {
  'bashrcfile':  '/home/developer/.bashrc'
}

T1078_VALID_ACCOUNT_CONFIG = {
    'command_list': ['usermod', 'groupmod']
}
T1136_CREATE_ACCOUNT_CONFIG = {
    'command_list': ['useradd', 'adduuser']
}
T1215_CONFIG = {
    'process': 'yum'
}
T1168_CONFIG = {
    'command_list': ['crond', 'crontab', 'at'],
    'file_list': ['/etc/crontab']
}





