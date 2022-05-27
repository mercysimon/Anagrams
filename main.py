# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
   if sorted(str1)==sorted(str2):
       print (True)
   else:
        print (False) # [assignment] Add your code here
        
    
str1="Stool"
str2="Tools"
str1 = str1.lower()
str2 = str2.lower()
find_anagram(str1,str2)