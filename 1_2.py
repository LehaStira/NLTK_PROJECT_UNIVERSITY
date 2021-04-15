from nltk.book import *
from pprint import pprint


def concordance_demonstration():
    text1.concordance('pleasure')


def similar_demostration():
    text1.similar('pleasure')


def common_context_demonstration():  # 1_2
    """
    Показывает, когда использование списка слов разделяет одни и те же окружающие слова.
    :return:
    """
    list_of_worlds = ['monstrous', 'true']
    text1.common_contexts(
        list_of_worlds)


def main():
    common_context_demonstration()


if __name__ == '__main__':
    main()