#imports
from proxmoxer import ProxmoxAPI
import configparser
import logging

#logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

#config init
config = configparser.ConfigParser()
config.read('config.ini')

#proxmox_settings
proxmox_host = config["Proxmox"]["host"]
proxmox_user = config["Proxmox"]["user"]
proxmox_realm = config["Proxmox"]["realm"]
proxmox_password = config["Proxmox"]["password"]
proxmox_ssl = False
proxmox_port = config["Proxmox"]["port"]

#proxmox api
proxmox_user_creds = proxmox_user + "@" + proxmox_realm

proxmox = ProxmoxAPI(proxmox_host, user=proxmox_user_creds, password=proxmox_password, verify_ssl=proxmox_ssl, port=proxmox_port)

def main():
    lxclist = proxmox.nodes("Beta").lxc.get()
    print(lxclist)
    
if __name__ == "__main__":
    main()
