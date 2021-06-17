from nltk.corpus import indian
from deep_translator import GoogleTranslator
from pprint import pprint


def get_list_of_sentences():
    sentences = indian.sents('bangla.pos')
    return sentences

my_path = 'russian_indian.txt'

def get_russian(sent):
    print(f'Starting translate sentence {sent}')
    russian = GoogleTranslator(target='ru').translate(sent)
    print(f'Translating is over. Translated sentence is {russian}')
    write_to_file(my_path, russian)
    return russian


def get_list_of_strings(sentences):
    """
    :param sentences: list of sentences (sentences is lis also)
    :return:  list of sentences (sentences is string)
    """
    print('Getting list of string')
    res = list()
    for i in sentences:
        res.append(' '.join(i))
    print(f'Ending of get list of string = {res}')
    return res


def get_translated_list(list_of_sentences, language):
    print(f'Begining getting translated list')
    res = list()
    if language == 'ru':
        print('Language is ru')
        for i in list_of_sentences:
            print(f'Sentence is {i}')
            tmp = get_russian(i)
            res.append(tmp)
    return res


def write_to_file(path, data):
    try:
        with open(path, 'a') as f:
            f.write(data)
            f.write('\n')
    except Exception:
        pass


def main():
    raw_sentences = get_list_of_sentences()
    pprint(raw_sentences)
    my_sentences = get_list_of_strings(raw_sentences)
    #print(my_sentences)
    russian_sentences = get_translated_list(my_sentences, 'ru')
    print(russian_sentences)
    print('We gat all sentences')
    print('Begining of writing file')
    print('Ending of writing to file')


if __name__ == '__main__':
    main()
