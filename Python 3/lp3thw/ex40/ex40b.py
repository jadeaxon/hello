#!/usr/bin/env python3

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.sing = self.sing_me_a_song # Alias

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def reverse_sing(self):
        r = list(self.lyrics)
        r.reverse()
        for line in r:
            print(line)


happy_bday = Song([
    "Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"
])

bulls_on_parade = Song([
    "They rally around than family",
    "With pockets full of shells"
])

lyrics = [
    "Twinlke, twinkle little star",
    "How I wonder what you are"
]
twinkle = Song(lyrics)

mary = Song([
    "Mary had a little lamb",
    "With mint sauce"
])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
twinkle.sing()
mary.sing()
mary.reverse_sing()
