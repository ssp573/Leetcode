class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        list_word=list(word)
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif list_word[0].isupper():
            for i in list_word[1:]:
                if i.isupper():
                    return False
            return True
        else:
            return False

