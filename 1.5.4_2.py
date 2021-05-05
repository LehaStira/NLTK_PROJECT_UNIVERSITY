from nltk.book import *
from deep_translator import GoogleTranslator


def get_lexical_diversity(my_text):
    count_of_lexemes = len(my_text)  # количество лексем. Лексемы - не только слова, но и знаки пунктуации
    count_of_words = len(set(my_text))  # количество элементов (словоформ)
    lexical_diversity_result = count_of_words / count_of_lexemes
    return lexical_diversity_result


def get_russian(my_text):
    russian = GoogleTranslator(target='ru').translate(my_text)
    return russian


def get_english(my_text):
    english = GoogleTranslator(target='en').translate(my_text)
    return english


def main():
    my_text = ' '.join(text1[0:200])
    lexical_diversity_eng = get_lexical_diversity(my_text)
    russian_text = get_russian(my_text)
    lexical_diversity_ru = get_lexical_diversity(russian_text)
    print(f'English = {lexical_diversity_eng}')
    print(f'Russian = {lexical_diversity_ru}')
    english_again = get_english(russian_text)
    second_english_lexical = get_lexical_diversity(english_again)
    second_russian = get_russian(english_again)
    second_russian_lexical = get_lexical_diversity(second_russian)
    print(f'Lexical diversity of second russian translate = {second_russian_lexical}')
    print(f'Lexical diversity of second english translate = {second_english_lexical}')
    third_english = get_english(second_russian)


if __name__ == '__main__':
    main()