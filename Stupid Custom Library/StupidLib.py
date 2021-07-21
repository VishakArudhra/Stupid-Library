class text_aug:
    def __init__(self, inpt):
        self.inpt = inpt
    def remove_repeats(self):
        split = self.inpt.split(' ')
        fix = []
        flag = 0
        for i in split:
            for ind, j in enumerate(i):
                    if(ind+2<len(i)):
                        if((i[ind]==i[ind+1])&(i[ind+1]==i[ind+2])):
                            flag = 1
                            break
            if (flag ==1):                
                i = ''.join(sorted(set(i),key = i.index))
                fix.append(i)
            else:
                fix.append(i)
        return ' '.join(split)