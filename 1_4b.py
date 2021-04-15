from nltk.book import *
from pprint import pprint


def lexical_diversity(my_text):  # 1_4b
    """
    len(text) - определяет лексемы.
    :return:
    """
    count_of_lexemes = len(my_text)  # количество лексем. Лексемы - не только слова, но и знаки пунктуации
    count_of_words = len(set(my_text))  # количество элементов (словоформ)
    lexical_diversity_result = count_of_words / count_of_lexemes
    return lexical_diversity_result


def get_texts():
    list_of_text = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
    return list_of_text


def best_diversity():
    list_of_texts = get_texts()
    list_of_result = [lexical_diversity(text) for text in list_of_texts]
    res = max(list_of_result)
    print(f'Best diversity has text number {list_of_result.index(res)}. Diversity is:  {res}')


def main():
    best_diversity()


if __name__ == '__main__':
    main()