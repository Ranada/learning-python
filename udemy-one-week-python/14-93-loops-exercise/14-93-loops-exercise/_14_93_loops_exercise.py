
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable

for c in word:
    print(c)
print("*" * 100)

# Write a while loop that does the same thing!
i = 0
while i < len(word):
    print(word[i])
    i += 1
print("*" * 100)

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
j = 100
while j <= 140:
    print(j)
    j += 2
print("*" * 100)

# Write a for loop that does the same thing (with range())
for num in range(100, 141, 2):
    print(num)
print("*" * 100)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
entry = ''
while entry != 'sillygoose':
    entry = input("Enter the phrase 'sillygoose': ")
    print("Nope. You need to enter 'sillygoose' you silly goose!\n")