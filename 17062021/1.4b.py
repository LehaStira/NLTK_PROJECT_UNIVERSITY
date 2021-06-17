from nltk.book import *


def lexical_diversity_demonstration(my_text):  # 1_4b
    """
    len(text) - определяет лексемы.
    :return:
    """
    count_of_lexemes = len(my_text)  # количество лексем. Лексемы - не только слова, но и знаки пунктуации
    count_of_words = len(set(my_text))  # количество элементов (словоформ)
    lexical_diversity_result = count_of_words / count_of_lexemes
    return lexical_diversity_result


def main():
    res = lexical_diversity_demonstration(text2)
    print(res)

if __name__ == '__main__':
    main()