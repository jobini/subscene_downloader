import os
import requests
from bs4 import BeautifulSoup
from clint.textui import progress
import shutil
import subprocess
import operator

path = "/media/jobsism10/2E381BD3381B9943/Downloads/Video/Movies/"

moviefolders = os.listdir(path)
is_file = False

for folder in moviefolders:
    try:
        files = os.listdir(path+folder)
    except OSError:
        is_file = True
        os.mkdir(path+folder[0:-4])
        shutil.move(path+folder,path+folder[0:-4])
        files = os.listdir(path+folder[0:-4])

    is_srt = False
    movie_name = ""

    for item in files:
        if item[-3:] == 'srt':
            is_srt = True
            break

    if not is_srt:
        size_dict = {}
        for item in files:
            if is_file:
                size_dict[item] = os.path.getsize(path+folder[0:-4]+'/'+item)
            else:
                size_dict[item] = os.path.getsize(path+folder+'/'+item)

        ordered_dict = sorted(size_dict.items(),key = operator.itemgetter(1),reverse = True)
        movie_name = ordered_dict[0][0][0:-3]

        response = requests.get('https://subscene.com/subtitles/release?q={0}'.format(movie_name))
        soup = BeautifulSoup(response.text,"lxml")
        soup.prettify()

        tdlist = soup.find_all('td',class_ = 'a1')
        for i in tdlist:
            soup2 = BeautifulSoup(str(i.contents[1]),"lxml")
            soup2.prettify()
            link = soup2.find("a")
            url = 'https://subscene.com' + link.get("href")
            rating = soup2.find("span")
            rating = rating.attrs["class"][2]
            goodsrt = False

            if url.split("/")[-2] == 'english' and (rating == 'positive-icon' or rating == 'neutral-icon'):
                response2 = requests.get(url)
                soup3 = BeautifulSoup(response2.text,"lxml")
                soup3.prettify()
                dlink = soup3.find("a",id = "downloadButton")
                durl = 'https://subscene.com' + dlink.get("href")

                response3 = requests.get(durl,stream = True)
                total_size = int(response3.headers.get('content-length'))

                with open('sub.zip','wb') as f:
                    print "Downloading subtitles for '{0}'...".format(movie_name)
                    for data in progress.bar(response3.iter_content(chunk_size=128),\
                    expected_size = total_size/128 + 1):
                        f.write(data)

                subprocess.check_output(['unzip','sub.zip'])
                os.remove('sub.zip')
                srtfile = [item for item in os.listdir(os.getcwd()) if item[-3:] == 'srt']
                srtfile = srtfile[0]
                os.rename(srtfile,movie_name + 'srt')
                srtfile = movie_name + 'srt'
                if is_file:
                    shutil.move(srtfile,path+folder[0:-4])
                    break
                else:
                    shutil.move(srtfile,path+folder)
                    break
            print "Sorry, no [good] subtitles were found for {0}".format(movie_name)

print "Subtitles for all movies downloaded!"
