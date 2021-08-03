import pandas as pd
from shutil import copyfile
import datetime
import re
from Constants.Italian.escape_phrases import escape_phrases, add_phrase, rem_phrase

class Parser:
    def __init__(self, inputfile, outputfile):
        self.inputfile = inputfile
        self.outputfile = outputfile

        with open(inputfile, 'r') as fp: text = fp.readlines()
        self.text = text
        self.adds = None
        self.rems = None
        self.df = None
        self.dpu = None


    def str2date(self, mystr):
        date = datetime.datetime.strptime(mystr, "%d/%m/%y, %H:%M")
        return date


    def parse(self, dump=True):
        new_text = []
        adds = []
        rems = []
        index = 0
        end = len(self.text) - 1
        while index < end:
            curr_line = self.text[index]
            next_line = self.text[index + 1]

            if self.is_formatted(next_line):
                res = self.check_add_rem(curr_line)
                if len(res) >0:
                    if res['type'] == 'add':adds.append(res)
                    else: rems.append('type')
                else:
                    new_text.append(self.string2dict(curr_line))
                index += 1
            else:
                line_to_save = ""
                multiline_mode = True
                while multiline_mode:
                    line_to_save += curr_line.replace('\n', ' ') + ' '
                    index += 1
                    '''manage the case the text finishes with multiline'''
                    if index > end - 1:
                        line_to_save += next_line.replace('\n', ' ') + ' '
                        new_text.append(self.string2dict(line_to_save.rstrip()))
                        index = end + 2
                        break
                    if self.is_formatted(next_line):
                        multiline_mode = False
                        new_text.append(self.string2dict(line_to_save.rstrip()))
                    else:
                        curr_line = self.text[index]
                        next_line = self.text[index + 1]


        self.adds = pd.DataFrame(adds)
        self.rems = pd.DataFrame(rems)
        self.df = pd.DataFrame(new_text, columns=['date', 'user', 'mex'])

        if dump:
            self.adds.to_csv(self.outputfile+'_adds.csv',index=False)
            self.rems.to_csv(self.outputfile+'_rems.csv',index=False)
            self.df.to_csv(self.outputfile+'_formatted.csv', index=False)

    def compute_day_per_user(self):

        dpu = pd.DataFrame(columns=['user', 'min_date', 'max_date', 'days'])
        dpu['user'] = self.df.user.unique()
        dpu = dpu.set_index('user')
        dpu['min_date'] = self.df.groupby('user').min()['date']
        dpu['min_date'] = pd.to_datetime(dpu['min_date'])

        dpu['max_date'] = self.df.groupby('user').max()['date']
        dpu['max_date'] = pd.to_datetime(dpu['max_date'])

        dpu['days'] = dpu['max_date'] - dpu['min_date']
        dpu['days'] = dpu.days.dt.days
        self.dpu = dpu
        return dpu

    def is_formatted(self, line):
        pattern = re.compile("[0-9][0-9]\/[0-9][0-9]\/[0-9][0-9], [0-9][0-9]:[0-9][0-9] - (.*):")
        return pattern.match(line) != None


    def check_add_rem(self, line):
        if add_phrase in line:
            mex = line.split(' - ')[1]
            if ':' not in mex:
                date = self.str2date(line.split(' - ')[0])
                mex = mex.strip().split(add_phrase)
                admin = mex[0]
                user = mex[1]
                return dict(date=date, admin=admin, user=user, type='add')


        elif rem_phrase in line:
            mex = line.split(' - ')[1]
            if ':' not in mex:
                date = self.str2date(line.split(' - ')[0])
                mex = mex.strip().split(' ha rimosso ')
                admin = mex[0]
                user = mex[1]
                return dict(date=date, admin=admin, user=user, type='rem')

        return {}


    def string2dict(self, line):
        line = line.replace(' - ', ';').replace(': ', ';')
        line = line.split(';')
        date=self.str2date(line[0])
        user=line[1]
        mex = ''.join(line[2:]).strip()
        return dict(date=date, user=user, mex=mex)





