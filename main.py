from requests_html import HTMLSession, HTMLResponse
import requests
import urllib.request
import time


start_episode = int(input("What episode to start with?\n"))
number_of_episodes = int(input("Number of episodes to download\n"))

for i in range(1,number_of_episodes+1):
    session = HTMLSession() #Not sure why but if I don't create a new session every time, it crashes after a few downloads     
    try:
        i = str(i)
        url = "http://www.hellointernet.fm/podcast/" + i
        source = session.get(url).html
        source.render()
        
        print("Getting Title")
        title = source.find(".entry-title", first=True).find('a', first=True).text
        print("Title: ", title)

        print("Getting download url")
        downloadUrl = source.find(".download", first=True).find('a',first=True).attrs['href']
        print("Downloading from", downloadUrl)
        filename = "Episode " + i + ".mp3"
        episode = urllib.request.urlretrieve(downloadUrl, filename= "./episodes/" + filename)
        print("File ", filename, "downloaded")
    except:
        print("Error")
    finally:
        session.close()
