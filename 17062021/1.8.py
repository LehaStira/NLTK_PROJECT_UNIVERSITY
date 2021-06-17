from nltk import FreqDist
from pprint import pprint
from nltk.book import *


def freq_dist_demostration():  # 1.8
    fdist1 = FreqDist(text1)
    pprint(fdist1.most_common(30))  # с помощью функции most_common мы определили 30 популярных слов
    pprint(fdist1.pformat(2))  # конвертирует это в строку
    fdist1.plot(50)  # Строит графики
    # for i in fdist1.elements():
    #    print()
    #    print(i)

def main():
    freq_dist_demostration()

if __name__ == '__main__':
    main()