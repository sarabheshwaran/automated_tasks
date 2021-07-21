#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start

# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
revtext = ''
for word in text.split():
	word = word[::-1]
	revtext += ' ' + word
	
pyperclip.copy(revtext)


