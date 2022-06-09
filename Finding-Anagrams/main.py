# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # to change text to lowercase

       
    word = word.lower()
    anagram = anagram.lower()

    # Remove whitespace
    word = word.replace(" ", "")
    anagram = anagram.replace(" ", "")

    # return sorted(word) == sorted(anagram): it will return a Boolean

    return sorted(word) == sorted(anagram)

    print("Calling find_anagram with 'dear' and 'read' ",
          find_anagram("dear", "read"))
    print("Calling find_anagram with 'adultery' and 'true lady' ",
          find_anagram("adultery", "true lady"))
    print("Calling find_anagram with 'tub' and 'but' ",
          find_anagram("tub", "but"))

    #return True