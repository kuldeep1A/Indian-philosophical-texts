import urllib.request
import bs4

URL = "https://www.valmiki.iitk.ac.in/content?language=dv"
KANDA_URL = "&field_kanda_tid="
SARGAURL = "&field_sarga_value="
SLOKAURL = "&field_sloka_value="


def isEng(san):
    return all(ord(char) < 128 for char in san)


def Parse(value1, value2, value3):
    Url = URL + KANDA_URL + str(value1) + SARGAURL + str(value2) + SLOKAURL + str(value3)
    idy = str(value1) + '.' + str(value2) + '.' + str(value3)

    while True:
        try:
            # retrieve the content of a web page specified by the 'Url' variable
            html_content = urllib.request.urlopen(Url).read()
            break
        except ExceptionGroup:
            pass

    # Convert the bytes data to string
    html_string = html_content.decode(errors="ignore")

    # Replace a substring in the HTML string
    html_content = html_string.replace('\r', '')
    if idy not in html_content:
        return None, None

    soup = bs4.BeautifulSoup(html_content, 'html.parser')
    DIV = soup.findAll("div", {"class": "field-content"})

    try:
        allX = DIV[0].findAll(string=True)
    except IndexError:
        return None, None

    sanskrit_shloka = ''
    for i in allX:
        if isEng(i):
            continue

        first = str(i.encode('utf-8'))
        for aa in range(-7, 8):
            for bb in range(-7, 8):
                first = first.replace(str(value1) + '.' + str(value2 + aa) + '.' + str(value3 + bb), '')
                first = first.replace(str(value1) + str(value2 + aa) + str(value3 + bb), '')

        first = first.replace('\xe0\xa5\xa4', '')  # |

        if i == allX[-1]:
            first += '\xe0\xa5\xa4\xe0\xa5\xa4'  # ||
        else:
            first += '\xe0\xa5\xa4'  # |

        sanskrit_shloka += first + ' '

    engX = DIV[2].findAll(string=True)
    english_shloka = ''
    try:
        for i in engX:
            english_shloka += str(i.encode('utf-8'))
    except ExceptionGroup:
        return None, None

    sanskrit_shloka = sanskrit_shloka.strip()
    sanskrit_shloka = sanskrit_shloka.strip(' ')
    sanskrit_shloka = sanskrit_shloka.strip('\n')
    english_shloka = english_shloka.strip()
    english_shloka = english_shloka.strip('\n')

    if english_shloka == '':
        return None, None

    return sanskrit_shloka, english_shloka


def get(kanda, sarga, kanda_tid):
    Member = []
    for sarga_n in range(1, sarga):
        count = 0
        for sloka_n in range(1, 2):
            sanskrit, english = Parse(kanda_tid, sarga_n, sloka_n)

            if sanskrit is None and english is None:
                count += 1
                if count >= 20:
                    break
            else:
                count = 0

            if (sanskrit, english) in Member:
                continue
            else:
                Member.append((sanskrit, english))

            if len(Member) >= 25:
                Member = Member[1:]

            print(sloka_n)
            if sanskrit is not None and english is not None:
                count = 0
                with open(str(kanda) + '_sanskrit.txt', 'a+', encoding='utf-8') as file:
                    file.write(sanskrit + '\n')
                with open(str(kanda) + '_english.txt', 'a+', encoding='utf-8') as file:
                    file.write(english + '\n')

                file.close()
            else:
                count += 1
                if count >= 20:
                    break


# Content: name(kanda), sarga, Sloka
Kandas = [('balakanda', 78, 1), ('ayodhyakanda', 120, 2), ('aranyakanda', 76, 3), ('kishkindakanda', 68, 4),
          ('sundarkanda', 69, 5), ('yuddhakanda', 132, 6)]

# Example
# Kandas = [('balakanda', 2, 1), ('ayodhyakanda', 2, 2), ('aranyakanda', 2, 3), ('kishkindakanda', 2, 4),
#           ('sundarkanda', 2, 5), ('yuddhakanda', 2, 6)]


for kanda_no, sarga_no, kanda_id in Kandas:
    get(kanda_no, sarga_no, kanda_id)
