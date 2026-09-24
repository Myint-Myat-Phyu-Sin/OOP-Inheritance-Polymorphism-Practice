class FileProcessor:
    def process(self):
        print("Processing file")


class TextFile(FileProcessor):
    def process(self):
        print("Processing text file")


class ImageFile(FileProcessor):
    def process(self):
        print("Processing image file")


class AudioFile(FileProcessor):
    def process(self):
        print("Processing audio file")

files = [
    TextFile(),
    ImageFile(),
    AudioFile()
]

for file in files:
    file.process()