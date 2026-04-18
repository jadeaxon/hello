#!/usr/bin/env python3

# Generates an endless stream of nonsense.

import random

nouns = [
    'donkey', 'cat', 'turkey', 'banana', 'blender', 'frisbee', 'spider', 'lamp', 'guitar',
    'mango', 'flower', 'waterfall', 'alien', 'fountain', 'tree', 'enchillada', 'clam',
    'frog', 'bee', 'tornado', 'trumpet', 'can of frosting', 'jar of mayo', 'cheesecake'
]
adjectives = [
     'angry', 'hungry', 'wild', 'tired', 'manic', 'thoughtful', 'drunk', 'distracted', 'shady',
     'impressive', 'thirsty', 'evil', 'trustworthy', 'graceful', 'unamused', 'glitchy',
     'jaded', 'diseased', 'frozen', 'melting', 'ginormous', 'disintegrating'
]
adverbs = [
    'quickly', 'thoroughly', 'patiently', 'relentlessly', 'unceremoniously', 'wearily',
    'slowly', 'completely', 'willfully', 'reluctantly', 'angrily', 'accidentally'
]
verbs = [
    'kick', 'tweak', 'smack', 'drop', 'twist', 'blast', 'chop', 'peel', 'destroy', 'heal',
    'format', 'debug', 'truncate', 'abandon', 'revive', 'ponder', 'interogate', 'pop',
    'burp', 'scold', 'ignore', 'taunt', 'defeat', 'wrestle', 'mock', 'educate'
]

def nonsense():
    adjective1 = random.choice(adjectives)
    noun1 = random.choice(nouns)
    verb = random.choice(verbs)

    # Past tenses are a bit tricky.
    if verb[-2] in 'aeiou' and verb[-1] not in 'aeiouyrn':
        if verb[-3] not in 'aeiou': # peeled, healed, etc.
            verb += verb[-1]
    if verb.endswith('e'): verb = verb[0:-1]

    adverb = random.choice(adverbs)
    adjective2 = random.choice(adjectives)
    noun2 = random.choice(nouns)
    s = f'The {adjective1} {noun1} {adverb} {verb}ed the {adjective2} {noun2}.'
    print(s)

if __name__ == '__main__':
    while True:
        nonsense()
        input()


