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
            words = in_english.split()
# All of the above is window dressing and then some interesting weird systematic code!
            target_language = request.form.get('conlang')
            if target_language == "verdurian":
                for word in words:
                    output += " " + into_verdurian(word)
            elif target_language == 'esperanto':
                for word in words:
                    output = into_esperanto(word)
        else:
            in_conlang = request.form.get("conlang_input")
            input_conlang = request.form.get('conlang')
            from_verdurian(in_conlang)
            words = in_conlang.split()
            if input_conlang == 'verdurian':
                for word in words:
                    output += " " + from_verdurian(word)
    return render_template('index.html', result=output, input=in_english) # Send it
# Aand... done.
punctuation = [".", ",", "!", "?"]
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
def reassemble_word(starts_with_capital, ends_with_punctuation, output_word, text):
    """
    Docstring for reassemble_word
    It reverses get_verdurian_word
    :param starts_with_capital: bool
    :param ends_with_punctuation: bool
    :param verdurian_word: str
    :param text: str
    """
    if starts_with_capital and ends_with_punctuation:
        output_word = output_word.capitalize() + text[-1]
    elif starts_with_capital:
        output_word = output_word.capitalize()
    elif ends_with_punctuation:
        output_word += text[-1]

    return output_word
def from_verdurian(word):
    """
    Docstring for from_verdurian
    It goes from Verdurian into English.
    :param text: string
    """
    verdurian_dictionary = get_verdurian_to_english_dictionary()
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
    return reassemble_word(
        starts_with_capital,
        ends_with_punctuation,
        english_word,
        word
    )
def into_esperanto(word):
    """words: It is the set of words the user puts in"""
    esperanto_dict = get_english_to_esperanto_dict()
    word = word.capitalize()
    punctuation_symbol = ""
    if word[-1] in punctuation:
        punctuation_symbol = word[-1]
        word = word[:-1]
    return esperanto_dict.lookup(word) + punctuation_symbol
def get_english_to_esperanto_dict():
    """
    Docstring for get_english_to_esperanto_dict
    It makes an Esperanto dictionary
    """
    return Dictionary(from_lang="english", to_lang="esperanto", corpus_path="esperanto_dict.txt")
