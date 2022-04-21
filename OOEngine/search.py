
import itertools
import csv
import string
from pathlib import Path
from OOEngine import database

STOP_WORDS = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "but", "if", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "and", "or", "not"}

base_path = Path(__file__).parent
csv_path = (base_path / "movies_new_dataset.csv").resolve()
movies_file = open(csv_path, 'r', encoding='utf-8')

MOVIES_LIMIT = 45000
db = database.Database()


# Call this from wherever DB is being setup
def read_from_csv():
    # ***CSV structure***
    # imdb_id, original_title, overview, tagline
    csv_reader = csv.reader(movies_file)
    next(csv_reader)

    movies_data_list = []
    movies_kw_data = {}
    for row in itertools.islice(csv_reader, MOVIES_LIMIT):
        movies_data_list.append(row)
        keywords = list(set(remove_stop_words(row[1] + ' ' + row[3]).split()))

        for keyword in keywords:
            if keyword not in movies_kw_data:
                movies_kw_data[keyword] = []
            movies_kw_data[keyword].append(len(movies_data_list) - 1)

    db.insert(movies_data_list, movies_kw_data)


def remove_stop_words(query):
    query = query.translate(str.maketrans('', '', string.punctuation))
    query = query.split()
    res = []

    for word in query: 
        if word in {"AND", "OR", "NOT"} or word.lower() not in STOP_WORDS:
            res.append(word)
    return ' '.join(res)


# Method to search as well as autofill
# Returns list of [imdbid, title, overview, tagline]
def search(query):
    query = remove_stop_words(query)
    result = db.get_data(query)
    return result


read_from_csv()
# print(search("Love OR Part"))
# print(remove_stop_words("Just When His World Is Back To Normal... He's In For The Surprise Of His Life!"))
