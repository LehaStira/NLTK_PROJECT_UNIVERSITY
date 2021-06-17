import nltk
from nltk.book import *
from nltk.corpus import gutenberg


def get_gutenberg_fileid():
    return gutenberg.fileids()


def get_text(name):
    corpus = nltk.corpus.gutenberg.words(name)  #  'shakespeare-hamlet.txt' 'austen-emma.txt'
    return nltk.Text(corpus)


def get_concordance(text, word):
    return text.concordance(word)


def main():
    word = 'fire'
    list_of_files = get_gutenberg_fileid()
    for files in list_of_files:
        print()
        my_text = get_text(files)
        res = get_concordance(my_text, word)
        print(res)
        print()

    #my_text = get_text('carroll-alice.txt')
    #res = get_concordance(my_text, word)
    #print(res)
    #print()



if __name__ == '__main__':
    main()