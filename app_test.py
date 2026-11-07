"""The app's test file"""
import sys
from app import into_verdurian, from_verdurian, into_esperanto
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

if compare(into_verdurian("conjuror"), "žóuom"):
    failures += 1
if compare(into_verdurian("abandon"), "fäsir"):
    failures += 1
if compare(into_verdurian("Thither"), "Cečelán"):
    failures += 1
if compare(into_verdurian("Yes."), "Ar."):
    failures += 1
if compare(into_verdurian("Felix."), "Felix."):
    failures += 1
if compare(from_verdurian("Ar."), "Yes."):
    failures += 1
if compare(from_verdurian("řosmeric"), "incompetent"):
    failures += 1
if compare(into_verdurian("hesitant herbalist"), "ukešec zeřašom"):
    failures += 1
if compare(into_verdurian("Fertile encompass!"), "Ofóry impiser!"):
    failures += 1
if compare(from_verdurian("velašir"), "elope"):
    failures += 1
if compare(into_verdurian("Elenico"), "Elenico"):
    failures += 1
if compare(into_esperanto("instructor"), "instruisto"):
    failures += 1
if compare(into_esperanto("Yes."), "jes."):
    failures += 1
print(f"{failures} test(s) failed!")
if failures > 0:
    sys.exit(1)
