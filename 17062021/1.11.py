from nltk.book import *


def sorted_list_generation():  # 1.11
    first = sorted(w for w in set(text7) if '-' in w and 'index' in w)  # в списке словоформы из текста 7, только, если в них есть '-' и индекс
    second = sorted(wd for wd in set(text3) if wd.istitle() and len(wd) > 10) # в списке все словормы из текста 3, если выполняется istitle (если в строке прописные буквы идут после заглавных) и если длина словоформы меньше десяти
    third = sorted(w for w in set(sent7) if not w.islower())  # все строки из списка sent 7, если они не содержат только прописные буквы
    fourth = sorted(t for t in set(text2) if 'cie' in t or 'cei' in t) # все словоформы из текста 2, если в них содержится 'cie' или 'cei'
    return first, second, third, fourth


def main():
    first, second, third, fourth = sorted_list_generation()
    print(f'first = {first}')
    print(f'second = {second}')
    print(f'third = {third}')
    print(f'fourth = {fourth}')


if __name__ == '__main__':
    main()