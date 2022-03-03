
import itertools
import csv
from urllib import response
import nltk
import string
nltk.download('stopwords')
from nltk.corpus import stopwords


movies_file = open('/Users/prasadshinde/Documents/My Repos/OOEngine/OOEngine/movies.csv', 'r', encoding='utf-8')
MOVIES_LIMIT = 10000
MOVIES_DATA = []
MOVIES_KWIC_DATA = {}
en_stops = set(stopwords.words('english'))


def read_from_csv():
    csvreader = csv.reader(movies_file)
    next(csvreader)
    next(csvreader)

    for row in itertools.islice(csvreader, MOVIES_LIMIT):
        row = [row[0], row[3]]
        MOVIES_DATA.append(row)
        keywords = remove_stop_words(row[0] + ' ' + row[1]).split()
        for keyword in keywords:
            keyword = keyword.lower()
            # print(keyword)
            # print(MOVIES_KWIC_DATA)
            # print(MOVIES_KWIC_DATA.get(keyword, []))
            if keyword not in MOVIES_KWIC_DATA:
                MOVIES_KWIC_DATA[keyword] = []
            MOVIES_KWIC_DATA[keyword].append(len(MOVIES_DATA) - 1)
            # if len(MOVIES_KWIC_DATA[keyword]) > 1:
            #     print(keyword)
            #     print(MOVIES_KWIC_DATA[keyword])
    
    # print(MOVIES_KWIC_DATA)
        


def remove_stop_words(query):
    query = query.translate(str.maketrans('', '', string.punctuation))
    query = query.split()
    res = []
    for word in query: 
        if word not in en_stops:
            res.append(word)
    return ' '.join(res)


def search(query):
    query = query.lower()
    query = remove_stop_words(query).split()
    resIndices = []
    for word in query:
        if word in MOVIES_KWIC_DATA:
            resIndices += MOVIES_KWIC_DATA[word]
    resIndices = set(resIndices)
    response = []
    for index in resIndices:
        response.append(MOVIES_DATA[index])
    
    return response


read_from_csv()
print(search("Twelve Outrageous guests"))
# print(remove_stop_words("Just When His World Is Back To Normal... He's In For The Surprise Of His Life!"))
