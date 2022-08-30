string='sehu098@
'
special_char = False
for letter in string:
    if (not letter.isnumeric() and not letter.isdigit()):
        special_char = True
        break
