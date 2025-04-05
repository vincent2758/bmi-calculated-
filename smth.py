import string
import random # define the random module
S = 681  # number of characters in the string

letters = 'abcdefg' 

ran = ''.join(random.choices(letters, k = S))
print("Generated text is : " + str(ran)) # print the random data
