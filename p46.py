text = 'Programming in python.'
new_text = text.lower().rstrip('.').replace(' ', '')
vowels={'a', 'e', 'i', 'o', 'u',}
vowel_arr = []
unique = set()
letters = set()
for i in vowels:
    vowel_arr.append(i)
for i in new_text:
    letters.add(i)
for i in letters:
    if i not in vowels:
         unique.add(i)        
print(f'Number of items: {len(unique)}')
