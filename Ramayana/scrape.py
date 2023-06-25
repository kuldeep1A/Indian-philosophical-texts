import urllib
import bs4

URL = "https://www.valmiki.iitk.ac.in/content?language=dv"
KANDA_URL = "&field_kanda_tid="
SARGAURL = "&field_sarga_value="
SLOKAURL = "&field_sloka_value="


def Parse(value1, value2, value3):
    Url = URL + KANDA_URL + str(value1) + SARGAURL + str(value2) + SLOKAURL + str(value3)
    idy = str(value1) + '.' + str(value2) + '.' + str(value3)

    while True:
        try:
            # retrieve the content of a web page specified by the 'Url' variable
            html_content = urllib.request.openurl(Url).read()
            break
        except ExceptionGroup:
            pass

    html_strign = html_content.decode()


def get(kanda, sarga, kanda_tid):
    Member = []
    for sarga_n in range(1, sarga):
        count = 0
        for sloka_n in range(1, 3):
            # sanskrit, english = Parse(kanda_tid, sarga_n, sloka_n)
            Parse(kanda_tid, sarga_n, sloka_n)





# Content: name(kanda), sarga, Sloka
# Kandas = [('balakanda', 78, 1), ('ayodhyakanda', 120, 2), ('aranyakanda', 76, 3), ('kishkindakanda', 68, 4),
#           ('sundarkanda', 69, 5), ('yuddhakanda', 132, 6)]

# Example
Kandas = [('balakanda', 2, 1), ('ayodhyakanda', 2, 2), ('aranyakanda', 2, 3), ('kishkindakanda', 2, 4),
          ('sundarkanda', 2, 5), ('yuddhakanda', 2, 6)]


for kanda_no, sarga_no, kanda_id in Kandas:
    get(kanda_no, sarga_no, kanda_id)
