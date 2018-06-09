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
    n = "NaN"
    for w in words:
        try:
            n = int(w)
        except ValueError:
            n = "NaN"
        token = (word_type[w] if (n == "NaN") else "number", w if (n == "NaN") else n)
        tokens.append(token)

    return tokens



