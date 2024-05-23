import datetime
id = 0
tab = '\t'

class Report:
    def __init__(self, action:object):
        id += 1; self.dateTime = datetime.datetime.now()
        self.content = action
        with open('AccountsLog.log', 'a') as log:
            log.write(id, tab, self.dateTime, tab, self.content, '\n')
        return action