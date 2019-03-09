# Grant's non-periodic work at home schedule generator.

import random
import os

rps = ''
index = 0
DaysOfWeek = ['Monday','Tuesday','Wednesdsay','Thursday','Friday']
Symbols = [':)', ':(',':|',':p',':$']

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def pickMeetingDay(one, two):
    for i in range(len(DaysOfWeek)):
        if i != one and i != two:
            return i

def  generate():
    wah1 = random.randint(0,4)
    wah2 = random.randint(0,4)
    apsm = pickMeetingDay(wah1, wah2)
    while True:
        if wah1 != wah2:
            break
        wah2 = random.randint(0,4)

    apsm = pickMeetingDay(wah1, wah2)

    print('WAH Day One -> ' + DaysOfWeek[wah1])
    print('WAH Day Two -> ' + DaysOfWeek[wah2])
    print('APS Meeting -> ' + DaysOfWeek[apsm])
    print('Jeff\'s Mood -> ' + Symbols[wah1])
    print('')

# Begin
clear()
while True:
    if index == 0:
        index += 1
        rsp = raw_input('Generate WAH Days? (y/n) ')
    else:
        rsp = raw_input('Regenerate WAH Days? (y/n) ')

    if rsp == 'Y' or rsp == 'y':
        clear()
        generate()
    else:
        break

