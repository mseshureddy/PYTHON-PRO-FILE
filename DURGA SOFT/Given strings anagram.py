'''
s='seshu'
s1='heussjhnu'
if sorted(s)==sorted(s1):
    print("anagram")
else:
    print("not anagram")

'''
#palindrome
'''
def ispalindrome(s):
    return s == s[::-1]

string='malayalam'
if ispalindrome(string):
    print("palindrome")
else:
    print("not palindrome")
'''
s='malayalam'
s1=s[::-1]
if s==s1:
    print("palindrome")
else:
    print("not palindrome")
