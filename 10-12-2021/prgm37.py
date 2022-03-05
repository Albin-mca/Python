# 37. Accept a list of words and return length of longest word using user-defined function

def longest():
   text = input("Please input a List of words to evaluate: ")
   longest = 0
   for words in text.split():
      if len(words) > longest:
         longest = len(words)
   print("The longest word is", words, "with lenght", longest)
longest()
