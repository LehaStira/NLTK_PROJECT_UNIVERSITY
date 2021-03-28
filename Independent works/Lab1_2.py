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
        list_of_worlds)  # Этот результат говорит нам, что фразы "the monstrous pictures" и "the true pictures" появляются в "Моби Дике".


def dispersion_plot_demonstration():  # 1_3b
    list_of_words = ['money', 'freedom', 'justice']
    text7.dispersion_plot(list_of_words)


def lexical_diversity_demonstration(my_text):  # 1_4b
    """
    len(text) - определяет лексемы.
    :return:
    """
    count_of_lexemes = len(my_text)  # количество лексем. Лексемы - не только слова, но и знаки пунктуации
    count_of_words = len(set(my_text))  # количество элементов (словоформ)
    lexical_diversity_result = count_of_words / count_of_lexemes
    return lexical_diversity_result


def freq_dist_demostration():  # 1.8
    fdist1 = FreqDist(text1)
    pprint(fdist1.most_common(30))  # с помощью функции most_common мы определили 30 популярных слов
    pprint(fdist1.pformat(2))  # конвертирует это в строку
    fdist1.plot(50)  # Строит графики
    # for i in fdist1.elements():
    #    print()
    #    print(i)


def lists_generation_demonstration():  # 1.9
    result = [i ** 2 for i in range(1, 100) if i % 10 == 5]
    return result


def collocation_demostration():  # 1.10
    text1.collocations()


def sorted_list_generation():  # 1.11
    first = sorted(w for w in set(text7) if '-' in w and 'index' in w)  # в списке словоформы из текста 7, только, если в них есть '-' и индекс
    second = sorted(wd for wd in set(text3) if wd.istitle() and len(wd) > 10) # в списке все словормы из текста 3, если выполняется istitle (если в строке прописные буквы идут после заглавных) и если длина словоформы меньше десяти
    third = sorted(w for w in set(sent7) if not w.islower())  # все строки из списка sent 7, если они не содержат только прописные буквы
    fourth = sorted(t for t in set(text2) if 'cie' in t or 'cei' in t) # все словоформы из текста 2, если в них содержится 'cie' или 'cei'
    return first, second, third, fourth


def main():
    # concordance_demonstration()
    # print('-----------------------')
    # similar_demostration()
    # print('-----------------------')
    # common_context_demonstration()
    # dispersion_plot_demonstration()
    # print(lexical_diversity_demonstration(text1))
    # freq_dist_demostration()
    # print(lists_generation_demonstration())
    pprint(sorted_list_generation())


if __name__ == '__main__':
    main()
