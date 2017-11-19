#!/usr/bin/env python
import os
import zipfile
import datetime
import socket

today = datetime.date.today()
backup_folder = 'C:\Analog'

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    print(get_ip())
    zipf = zipfile.ZipFile('backup-'+str(today)+'.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(backup_folder, zipf)
    zipf.close()