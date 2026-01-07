#two strings, ransomeNote and magazine
#if ransomNote can be made from the letters in magazine, return true
    #Each letter can only be used as many times as it appears

#So my first thought is that if ransomNote is longer than magazine, then we can return false without any extra logic
    #Oh also if magazine length == 0. Just kidding that's already a constrain lol
#Then I'm considering looping through all the letters in magazine and putting them in an array, then loop through each letter in ransomNote and if the letter is in the new array, remove it. If it can't be found, return false.
    #Probably is a more optimal way to do this but this is my first thought to try

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        if len(ransomNote) > len(magazine):
            return False

        array_letters_to_use = []

        for char in magazine:
            array_letters_to_use.append(char)

        for char in ransomNote:
            for item in array_letters_to_use:
                if item == char:
                    array_letters_to_use.remove(item)
                    break
            else:   #Struggled here because I didn't know that python had an else statement for for loops
                return False
        return True
                    