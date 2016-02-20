class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    # study drill 3 -> Make the class do more things
    def new_lyrics(self, lyrics):
        self.lyrics = lyrics

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family", "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

# study drill 1, 2
lyric = ["I never thought I'd need you there when I cry", "And the days feel like years when I'm alone",
         "And the bed where you lie", "Is made up on your side"]
when_you_are_gone = Song(lyric)
when_you_are_gone.sing_me_a_song()

# study drill 3
when_you_are_gone.new_lyrics(["good job!", "test successfully"])
when_you_are_gone.sing_me_a_song()
