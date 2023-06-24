import urllib.request
import bs4

URL = 'https://www.gitasupersite.iitk.ac.in/srimad?language=dv&field_chapter_value='
URL1 = '&field_nsutra_value='
URL2 = '&etsiva=1&choose=1'


def Parse(val0, val1):
    Url = URL + str(val0) + URL1 + str(val1) + URL2
    chapter_shloka = str(val0) + '.' + str(val1)
    print(chapter_shloka)

    while True:
        try:
            # retrieve the content of a web page specified by the 'Url' variable
            html_content = urllib.request.urlopen(Url).read()
            break
        except Exception:
            pass

    # Convert the bytes data to string
    html_string = html_content.decode(errors="ignore")

    # Replace a substring in the HTML string
    html_content = html_string.replace('\r', '')
    if chapter_shloka not in html_content:
        return None, None

    soup = bs4.BeautifulSoup(html_content, 'html.parser')
    FONT = soup.findAll('font', {'size': '3px'})
    sanskrit_shloka = ''

    try:
        san = FONT[0].findAll(string=True)
        eng = FONT[1].findAll(string=True)
    except IndexError:
        return None, None

    print(san)
    print(eng)

    print("complete")


def get(chapter):
    Member = []
    count = 0
    for shloka in range(1, 2):
        Parse(chapter, shloka)


# for example: I have a two chapter
for chapters in range(1, 2):
    get(chapters)
