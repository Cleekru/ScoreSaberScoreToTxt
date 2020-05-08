from urllib.request import urlopen, Request
import re
import time
import configparser
import sys

config = configparser.ConfigParser()
config.read('config.ini')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
confurl = config['(REQUIRED) Your ScoreSaber.com URL']['url']
if confurl == '' or not re.match('https://scoresaber.com/u/', confurl):
    print('PLEASE SPECIFY YOUR SCORESABER URL IN THE config.ini FILE')
    time.sleep(6)
    sys.exit()
req = Request(url=confurl, headers=headers)
while(True):
    html = urlopen(req).read()

    result = re.search('global">(#[0-9,.]+)</.*png" /> (#[0-9,.]+).*nts:</strong> ([0-9.]+pp).*ount:</strong> ([0-9.,]+).* Score:</strong> ([0-9,]+)', str(html))
    o = 'Score Saber Ranking:\nWorldwide: ' + result.group(1) + ' ' + config['(optional) Settigns']['country'] + ': ' + result.group(2) + '\nPerformance Points: ' + result.group(3) + ' \nPlay Count: ' + result.group(4) + '\nTotal Score: ' + result.group(5)
    print(o)
    f = open(config['(optional) Settigns']['filename'], "w")
    f.write(o)
    f.close()
    time.sleep(int(config['(optional) Settigns']['refreshrate']))
