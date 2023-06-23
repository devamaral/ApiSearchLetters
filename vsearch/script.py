# frutas = {};

# while True:
#     fruta = input('Digite o nome de uma fruta ou "sair": ');

#     if fruta != 'sair':
#         if fruta in frutas:
#             frutas[fruta] += 1
#         else:
#             frutas[fruta] = 1
#     else:
#         break

# print(frutas)

# frutas = {};

# while True:
#     fruta = input('Digite o nome de uma fruta ou "sair": ');
#     if fruta != 'sair':

#         frutas.setdefault(fruta, 0);
#         frutas[fruta] += 1;
#     else:
#         break;

# setNumbers = {1, 2 , 3, 4, 4, 1, 2, 5};

# print(setNumbers);
# print(type(setNumbers));

# setNumber = {1, 2, 3, 4, 5};
# setNumber2 = {1, 2, 6, 4, 5};

# # print(2 in setNumber);
# print(setNumber.intersection(setNumber, setNumber2));
# print('Oi');

def search4vowels(phrase: str) -> set:
    """ Retorna quaisquer vogais encontradas em uma frase fornecida """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """ Rertorna quaisquer letras encontradas de uma frase fornecida """
    return set(letters).intersection(set(phrase))
