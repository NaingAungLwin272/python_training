#   1
import re


def text_match(text):
    pattern = 'I{2,3}'
    if re.search(pattern,  text):
        print('Found! Match Sentence')
    else:
        print('Oops! Nothing is match')


text_match("ABCDEFGHIIIII")


#   2
def text(text):
    patterns = '\w*a.'
    if re.search(patterns,  text):
        print("Found a Match")
    else:
        print('Not matched!')


text("Naing Aung Lwin")


#   3
def match_num(string):
    text = re.compile("^4")
    if text.match(string):
        print("Start with 4")
    else:
        print("Not Start with 4 ")


match_num('4 is number')
