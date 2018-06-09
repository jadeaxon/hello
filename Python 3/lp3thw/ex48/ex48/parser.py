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
    'princess': 'noun'
}

def get_command():
    command = input('> ')
    tokens = tokenize(command)

def tokenize(command):
    words = command.split()
    tokens = []
    for w in words:
        token = (word_type[w], w)
        tokens.append(token)

    return tokens



