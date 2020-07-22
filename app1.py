import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn =  input("Did you mean %s instead? Enter Y if yes, or N if no  " % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn =="N":
            return "Word dosen't exist"
        else:
            return "Enter correct Choice"
    else:
        return "The word dosen't exist."

word = input("Enter Word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
