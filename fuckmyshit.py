from googletrans import Translator
from random import randint
import lang

translator = Translator()
l = lang.launguages


def fuckit(power):
    text = input('Please enter text... \n')
    print('PROCESSING... \n')
    start_lang = translator.detect(text).lang
    for i in range(power):
        dest = l[randint(0, len(l)-1)]
        # print (dest)
        text = translator.translate(text, dest=dest).text
    return translator.translate(text, dest=start_lang).text

while True:
    power = int(input('Enter how hard to fuck this text: '))
    
    print(fuckit(power))
    # b = input('\n Continue? Y or N: ').lower
    # if b == 'y':
    #     continue
    # elif b == 'n':
    #     exit()