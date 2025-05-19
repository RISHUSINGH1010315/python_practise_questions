Vowel = ['a', 'e', 'i', 'o', 'u']
Word = "Programming"
count = 0
for charater in Word:
    if charater not in Vowel:
        count += 1
    print(count)