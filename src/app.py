#!/usr/local/bin/python3
import url_status
from prometheus_client import start_http_server, Gauge

urls = []
url_file = open("urls.txt", "r")
for i in url_file.readlines():
    urls.append(i.strip())
url_file.close()

if __name__ == '__main__':
    start_http_server(80)
    label_url_status = ['url']
    g1 = Gauge('sample_external_url_up','Status of URL',labelnames=label_url_status)
    g2 = Gauge('sample_external_url_response_ms','Response time of URL',labelnames=label_url_status)
    while True:
        for i in urls:
            values = url_status.get_url_status(i)
            if values[1] == 200:
                g1.labels(url=values[0]).set(1)
            else:
                g1.labels(url=values[0]).set(0)
            g2.labels(url=values[0]).set(values[2])
            # print(values)
#comment to test github actions
