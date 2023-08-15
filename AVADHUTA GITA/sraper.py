import urllib.request
import bs4

URL = "https://www.gitasupersite.iitk.ac.in/minigita/avadhuta?language=dv"
CHAPTER_URL = "&field_chapter_value="
SLOKAURL = "&field_nsutra_value="


def Parse(chapterN, slokaN):
    URLPATH = f"{URL}{CHAPTER_URL}{chapterN}{SLOKAURL}{slokaN}"

    while (True):
        try:
            html = urllib.request.urlopen(URLPATH).read()
            break
        except ExceptionGroup:
            pass

    html = html.replace('\r', '')
    soup = bs4.BeautifulSoup(html)
    FONT = soup.findAll('font', {'size': '3px'})
    print(FONT)

    return 0


def get(chapter):
    Mem = []
    Count = 0
    for i in range(1, 5):
        san = Parse(chapter, i)


for chapter in range(1, 9):
    get(chapter)
