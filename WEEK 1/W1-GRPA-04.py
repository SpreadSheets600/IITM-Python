# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
word1 = "Wingardium" # str
word2 = "Leviyosa" # str
word3 = "Silver" # str
sentence = "Learning python is fun"
n1 = 6 # int
n2 = 4 # int
# <eoi>

output1 = word1 + " " + word2 # str: join word1 and word2 with space in between

output2 = word1[0:4] + "-" + word2[-4:] # str: join first four letters of word1 and last four letters of word 2 with a hyphen "-" in between

output3 = word3 + " " + str(n1) # str: join the word3 and n1 with a space in between

output4 = "-" * 50 # str: just the hypen "-" repeated 50 times

output5 = "-" * n2 # str: just the hypen "-" repeated n2 times

output6 = str(n1) * n2 # str: repeat the number n1, n2 times

are_all_words_equal = True if word1 == word2 == word3 else False # bool: True if all three words are equal

is_word1_comes_before_other_two = True if word1 < word2 and word1 < word3 else False # bool: True if word1 comes before other two words

has_h = True if "h" in word1 else False # bool: True if word1 has the letter h

ends_with_a = True if word1[-1] in ["a", "A"] else False # bool: True if word1 ends with letter a or A

has_the_word_python = True if "python" in sentence.split(" ") else False # bool: True if the sentence has the word python
