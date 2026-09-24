class Media:
    def __init__(self, title):
        self.title = title
    def play(self):
        print(f"Playing {self.title}")
class Audio(Media):
   def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration
   def play(self):
       print(f"{self.title} - {self.duration}")
class Podcast(Audio):
   def __init__(self, title, duration, host):
        super().__init__(title, duration)
        self.host = host
   def play(self):
       print(f"AI Today hosted by {self.host}")
program1 = Media("Python Basic")
program2 = Audio("Relaxing Music", "4minutes")
program3 = Podcast("AI", "Today", "John")
program1.play()
program2.play()
program3.play()