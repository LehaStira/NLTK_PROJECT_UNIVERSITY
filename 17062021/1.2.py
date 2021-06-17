from nltk.book import *


def common_context_demonstration():  # 1_2
    """
    Показывает, когда использование списка слов разделяет одни и те же окружающие слова.
    :return:
    """
    list_of_worlds = ['monstrous', 'true']
    text1.common_contexts(
        list_of_worlds)  # Этот результат говорит нам, что фразы "the monstrous pictures" и "the true pictures" появляются в "Моби Дике".


def main():
    common_context_demonstration()


if __name__ == '__main__':
    main()