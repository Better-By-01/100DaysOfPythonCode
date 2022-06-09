import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter:row.code for (index, row) in df.iterrows()}

def generated_phonetic():
    word = input("Enter a word: ").upper()
    try:
        coded_word = [code_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabets")
        generated_phonetic()
    else:
        print(coded_word)

generated_phonetic()


# Enter a word: Ashutosh
# ['Alfa', 'Sierra', 'Hotel', 'Uniform', 'Tango', 'Oscar', 'Sierra', 'Hotel']

# Enter a word: ashutosh32
# Sorry, only letters in the alphabet