#testfile.py
from lab03 import integerDivision, collectEvenInts, countVowels, reverseString, removeSubString

def test_integerDivision():
    assert integerDivision(27,4) == 6
    assert integerDivision(5,7) == 0
    assert integerDivision(144,12) == 12
def test_collectEvenInts():
    assert collectEvenInts([1,2,3,4,5]) == [2,4]
    assert collectEvenInts([]) == []
    assert collectEvenInts([1,3,5]) == []
def test_countVowels():
    assert countVowels("This Is A String") == 4
    assert countVowels("") == 0
    assert countVowels("Hll m Sml") == 0
def test_reverseString():
    assert reverseString("CMPSC9") == "9CSPMC"
    assert reverseString("") == ""
    assert reverseString("racecar") == "racecar"
def test_removeSubString():
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("", "lol") == ""
    assert removeSubString("Boiboiboi", "oi") == "Bbb"
    

    
    
    
