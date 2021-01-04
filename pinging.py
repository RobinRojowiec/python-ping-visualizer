import csv
import re
import subprocess
import time
from datetime import datetime


def ping(ip):
    """
    Send a ping request to server and parse response time from response text
    :param ip:
    :return:
    """
    try:
        response = str(subprocess.check_output("ping -a -n 1 " + ip, shell=True))
        m = re.search("Zeit=([0-9]+)ms", response)
        return m.group(1)
    except:
        return -1


if __name__ == '__main__':
    url = "8.8.8.8"
    name = '{0:%Y-%m-%d_%H_%M_%S}'.format(datetime.now())
    with open(name + '_ping_report.csv', 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["ip", "avg_rtt", "ret_code"])
        while True:
            ping_time = ping(url)
            print("Ping " + str(ping_time))
            writer.writerow([url, ping_time])
            time.sleep(0.2)
