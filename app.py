"""This is the actual code of the conlang translator."""
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    """This is the main app code."""
    in_english = None
    output = ""
    if request.method == 'POST':
        print(request.form)
        in_english = request.form.get("input")
# All of the above is window dressing and then some interesting weird systematic code!
        words = in_english.split()
        target_language = request.form.get('conlang')
        if target_language == "verdurian":
            for word in words:
                output += " " + into_verdurian(word)
            output = "In Verdurian it's " + output
        elif target_language == 'pig_latin':
            for word in words:
                output += " " + into_pig_latin(word)
            output = "In Pig Latin it's " + output
        else:
            print("I... don't think that you bothered to use the website, you just broke the code!")
    return render_template('index.html', result=output, input=in_english) # Send it
# Aand... done.
punctuation = [".", ",", "!", "?"]
def into_pig_latin(text): # Supplementary functions
    """And this goes the other way."""
    # Get first letter and check if it is capitalized
    # If so, set starts_with_capital? to True
    # if not, set starts_with_capital? to False and made a major refactor
    starts_with_capital = text[0].isupper()
    last_letter = text[-1:]
    output = text
    if last_letter in punctuation:
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
def into_verdurian(text):
    """
    Docstring for into_verdurian
    It translates into Verdurian, an ACTUAL conlang, from English.
    :param text: It lets you pass in English text to translate into Verdurian.
    """
    starts_with_capital = text[0].isupper()
    verdurian_dictionary = {}
    with open('verdurian_dictionary.txt', 'r', encoding="utf-8") as file:
        for line in file:
            array = line.strip().split(" - ")
            english_word = array[0][1:]
            if len(array) > 2:
                verdurian_word = array[2]
                verdurian_dictionary[english_word] = verdurian_word
    last_letter = text[-1]
    if last_letter in punctuation:
        stripped_text = text[:-1]
        verdurian_word = verdurian_dictionary.get(stripped_text.lower())
        if verdurian_word:
            if starts_with_capital:
                return verdurian_dictionary[stripped_text.lower()].capitalize() + last_letter
            return verdurian_dictionary[stripped_text] + last_letter
    verdurian_word = verdurian_dictionary.get(text.lower())
    if verdurian_word:
        if starts_with_capital:
            return verdurian_dictionary[text.lower()].capitalize()
        return verdurian_dictionary[text]
    return text
