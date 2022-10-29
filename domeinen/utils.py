# domeinen/utils.py

import urllib .request as urllib

# functio to check if url is online
def urlisonline(url):
  try:
    response = urllib.urlopen(url)
    print('response code: ', response.getcode())
    return response.getcode()
  except:
    return ('Not Found')