import urllib.request
import bs4

URL = "https://www.gitasupersite.iitk.ac.in/minigita/avadhuta?language=dv"
CHAPTER_URL = "&field_chapter_value="
SLOKAURL = "&field_nsutra_value="


def Parse(chapterN, slokaN):
    URLPATH = f"{URL}{CHAPTER_URL}{chapterN}{SLOKAURL}{slokaN}"

    while True:
        try:
            html_content = urllib.request.urlopen(URLPATH).read()
            break
        except ExceptionGroup:
            pass

    html_string = html_content.decode(errors="ignore")

    html_content = html_string.replace('\r', '')
    soup = bs4.BeautifulSoup(html_content, 'html.parser')
    FONT = soup.findAll('font', {'size': '3px'})

    try:
        input_strings = FONT[0].findAll(string=True)
    except IndexError:
        return None, None

    # Extract and process each string separately
    lines = []
    for input_string in input_strings:
        cleaned_line = input_string.strip().replace('\t', '    ')
        if cleaned_line:
            lines.append(cleaned_line)

    # Join the cleaned lines back into a single string
    sanX = ' '.join(lines)

    return sanX


def get(c):
    Mem = []
    count = 0
    for i in range(1, 35):
        san = Parse(c, i)

        if san is None:
            count += 1
            if count > 30:
                break
        else:
            count = 0

        if san in Mem:
            continue
        else:
            Mem.append(san)

        if san is not None:
            count = 0
            with open(str(chapter) + '_sanskrit.txt', 'a+', encoding='utf-8') as file:
                file.write(str(san) + '\n')


for chapter in range(4, 9):
    print(chapter)
    get(chapter)
