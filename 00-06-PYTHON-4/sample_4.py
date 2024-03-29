#!/usr/bin/python3

text = """
The rabbit-hole went straight on like a tunnel for some way, and then dipped
suddenly down, so suddenly that Alice had not a moment to think about stopping
herself before she found herself falling down a very deep well.

Either the well was very deep, or she fell very slowly, for she had plenty of
time as she went down to look about her and to wonder what was going to happen
next. First, she tried to look down and make out what she was coming to, but it
was too dark to see anything; then she looked at the sides of the well, and
noticed that they were filled with cupboards and book-shelves; here and there
she saw maps and pictures hung upon pegs. She took down a jar from one of the
shelves as she passed; it was labelled `ORANGE MARMALADE', but to her great
disappointment it was empty: she did not like to drop the jar for fear of
killing somebody, so managed to put it into one of the cupboards as she fell
past it.

`Well!' thought Alice to herself, `after such a fall as this, I shall think
nothing of tumbling down stairs! How brave they'll all think me at home! Why, I
wouldn't say anything about it, even if I fell off the top of the house!'
(Which was very likely true.)
"""
text = text.lower()
text = text.replace(',', '').replace('.', '')
text = text.replace('-', '').replace(';', '').replace(':', '')
text = text.replace('\'', '').replace('`', '')
text = text.replace('(', '').replace(')', '')
text = text.replace('!', '').replace(' ', '').replace('\n', '')

letter_dict = {}
for letter in text:
    if letter not in letter_dict:
        letter_dict[letter] = 1
    else:
        letter_dict[letter] += 1
print(letter_dict)

# Reversed sorting of dictionary output
rs_list = sorted(letter_dict, key=lambda sym: letter_dict[sym], reverse=True)
for letter in rs_list:
    print('{}: {}'.format(letter, letter_dict[letter]))
