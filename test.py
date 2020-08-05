import sys
import shutil

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
  url = "http://nba-streams.xyz/stream/miami-heat-live-stream/"
  r = requests.get(url)
  doc = BeautifulSoup(r.text, "lxml")

  iframe = doc("iframe")
  if len(iframe) == 0:
    sys.exit()

  phpURL = iframe[0]["src"]
  team = phpURL.split("/")[-2]

  baseVidURL = "http://kc.crackstreams.ga/show"
  playlistM3U8 = "{}/{}/playlist.m3u8".format(baseVidURL, team)
  chunksM3U8 = "{}/{}/chunks.m3u8".format(baseVidURL, team)

  # TODO: figure out how to keep following the m3u8s

  r = requests.get(chunksM3U8)
  print(r.text)
