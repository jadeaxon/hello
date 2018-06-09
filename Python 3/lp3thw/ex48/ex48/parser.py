word_type = {
    'go': 'verb',
    'north': 'direction',
    'east': 'direction',
    'south': 'direction',
    'west': 'direction',
    'up': 'direction',
    'down': 'direction'
}

def get_command():
    command = input('> ')
    tokens = tokenize(command)

def tokenize(command):
    words = command.split()
    tokens = []
    for w in words:
        token = (word_type[w], w)
        tokens.push(token)

    return tokens



