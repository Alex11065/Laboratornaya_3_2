
def count_letters(main_str):             # TODO  Напишите функцию count_letters
    letters = {}
    lowercase_text = main_str.lower()
    for symbol in lowercase_text:
        if symbol.isalpha():
            if symbol in letters:
                letters[symbol] += 1
            else:
                letters[symbol] = 1
    return letters
def calculate_frequency(letters):         # TODO Напишите функцию calculate_frequency
    total_count = sum(letters.values())
    dict_ = {}
    for letter, count in letters.items():
        frequency = round(count / total_count, 2)
        dict_[letter] = frequency
    return dict_

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
letters = count_letters(main_str)
dict_ = calculate_frequency(letters)

for letter, frequency in dict_.items():
    print(f"{letter}: {frequency:.2f}")

# TODO Распечатайте в столбик букву и её частоту в тексте
