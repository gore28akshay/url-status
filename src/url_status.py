import requests

def get_url_status(url):
  url_info = requests.get(url)
  status = url_info.status_code
  response_time = url_info.elapsed.total_seconds() * 1000
  return [url, status, response_time]
