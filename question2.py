#in this we have to replace a letter by other letter

letter = '''
Dear <|Name>
You are Selected By Google 
<|Date>'''
print(letter.replace("<|Name>", "Rishu Singh").replace("<|Date>", "13th May"))