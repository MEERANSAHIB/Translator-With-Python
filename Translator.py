# by this program i leared how dictionary works in python
print("Translator")
print("By Using This Program You Can Translate English Into Meeran's Language")
meeran_dict = {
    'a': 'l',
    'b': 'k',
    'd': 'p',
    'e': 'r',
    'h': 't',
    'i': 'm',
    'j': 'u',
    'v': 'z',
    'w': 'q',
    'x': 'f',
    'c': 'o',
    'y': 'z',
    'g': 's',
    'l': 'a',
    'k':'b',
    'p':'d',
    'r':'e',
    't':'h',
    'm':'i',
    'u':'j',
    'z':'v',
    'q':'w',
    'f':'x',
    'o':'c',
    'z':'y',
    's':'g'
}
def Translate(phrase):
    translatedtext = '' 
    for letter in phrase:
        translatedtext += meeran_dict.get(letter, letter)
    return translatedtext
n=int(input("Enter the number of time you want to execute this program"))
for i in range(0,n):
   input_phrase = input("Enter a phrase in lower case: ")
   final_output = Translate(input_phrase)
   print(final_output)
