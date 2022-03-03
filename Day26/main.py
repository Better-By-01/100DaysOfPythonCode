import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter:row.code for (index, row) in df.iterrows()}
word = input("Enter a word: ").upper()
coded_word = [code_dict[letter] for letter in word]
print(coded_word)
# Enter a word: Ashutosh
# ['Alfa', 'Sierra', 'Hotel', 'Uniform', 'Tango', 'Oscar', 'Sierra', 'Hotel']