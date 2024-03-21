# logbook.py - easy string log enumerated and pickled..
import pickle
import os.path

class Logbook:
    def __init__(self, ownerstring):

        self.owner = ownerstring
        filename = 'LOG from '+self.owner+'.pickle'
        if os.path.isfile(filename):
            with open(filename, 'rb') as fileobj:
                self.logbook = pickle.load(fileobj)
                self.counter = len(self.logbook)
                print('logbook loaded..')

        else:
            self.counter = 0
            self.logbook = {}
            print('logbook new...')

    def exitting(self):
        #
        filename = 'LOG from '+self.owner+'.pickle'
        with open(filename, 'wb') as f:
            pickle.dump(self.logbook, f, pickle.HIGHEST_PROTOCOL)
            return 1

    def reset(self, ownerstring):

        #
        self.owner = ownerstring
        self.counter = 0
        self.logbook = {}

    def enter(self, entrystring):

        # 
        self.logbook[self.counter] = entrystring
        self.counter += 1
        print('logentry', self.counter, entrystring)

    def read(self):
        #
        entries = 0
        while entries < self.counter:

            print(entries, self.logbook[entries])
            entries += 1
        return entries

    def write(self):

        #
        filename = 'LOG from '+self.owner+'.txt'
        with open(filename, 'w') as loggerfile:

            entries = 0
            while entries < self.counter:

                entry = self.logbook[entries]+'\n'
                loggerfile.write(entry)
                entries += 1

        print('logbook saved.', filename)
