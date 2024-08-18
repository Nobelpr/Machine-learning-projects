import pandas as pd

# please imstall the latest version of with google translator using pip install googletrans==4.0.0-rc1


from googletrans import Translator 
data = pd.read_csv("./hindi.csv")
#print(data)


translator = Translator()
translations = {}
for column in data.columns:
    unique = data[column].unique()
    #print(unique)
    for element in unique:
        #print(element)
        translations[element] = translator.translate(element).text

for i in translations.items():
     print(i)


data.replace(translations, inplace=True)
print(data)