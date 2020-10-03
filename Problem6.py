original = 323
new = list(str(original))
new.reverse()
print(f'original number is {original}\n The Original and Reverse is same') if new == list(str(original)) else print(f'original number is {original}\n The Original and Reverse is not same')
