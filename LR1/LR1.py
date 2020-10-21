# Задача
# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# Оформите алгоритм в виде функции, которая принимает текст, а возвращает ответ.

# Ход работы
# Разобрать строку. Удалить лишние символы.
# Перекидать в словарь, где ключ - слово, а значение - его частота.
# Отсортировать словарь по значениям
# Вытащить ключи, добавить первый в итоговый список
# Если значение этого ключа совпадает с значением последующего, также добавить в список
# Отсортировать список по умолчанию (это лексикографический порядок), вернуть первое.

with open('text.txt', encoding="utf8") as file:
    text = file.read().lower()


def function(text):
    import re
    words = re.split(r'\W+', text)

    dict_words = {}

    for word in words:
        if(dict_words.get(word) == None):
            dict_words[word] = 1
        else:
            dict_words[word] = dict_words.get(word)+1

    sort_dict = dict(
        sorted(dict_words.items(), key=lambda item: item[1], reverse=True))

    list_keys = list(sort_dict)

    result_set = list()
    result_set.append(list_keys[0])

    value = sort_dict.get(result_set[0])

    del sort_dict[result_set[0]]

    for key in sort_dict:
        if(sort_dict.get(key) == value):
            result_set.append(key)
        else:
            break

    result_set.sort()

    return result_set[0]


print("Наиболее частое слово: '", function(text), "'")
