word = input('Enter your new password: ')

x = len(word)

if x >=12: print('strong')
elif x>=8: print('good')
else: print('weak')
