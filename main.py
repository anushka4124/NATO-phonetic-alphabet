import pandas as pd
df=pd.read_csv("nato_phonetic_alphabet.csv")
d={row["letter"]:row["code"] for (index,row) in df.iterrows()}
user_word=input("Enter a word: ").upper()
phone_lst=[d[letter] for letter in user_word if letter in d]
print(phone_lst)


