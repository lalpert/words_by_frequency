import collections
import sys

word_files = [10,20,35,40,50,55,60,70,80,95]
        
def file_to_set(filename):
    return set(line.strip() for line in open(filename, encoding = "ISO-8859-1"))

def categorize_word(word, word_dicts, word_ranks):
    for i in range(len(word_dicts)):
        d = word_dicts[i]
        if word in d:
            word_ranks[i].append(word)
            return
    print("Word not found: " + word)
    word_ranks[i+1].append(word)


def generate_dicts(word_files):
    word_sets = []
    for f in word_files:
        filename = "english_dictionaries/english-words." + str(f)
        words = file_to_set(filename)
        word_sets.append(words)
    return word_sets

def print_ranks(word_ranks):
    for i in range(len(word_ranks)):
        print("RANK " + str(i))
        print(word_ranks[i])
        print("\n")

def vocab_words():
    filename = "vocab.txt"
    return file_to_set(filename)

vocab_file = sys.argv[1]
word_ranks = collections.defaultdict(list)
word_sets = generate_dicts(word_files)
for word in file_to_set(vocab_file):
    categorize_word(word, word_sets, word_ranks)
print_ranks(word_ranks)
