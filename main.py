import requests
import m3u8
from bs4 import BeautifulSoup
import subprocess

# ** convert to mp4 *****  subprocess.run(['ffmpeg', '-i', 'NAME OF .TS FILE', 'dwnloadedVid.mp4']) *****
import sched
import time
# event_schedule = sched.scheduler(time.time, time.sleep)
# TODO: CREATE SCHEDULER TO RUN SCRIPT AUTOMATICALLY (CHUNK EVERY 48 SEC)
# def stream():

chunks = 'chunks.m3u8'

# GET LINKS FROM PARENT WEBSITE (WORKS)
source = requests.get('http://nba-streams.xyz/schedule/').text
soup = BeautifulSoup(source, 'lxml')
links = []
for a in soup.find_all('a', href=True):

    links.append(a['href'])
del links[0]

# TODO: ITERATE THROUGH EACH STREAM AND GET .TS

for nbaStream in links:
    stream = requests.get(nbaStream).text
    s = BeautifulSoup(stream, 'lxml')
    php = s.find_all('iframe')[0]['src']
    nbaAbv = php.split('/')[4]
    prefix = 'jc'
    print('Fetching {} stream...'.format(nbaAbv))
    url = 'http://{}.crackstreams.ga/show/{}/{}'.format(prefix, nbaAbv, chunks)
    link = requests.get(url)
    m3u8_master = m3u8.loads(link.text)


    # 12 ts in each chunk, 4 sec for each ts = 48 sec before next fetch
    # with open("./Streams/{}Stream.ts".format(nbaAbv), 'wb') as f:
    #     for segment in m3u8_master.data['segments']:
    #         if segment['uri'] is None:
    #             break
    #         url = 'http://{}.crackstreams.ga/show/{}/'.format(prefix, nbaAbv) + segment['uri']
    #         r = requests.get(url)
    #         f.write(r.content)
    #         print('here')

