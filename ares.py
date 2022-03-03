# REQUIREMENTS

from pyfade import Fade, Colors
from pycenter import center
from requests import get

from os import system, mkdir, name
from os.path import isdir
from base64 import b64decode as bd


def clear():
    system("cls" if name == 'nt' else "clear")


clear()

if name == 'nt':
    system("title Ares")
    system("mode 160, 50")

class Col:
    colors = {"red" : "\033[38;2;255;0;0m", 
              "orange" : "\033[38;2;255;100;0m", 
              "yellow" : "\033[38;2;255;255;0m",
              "white" : "\033[38;2;255;255;255m"}

    red = colors['red']

    orange = colors['orange']

    yellow = colors['yellow']
    
    white = colors['white']


pantheon = """
                       §§§§§§§§§@                                                         
                 §§§§§§§§§§§§§§§§§§                                                       
               §§             §§§§§                                                       
             §§             §§§§§§§                                                       
            §§             §§§@§§§§                                                       
           §§             §§§ §§§§                                                        
          §§§            §§§  §§§§                                                        
         %§§§           §§§   §§§§             §§§      §§§§§      §§§§§§§      §§§§§§§§§§
         §§§*          §§§    §§§§           § §§§    §§        §§     §§§    §§       §  
         §            §§§     §§§§         @  §§§    §         §§     §§§    §§!          
                     §§§      §§§§            §§§   §        §§§     §§     §§§§          
                    §§§       §§§§            §§§  §        §§§    §§        §§§§         
                   §§§§§§§§§§§§§§§           §§§§ §        §§§§  §§           §§§§§       
                  §§          *§§§           §§§ §         §§§&§            §   §§§§§     
                §§§            §§§           §§§§         §§§§             §     §§§§§    
               §§§             §§§§         §§§§§         §§§§           §         §§§§   
              §§§              §§§§         §§§§          §§§§         §$           §§§   
             §§                §§§§         §§§*           §§§§      §§             §§    
           §§                  §§§§§    §: #§§§            §§§§§   §§              §      
  §§§§§§§§§                     §§§§§§§    §§§              #§§§§§§      §§§§§§§§§        
 $$$*                             §§       :                   §           %%             

"""

author = "   - - - {} - - -".format(bd("Tnlha3UjMDAwMQ==").decode('utf-8'))

print(Fade.Vertical(Colors.blue_to_purple, center(pantheon)))
print(Fade.Horizontal(Colors.blue_to_purple, center(author)))


print()

print(Col.white+center("   Ares - The fastest YouTube video downloader.")+Col.white)

print("\n\n")

video_url = input(Col.white+"Video url > "+Col.white)
video_id = video_url.split("watch?v=")[-1]
video_id = video_id.split("&")[0]

print()

def get_title(id) -> str:
    verify_url = "https://www.youtube.com/oembed?format=json&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D" + id
    response = get(verify_url)
    if response.status_code == 400:
        return False
    json = response.json()
    return json["title"]


video_title = get_title(video_id)

if not video_title:
    input(Col.white+"Invalid URL!"+Col.white)
    exit()

else:
    print(Col.white+"Video title: "+Col.white+video_title)

print()

mode = input(Col.white+"1: MP3 - 2: MP4 > "+Col.white)

print()

if mode == '1':
    download_url = "https://www.yt-download.org/api/button/mp3/"
elif mode == '2':
    download_url = "https://www.yt-download.org/api/button/videos/"
else:
    input(Col.red+"Invalid mode!"+Col.white)
    exit()


download_url += video_id

print(Col.white+"Getting download link...\n"+Col.white)

response = get(download_url).text
response = response.split('"')
textures = list(reversed([link for link in response if video_id in link]))

if mode == '1':
    quality = input(Col.white+"1: 128kbps - 2: 192kbps - 3: 256kbps - 4: 320kbps > "+Col.white)
elif mode == '2':
    if len(textures) == 1:
        quality = input(Col.white+"1: 360p > "+Col.white)
    else:
        quality = input(Col.white+"1: 360p - 2: 720p > "+Col.white)

print()

try:
    quality = int(quality)
except ValueError:
    input(Col.red+"Please enter an integer!"+Col.white)
    exit()


if quality > len(textures):
    input(Col.red+"Invalid choice!"+Col.white)
    exit()


download_url = textures[quality-1]

print(Col.white+"Downloading...\n\n"+Col.white)

content = get(download_url).content



if not isdir("Downloads"):
    mkdir("Downloads")


if mode == '1':
    file = ".mp3"
elif mode == '2':
    file = ".mp4"


for char in ('\\', '/', ':', '*', '?', '"', '<', '>', '|'):
    video_title = video_title.replace(char, '')

path = "Downloads/" + video_title + file

with open(path, 'wb') as f:
    f.write(content)


input(Col.white+"Downloaded!"+Col.white)
