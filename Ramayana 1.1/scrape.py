import bs4
import urllib.request
import os
import dotenv

dotenv.load_dotenv()
# Data access through valmiki site
URL = os.getenv("URL1")
KANDA_URL = os.getenv("KANDA_URL1")
SARGAURL = os.getenv("SARGAURL1")
SLOKAURL = os.getenv("SLOKAURL1")


def parse(value1, value2, value3):
    url = URL + KANDA_URL + str(value1) + SARGAURL + str(value2) + SLOKAURL + str(value3)
    idy = str(value1) + '.' + str(value2) + '.' + str(value3)

    while True:
        try:
            # retrieve the content of a web page specified by the 'url' variable
            html_content = urllib.request.urlopen(url).read()
            break
        except ExceptionGroup:
            pass

    # Convert the bytes data to string
    html_string = html_content.decode(errors="ignore")

    # Replace a substring in the HTML string
    html_content = html_string.replace('\r', '')
    if idy not in html_content:
        return None, None, None

    soup = bs4.BeautifulSoup(html_content, 'html.parser')
    div = soup.findAll("div", {"class": "field-content"})

    try:
        shloka_x = div[0].findAll(string=True)
        translate_x = div[1].findAll(string=True)
        description_x = div[2].findAll(string=True)
    except IndexError:
        return None, None, None

    if value3 == 1:
        san_list = str(shloka_x).split("[")[2].split("]")[0].split(",")
        if len(san_list) == 3:
            eng = san_list[0]
            san = san_list[1] + "," + san_list[2]
            shloka = eng + " " + san
        else:
            eng = str(shloka_x).split("[")[2].split("]")[0]
            san_list = str(shloka_x).split("[")[2].split("]")[1].split(",")
            san = san_list[1] + "," + san_list[2]
            shloka = eng + " " + san
    else:
        shloka = str(shloka_x).split("[")[1].split("]")[0]

    translate = str(translate_x).split("[")[1].split("]")[0]
    description = str(description_x).split("[")[1].split("]")[0]
    return shloka, translate, description


def get(kanda, sarga, kanda_tid):
    shloka_member = []
    translate_member = []
    description_member = []
    for sarga_n in range(1, sarga):
        count = 0
        for sloka_n in range(1, 150):
            print("kanda: ", kanda, "=", kanda_tid, "sarga: ", sarga_n, " sloka_n: ", sloka_n, "****")
            shloka, translate, description = parse(kanda_tid, sarga_n, sloka_n)
            if shloka is None and translate is None and description is None:
                count += 1
                if count >= 5:
                    break
            else:
                count = 0
            if shloka in shloka_member and translate in translate_member and description in description_member:
                continue
            else:
                shloka_member.append(shloka)
                translate_member.append(translate)
                description_member.append(description)

            if len(shloka_member) >= 25 and len(translate_member) >= 25 and len(description_member) >= 25:
                shloka_member = shloka_member[1:]
                translate_member = translate_member[1:]
                description_member = description_member[1:]

            if shloka is not None and translate is not None and description is not None:
                count = 0
                with open(str(kanda_tid) + '_' + str(kanda) + '_shloka.txt', 'a+', encoding='utf-8') as file:
                    file.write(shloka + "\n\n")
                with open(str(kanda_tid) + '_' + str(kanda) + '_translate.txt', 'a+', encoding='utf-8') as file:
                    file.write(translate + '_' + "\n\n")
                with open(str(kanda_tid) + '_' + str(kanda) + '_description.txt', 'a+', encoding='utf-8') as file:
                    file.write(description + "\n\n")
                file.close()
            else:
                count += 1
                if count >= 20:
                    break
        print("****** \n ")


# Content: name(kanda), sarga, Sloka
Kandas = [('balakanda', 78, 1), ('ayodhyakanda', 120, 2), ('aranyakanda', 76, 3), ('kishkindakanda', 68, 4),
          ('sundarkanda', 69, 5), ('yuddhakanda', 132, 6)]

for kanda_no, sarga_no, kanda_id in Kandas:
    get(kanda_no, sarga_no, kanda_id)
