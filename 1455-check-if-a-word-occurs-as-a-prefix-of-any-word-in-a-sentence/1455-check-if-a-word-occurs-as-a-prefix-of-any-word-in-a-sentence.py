class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

      letter=sentence.split(" ")

      for j,i in enumerate(letter):
          if len(i)>=len(searchWord) and i[0:len(searchWord)]==searchWord:
               return j+1
      return -1
               
        