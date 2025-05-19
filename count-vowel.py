Vowel = ['a', 'e', 'i', 'o', 'u']
Word = "Programming"
count = 0
for character in Word:
    if character in Vowel:
        count += 1
    print(count)    
