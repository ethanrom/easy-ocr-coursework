title = ''
with open('input.txt', 'r') as file:
    data = file.read()
    data = data.replace('[','').replace(']','').replace("'",'').split(',')
    for word in data:
        if 'measurement' in word or 'AC meter' in word:
            title = word
            break
print("Title:", title)
