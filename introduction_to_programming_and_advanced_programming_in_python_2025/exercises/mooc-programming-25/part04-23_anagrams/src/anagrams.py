# Write your solution here
def anagrams(str1: str, str2: str):
    """
    Checks if two strings are anagrams.
    
    Logic: Verify all chars from str1 appear same number of times in str2.
    Since len(str1) == len(str2), this guarantees str2 has no extra chars.
    No need to check str2 → str1 direction (would be redundant).
    
    Alternative (faster): return sorted(str1) == sorted(str2)
    """    
    if len(str1) != len(str2):
        return False

    for char1 in str1:
        index1   = 0
        counter1 = 0
        while(index1<len(str1)):
            if char1 == str1[index1]:
                counter1 +=1
            index1 +=1
        index2   = 0
        counter2 = 0
        while(index2<len(str2)):
            if char1 == str2[index2]:
                counter2 +=1
            index2 +=1
        
        if counter1 != counter2: 
            return False         
    return True                  

# Note: I checked all the chars from str1 and checked also if each one of them appear the same number of times on str2;
# NOTICE that I didn´t need to do the same check for all the chars from str2 because the first IF-declaration assures that
# str1 and str2 have the same number of chars, which is analogous to:
#   -- Count every char of str1 and compare with the counting on str2 AND
#   -- Count every char of str2 and compare with the counting on str1
# 
# tl; dr: It is sufficient to check every char from str1 and if they appear the same amount of times in str1 and str2 and
#         also know that len(str1) == len(str2) in order to prove that both strings are anagrams of each other


 # ===============================================================================================================   
 # Another way, but much easier and with much better performance, is to compare the 2 strings after sorting them ||
 # def anagrams (str1: str, str2: str):                                                                          ||
 #    return sorted(str1) == sorted(str2):                                                                       ||
 # ===============================================================================================================      
                                                                                                          
if __name__ == "__main__":
    ans1 = anagrams("tame", "mate")
    print(ans1)  #True
    ans2 = anagrams("polenta", "tilapia")
    print(ans2)  #False
    ans3 = anagrams('aab', 'abb')
    print(ans3)  #False
    ans4 = anagrams('ab', 'abc') # str1 has its chars in the same amount of str2, but str2 has a char that str1 doesn't have
    print(ans4)  #False
