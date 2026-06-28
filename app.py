"""This is the actual code of the conlang translator."""
from flask import Flask, render_template, request
from dictionary import Dictionary

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    """This is the main app code."""
    in_english = None
    output = ""
    if request.method == 'POST':
        print(request.form)
        if request.form.get("input"):
            in_english = request.form.get("input")
# All of the above is window dressing and then some interesting weird systematic code!
            words = in_english.split()
            target_language = request.form.get('conlang')
            if target_language == "verdurian":
                for word in words:
                    output += " " + into_verdurian(word)
            elif target_language == 'pig_latin':
                for word in words:
                    output += " " + into_pig_latin(word)
                output = "In Pig Latin it's " + output
        else:
            in_conlang = request.form.get("conlang_input")
            input_conlang = request.form.get('conlang')
            if input_conlang == 'verdurian':
                output = from_verdurian(in_conlang)
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
    text = text.split()
    verdurian_dictionary = get_english_to_verdurian_dictionary()
    verdurian_output = ""
    for word in text:
        starts_with_capital = word[0].isupper()
        ends_with_punctuation = word[-1] in punctuation
        if ends_with_punctuation:
            verdurian_word = get_verdurian_word(word[:-1], verdurian_dictionary)
        else:
            verdurian_word = get_verdurian_word(word, verdurian_dictionary)

        if not verdurian_word:
            return word
        verdurian_word = reassemble_word(
            starts_with_capital,
            ends_with_punctuation,
            verdurian_word,
            word
        )
        verdurian_output = verdurian_output + " " + verdurian_word
    return verdurian_output.lstrip()
def get_english_to_verdurian_dictionary():
    """Makes verdurian_dictionary available"""
    verdurian_dictionary = Dictionary(
        from_lang="english",
        to_lang="verdurian",
        corpus_path='verdurian_dictionary.txt'
    )

    return verdurian_dictionary
def get_verdurian_to_english_dictionary():
    """Makes verdurian_dictionary available"""
    verdurian_dictionary = Dictionary(
        from_lang="verdurian",
        to_lang="english",
        corpus_path='verdurian_dictionary.txt'
    )

    return verdurian_dictionary
def get_verdurian_word(text, verdurian_dictionary):
    """
    Docstring for get_verdurian_word
    
    :param starts_with_capital: boolean
    :param ends_with_punctuation: boolean
    :param text: string
    :param verdurian_dictionary: dictionary
    """
    normalized_word = text.lower()
    verdurian_word = verdurian_dictionary.lookup(normalized_word)

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
def from_verdurian(text):
    """
    Docstring for from_verdurian
    It goes from Verdurian into English.
    :param text: string
    """
    verdurian_dictionary = get_verdurian_to_english_dictionary()
    sentence = ""
    for word in text:
        starts_with_capital = word[0].isupper()
        ends_with_punctuation = word[-1] in punctuation
        if ends_with_punctuation:
            normalized_word = word[:-1].lower()
            english_word = verdurian_dictionary.lookup(normalized_word)
        else:
            normalized_word = word.lower()
            english_word = verdurian_dictionary.lookup(normalized_word)
        if not english_word:
            return word
        english_word = reassemble_word(
            starts_with_capital,
            ends_with_punctuation,
            english_word,
            word
        )
        sentence = sentence + " " + english_word
    return sentence.strip()
