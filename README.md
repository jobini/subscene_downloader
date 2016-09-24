<h1><b>Subscene downloader</b></h1>

<h2><b>Synopsis</b></h2>

This is a Python script that, given a path containing movie folders, recursively downloads a positively/neutrally rated English subtitle file from [Subscene](http://www.subscene.com), for every movie that doesn't already have one.

<h2><b>Requirements</b></h2>

1. Python version 2.7.6+
2. [requests](https://pypi.python.org/pypi/requests)
3. [beautifulSoup4](https://pypi.python.org/pypi/beautifulsoup4)
4. [clint](https://pypi.python.org/pypi/clint)

<h2><b>Usage</b></h2>

First, set the path which contains the movie folders, by setting the `path` variable in `subscene_downloader.py`, using a text editor. Then, to run the script, simply run `python subscene_downloader.py` in the Terminal, from the directory of the extracted files. The subtitle file is downloaded to each corresponding movie folder. 

If no positively/neutrally rated subtitle is found for a particular movie, a message is printed saying so, and the script moves on to the next movie. 

Once subtitles for all the movies are downloaded, the script ends with a message saying so. 

<h2><b>To add</b></h2>

1. Download subtitles for movies that are not in individual movie folders - DONE
2. Add support for subtitles in other languages

<h2><b>License</b></h2>

Please view LICENSE for details on the usage of code in this repository.
