class ConsoleLogger:

    def log(self, message):
        print(message)

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

    def __init__(self, pattern):
        self.pattern = pattern


    def log(self, message):
        if self.pattern.lower() in message.lower():
            super().log(message)




class FilteredConsoleLogger(FilteredLogger, ConsoleLogger):

    def __init__(self, pattern):
        super().__init__(pattern)


fcl = FilteredConsoleLogger("ERROR")
fcl.log("This is an error message")



class FilteredTextLogger(FilteredLogger, TextLogger):

    def __init__(self, pattern, file_object):
        FilteredLogger.__init__(self, pattern)
        TextLogger.__init__(self, file_object)



# file_obj = open("sample1.txt", "w")
# ftl = FilteredTextLogger("error", file_obj)
# ftl.log("This is an error message")

# fcl = FilteredConsoleLogger("error")
# fcl.log("this is an error message")























