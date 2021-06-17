from nltk.corpus import opinion_lexicon
from nltk.corpus import wordnet
from pprint import pprint


def get_list_of_words_wordnet():
    return list(wordnet.words())


def get_list_of_word_positive():
    return opinion_lexicon.words('positive-words.txt')


def get_list_of_word_negative():
    return opinion_lexicon.words('negative-words.txt')


def get_intersection(first_set, second_set):
    if not isinstance(first_set, set) or not isinstance(second_set, set):
        raise ValueError
    else:
        return first_set.intersection(second_set)


def main():
    my_fileids = opinion_lexicon.fileids()
    print(my_fileids)
    my_words = opinion_lexicon.words('negative-words.txt')
    print(my_words)
    words_from_wordnet = set(get_list_of_words_wordnet())
    positive_words = set(get_list_of_word_positive())
    negative_words = set(get_list_of_word_negative())
    print(positive_words)
    #print(words_from_wordnet)
    #res = words_from_wordnet.intersection(positive_words)  # общие слова позитивные и ворднетовские
    res_positive = get_intersection(positive_words, words_from_wordnet)
    res_negative = get_intersection(negative_words, words_from_wordnet)
    res_test = get_intersection(positive_words, negative_words)
    print('Positive & Wordnet: ')
    pprint(res_positive)
    print('Negative & Wordnet: ')
    pprint(res_negative)
    print('Positive & Negative: ')
    pprint(res_test)



if __name__ == '__main__':
    main()