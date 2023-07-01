import os

works = [{
    'originalTitle': "भगवद्गीता",
    'englishTitle': "Bhagavad Gita",
    'author': "Not available",
    'dirname': "bhagavadgita",
    'source': 'source',
    'sourceLink': 'sourceLink',
    'language': 'sanskrit',
    'text': {},
}, {
    'originalTitle': "ब्रह्म सूत्र",
    'englishTitle': "Brahma Sutras",
    'author': "Not available",
    'dirname': "brahmasutra",
    'source': 'source',
    'sourceLink': 'sourceLink',
    'language': 'sanskrit',
    'text': {},
}, {
    'originalTitle': "रामायणम्",
    'englishTitle': "Ramayana",
    'author': "Not available",
    'dirname': "ramayana",
    'source': 'source',
    'sourceLink': 'sourceLink',
    'language': 'sanskr	it',
    'text': {},
}, {
    'originalTitle': "श्रीरामचरितमानस",
    'englishTitle': "Ramcharitmanas",
    'author': "Not available",
    'dirname': "ramcharitmanas",
    'source': 'source',
    'sourceLink': 'sourceLink',
    'language': 'sanskrit',
    'text': {},
}, {
    'originalTitle': "Yoga Sūtras of Patañjali",
    'englishTitle': "Yoga Sūtras of Patañjali",
    'author': "Not available",
    'dirname': "yogasutra",
    'source': 'source',
    'sourceLink': 'sourceLink',
    'language': 'sanskrit',
    'text': {},
}]


def main():
    # nahi hai to bana dega
    if not os.path.exists('jk_json'):
        os.makedirs('jk_json')

    # Build json docs from txt files
    for root, dirs, files in os.walk('.'):
        path = root.split('/')
        print(os.path.basename(root))
        # print((len(path) - 1) * '---', os.path.basename(root))

        for fname in files:
            if fname.endswith('.txt'):
                print((len(path)) * '---', fname)

                for work in works:
                    if path[1] == work['dirname']:
                        if work['dirname'] == 'bhagavadgita':
                            chapter = int(fname.replace('chapter_', '').replace('_sanskrit.txt', '')) - 1
                            text = fileToLines(root, fname)


if __name__ == '__main__':
    main()
