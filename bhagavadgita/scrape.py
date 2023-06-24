import urllib.request
import bs4

URL = 'https://www.gitasupersite.iitk.ac.in/srimad?language=dv&field_chapter_value='
URL1 = '&field_nsutra_value='
URL2 = '&etsiva=1&choose=1'


def isEng(san):
    return all(ord(char) < 128 for char in san)


def Parse(value1, value2):
    Url = URL + str(value1) + URL1 + str(value2) + URL2
    chapter_shloka = str(value1) + '.' + str(value2)

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

    try:
        sanX = FONT[0].findAll(string=True)
        engX = FONT[1].findAll(string=True)
    except IndexError:
        return None, None

    sanskrit_shloka = ''
    for i in sanX:
        if isEng(i):
            continue
        first = str(i.encode('utf8'))
        sanskrit_shloka += first + ' '

    english_shloka = ''
    try:
        for i in engX:
            english_shloka += str(i.encode('utf8'))
    except Exception:
        return None, None

    sanskrit_shloka = sanskrit_shloka.strip()
    sanskrit_shloka = sanskrit_shloka.strip(' ')
    sanskrit_shloka = sanskrit_shloka.strip('\n')

    english_shloka = english_shloka.strip()
    english_shloka = english_shloka.strip('\n')

    if english_shloka == '':
        return None, None

    return sanskrit_shloka, english_shloka


def get(chapter):
    Member = []
    count = 0
    for shloka in range(1, 10):
        sanskrit, english = Parse(chapter, shloka)

        print(sanskrit)
        print(english)

# for example: I have a two chapter
for chapters in range(1, 2):
    get(chapters)
