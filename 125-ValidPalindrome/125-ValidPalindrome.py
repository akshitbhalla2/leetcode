# Last updated: 4/19/2026, 11:23:41 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:

        news = ""
        for char in s:
            if char.isalnum():
                news += char

        news = news.lower()

        size = len(news)

        for i in range(size//2):
            if news[i] != news[size-1-i]:
                print(i, news[i], news[size-1-i]) 
                return False

        return True