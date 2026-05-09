"""The app's test file"""
from app import into_english, into_pig_latin

def compare(real, expected):
    """It's just a nice test that tests if it's working"""
    print("Expected: " + expected)
    print(F"Real: {real}")
    if real != expected:
        print("❌ It's somehow wrong!")
    else:
        print("✅ It's somehow right?")

compare(into_english("oday"), "do")
compare(into_english("omputercay"), "computer")

compare(into_pig_latin("aligator"), "aligatorway")
compare(into_pig_latin("tall"), "alltay")
compare(into_pig_latin("how?"), "owhay?")
compare(into_pig_latin("ow!"), "owway!")
compare(into_pig_latin("Interesting."), "Interestingway.")
compare(into_pig_latin("No"), "Onay")
compare(into_pig_latin("that"), "atthay")

compare(into_english("owhay?"), "how?")
compare(into_english("interestingway."), "interesting.")
