def count_spl_char(String):
    spl_char = "!@#$%^&*():;"
    count = 0
    for i in String:
        if i in spl_char:
            count += 1  
    return count  

text = "Hello! & Welcome to Rishu:channel (The rishu flet;)"
result = count_spl_char(text)
print(result)
