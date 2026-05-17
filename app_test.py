"""The app's test file"""
import sys
from app import into_pig_latin, into_verdurian
failures = 0
def compare(real, expected):
    """It's just a nice test that tests if it's working"""
    print("Expected: " + expected)
    print(F"Real: {real}")
    if real != expected:
        print("❌ It's somehow wrong!")
        return True
    print("✅ It's somehow right?")
    return False

if compare(into_pig_latin("aligator"), "aligatorway"):
    failures += 1
if compare(into_pig_latin("tall"), "alltay"):
    failures += 1
if compare(into_pig_latin("how?"), "owhay?"):
    failures += 1
if compare(into_pig_latin("ow!"), "owway!"):
    failures += 1
if compare(into_pig_latin("Interesting."), "Interestingway."):
    failures += 1
if compare(into_pig_latin("No"), "Onay"):
    failures += 1
if compare(into_pig_latin("that"), "atthay"):
    failures += 1
if compare(into_verdurian("Verdurian"), "soa Sfahe"):
    failures += 1
if compare(into_verdurian("abandon"), "fäsir"):
    failures += 1
if failures > 0:
    print("At least 1 test failed!")
    sys.exit(1)
