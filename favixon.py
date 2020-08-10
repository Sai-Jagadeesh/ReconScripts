import mmh3
import requests
import codecs
import urllib3
 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
response = requests.get('https://websitename/favicon.ico', verify=False)
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print(hash)
