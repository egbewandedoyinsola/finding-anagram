# This simple python program checks if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):

    # my code for implementing the function
    if(sorted(word) == sorted(anagram)):
        # used return to get info back from function
        # the return key word breaks us out of the function
        return True

    else:
        return False


print(find_anagrams("hello", "check"))
print(find_anagrams("below", "elbow"))
print(find_anagrams("players", "parsley"))
print(find_anagrams("cider", "cried"))
