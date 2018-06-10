# Our own custom exception class.
class ParserError(Exception):
    pass

class Command(object):
    def __init__(self, subject, verb, obj):
        # The args are (<word type>, <word>) duples.
        self.subject = subject[1]
        self.verb = verb[1]
        self.obj = obj[1]

# Maps word to word type.
word_type = {
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'north': 'direction',
    'east': 'direction',
    'south': 'direction',
    'west': 'direction',
    'up': 'direction',
    'down': 'direction',
    'bear': 'noun',
    'princess': 'noun',
    'to': 'preposition',
    'from': 'preposition',
    'into': 'preposition',
    'a': 'article',
    'an': 'article',
    'the': 'article'
}


# Prompts user for a command.
def get_command():
    command = input('> ')
    tokens = tokenize(command)


# Turns space-separated list of words into list of (<word type>, <word>) tokens.
def tokenize(command):
    words = command.split()
    tokens = []
    token = (None, None)
    n = "NaN"
    for w in words:
        try:
            n = int(w)
        except ValueError:
            n = "NaN"
        try:
            token = (word_type[w] if (n == "NaN") else "number", w if (n == "NaN") else n)
        except KeyError:
            token = ("error", w)
        tokens.append(token)

    return tokens



