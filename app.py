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
    verdurian_dictionary = get_verdurian_dictionary()
    starts_with_capital = text[0].isupper()
    ends_with_punctuation = text[-1] in punctuation
    verdurian_word = get_verdurian_word(
        starts_with_capital,
        ends_with_punctuation,
        text,
        verdurian_dictionary
    )

    if not verdurian_word:
        return text
    verdurian_word = reassemble_word(
        starts_with_capital,
        ends_with_punctuation,
        verdurian_word,
        text
    )
    return verdurian_word
def get_verdurian_dictionary():
    """Makes verdurian_dictionary available"""
    verdurian_dictionary = {}
    with open('verdurian_dictionary.txt', 'r', encoding="utf-8") as file:
        for line in file:
            array = line.strip().split(" - ")
            english_word = array[0][1:]
            if len(array) > 2:
                verdurian_word = array[2]
                verdurian_dictionary[english_word] = verdurian_word
    return verdurian_dictionary
def get_verdurian_word(starts_with_capital, ends_with_punctuation, text, verdurian_dictionary):
    """
    Docstring for get_verdurian_word
    
    :param starts_with_capital: boolean
    :param ends_with_punctuation: boolean
    :param text: string
    :param verdurian_dictionary: dictionary
    """
    verdurian_word = ""
    if starts_with_capital and ends_with_punctuation:
        verdurian_word = verdurian_dictionary.get(text[:-1].lower())
    elif starts_with_capital:
        verdurian_word = verdurian_dictionary.get(text.lower())
    elif ends_with_punctuation:
        verdurian_word = verdurian_dictionary.get(text[:-1])
    else:
        verdurian_word = verdurian_dictionary.get(text)

    return verdurian_word
def reassemble_word(starts_with_capital, ends_with_punctuation, verdurian_word, text):
    """
    Docstring for reassemble_word
    It reverses get_verdurian_word
    :param starts_with_capital: bool
    :param ends_with_punctuation: bool
    :param verdurian_word: str
    :param text: str
    """
    if starts_with_capital and ends_with_punctuation:
        verdurian_word = verdurian_word.capitalize() + text[-1]
    elif starts_with_capital:
        verdurian_word = verdurian_word.capitalize()
    elif ends_with_punctuation:
        verdurian_word += text[-1]

    return verdurian_word
