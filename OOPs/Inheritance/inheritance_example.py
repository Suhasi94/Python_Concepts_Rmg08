class ConsoleLogger:

    def log(self, message):
        print(message)


class FilteredConsoleLogger(ConsoleLogger):

    def __init__(self, pattern):            # error
        self.pattern = pattern

    def log(self, message):             # This is an error message
        if self.pattern.lower() in message.lower():
            super().log(message)

# c = FilteredConsoleLogger("error")
# c.log("this is an error message")


class TextLogger:
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        self.file_object.write(message+"\n")


class FilteredTextLogger(TextLogger):

    def __init__(self, pattern, file_object):
        self.pattern = pattern
        super().__init__(file_object)

    def log(self, message):
        if self.pattern.lower() in message.lower():
            super().log(message)

import os
os.chdir(r"C:\Users\User\OneDrive\Desktop\svit")
# file_obj = open("sample1.txt", "w")
# ftl = FilteredTextLogger("Info", file_obj)
# ftl.log("This is a info message")

# file_obj = open("sample1.txt", "a")
# text_log = TextLogger(file_obj)
# text_log.log("hello world")

# with open("sample.txt", "a") as file_obj:
#     text_log = TextLogger(file_obj)
#     text_log.log("hai")


class CSVLogger:
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        words = message.split()
        import csv
        write_obj = csv.writer(self.file_object)
        write_obj.writerow(words)


class FilteredCSVLogger(CSVLogger):
    def __init__(self, pattern, file_object):
        self.pattern = pattern
        super().__init__(file_object)

    def log(self, message):
        if self.pattern.lower() in message.lower():
            super().log(message)
            

file_obj = open("demo1.csv", "w")
fcl = FilteredCSVLogger("Error", file_obj)
fcl.log("This is an error message")


# file_obj = open("demo.csv", "w")
# csv_log = CSVLogger(file_obj)
# csv_log.log("hello world welcome")
