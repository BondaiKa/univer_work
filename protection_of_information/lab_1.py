# 7
# P = 10^-6
# V = 20 pass/min
# T = 3 weeks,
# Integers and russian chars (lower)


# A = 43

# 10^-6 = (20 * 30240) / 43^L
# L = 8

# big_int = ((20 * 30240) / (10** (-6)))

# num = 43
# ten = 1
# while 1:
#     if num ** ten > big_int:
#         print(ten)
#         break
#     ten += 1

import random

russian_symbols = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к',
                   'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
                   'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


def generate_password(length_pass):
    password = []
    all_symbols = russian_symbols + [str(x) for x in range(10)]
    for x in range(length_pass):
        index = random.randint(0,len(all_symbols)-1)
        password.append(all_symbols[index])
    return ''.join(password)

for x in range(10):  
    print(generate_password(8))
