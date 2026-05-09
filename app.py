from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    in_english = None
    output = ""
    in_pig_latin = None
    if request.method == 'POST':
        print(request.form)
        input_language = request.form.get('submit-input')
        if input_language == "english":
            in_english = request.form.get("input")
# All of the above is window dressing and then some interesting weird systematic code!
            words = in_english.split()
            for word in words:
                output = output + " " + into_pig_latin(word)       
        elif input_language == 'pig-latin':
            in_pig_latin = request.form.get('input')
            output = into_english(in_pig_latin)
        else:
            print("Wait a minute minute...")
    return render_template('index.html', result=output, input=in_english) # Send it
# Aand... done.
def into_english(text):
    last_letter = text[-1:]
    output = text
    if last_letter in [",", ".", "!", "?"]:
        text = text[:-1]
        output = into_english(text)
        print("Output: " + output + " And the last letter is: " + last_letter + " .")
        output = output + last_letter
        return output
    if text[-2:] == 'ay':
        output = text[:-2]
        last_letter = output[-1:]
        output = output[:-1]
        if not last_letter == "w":
            output = last_letter + output
            return output
        else:
            print("Oh no, it's a bit tricky so PLEASE don't use this or anything? haha --- NEED HUMAN CONFIRMATION")
    else:
        print("Wait a minute")
    return output
def into_pig_latin(text): # Supplementary functions
    # Get first letter and check if it is capitalized
    # If so, set starts_with_capital? to True
    # if not, set starts_with_capital? to False
    starts_with_capital = text[0].isupper()
    last_letter = text[-1:]
    output = text
    if last_letter in [",", ".", "!", "?"]:
        text = text[:-1]
        output = into_pig_latin(text)
        print("Output: " + output + " And the last letter is: " + last_letter + " .")
        output = output + last_letter
        return output
    consonant_cluster = ""
    vowel_position = 0
    for index, letter in enumerate(text, start=0):
        if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            vowel_position = index
            break
        else:
            consonant_cluster = consonant_cluster + letter
    if text[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]: # the vowels
        output = output + "way"
    else:
        output = output[vowel_position:] + consonant_cluster + "ay" # it uses first_letter
    # Check if starts_with_capital? is true
    # If so, capitalize our new first letter
    # If not, lower case our new first letter
    if starts_with_capital:
        output = output.capitalize() # Uppercase
    return output