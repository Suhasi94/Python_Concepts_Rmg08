class ConsoleLogger:

    def log(self, message):
        print(message)

    def display(self):
        print("This is display")

class TextLogger:
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        self.file_object.write(message+"\n")

class CSVLogger:
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        words = message.split()
        import csv
        write_obj = csv.writer(self.file_object)
        write_obj.writerow(words)

class FilteredLogger:

    def __init__(self, pattern, logger_object):
        self.logger_object = logger_object
        self.pattern = pattern

    def log(self, message):
        if self.pattern.lower() in message.lower():
            self.logger_object.log(message)
            self.logger_object.display()

c = ConsoleLogger()
fl = FilteredLogger("ERROR", c)
fl.log("This is an error message")

with open("sample.txt", "w") as file_:
    t = TextLogger(file_)
    fl = FilteredLogger("ERROR", t)
    fl.log("This is an error message")
