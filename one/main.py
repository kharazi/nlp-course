import sys
import random
import nltk
from sets import Set
from nltk.stem.porter import PorterStemmer
from nltk.util import ngrams
# from nltk.collections import BigramCollocationFinder, TrigramAssocMeasures, \
    # BigramCollocationFinder


# Open and read corpus
text_corpus = open('data.txt').read()

# Basic initialization and instansate
tokens = nltk.word_tokenize(text_corpus)
tokens = [w.lower() for w in tokens]  # Basic normalization
stemmer = PorterStemmer()

# Part 1
tokens_len = len(tokens)
unique_tokens_len = len(Set(tokens))

if sys.argv[1] == "q1":
    print "|V| = %d, N = %d, N ^ (1/2) = %f" % (
        unique_tokens_len, tokens_len, tokens_len ** (1.0/2.0)
    )

# Part 2
stemmed = [stemmer.stem(t) for t in tokens]
unique_stems = Set(stemmed)

if sys.argv[1] == "q2":
    print "unique stems = %d\nlist = %s " % (
        len(unique_stems), ", ".join(unique_stems))


# Part 3
def generate(starting_point='i', crp=nltk.corpus.brown, ngram=2):
    words = nltk.corpus.brown.words(categories='news')

    ngrams = nltk.ngrams([w.lower() for w in words], ngram)

    cdf = nltk.ConditionalFreqDist(ngrams)
    # print cdf.viewitems(
    # for item in cdf.viewitems():
        # print item
    word = starting_point.lower()
    result = [word]

    while word not in [".", "?", "!", "'", ";", "`", "``"]:
        prev_word = result[-1]

        for new_word in cdf[word]:
            if new_word not in result[-len(result) / 2:]:
                prev_phrase = [prev_word, new_word]
                if not ' '.join(prev_phrase) in ' '.join(result):
                    word = new_word

        if word == result[-1]:
            break
        result.append(word)

    result = ' '.join(result)
    return result

if sys.argv[1] == "q3":
    # Bigram models
    print ">>> generate('i')"
    print generate('i')
    print ">>> generate('my')"
    print generate('my')
    print ">>> generate('why')"
    print generate('why')
    # Trigram models