import urllib
import bs4

URL = 'https://www.gitasupersite.iitk.ac.in/srimad?language=dv&field_chapter_value='
URL1 = '&field_nsutra_value='
URL2 = '&etsiva=1&choose=1'

def Parse(val0, val1):
    Url = URL + str(val0) + URL1 + str(val1) + URL2
    print(Url)
    # retrieve the content of a web page specified by the 'Url' variable

def get(chapter):
    Member = []
    count = 0
    for shloka in range(1, 10):
        Parse(chapter, shloka)


# for example: I have a two chapter
for chapters in range(1, 3):
    print(chapters)
    get(chapters)