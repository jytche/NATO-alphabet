import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetic_word = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_word)


generate_phonetic()
