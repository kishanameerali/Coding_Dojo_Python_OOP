class MathDojo(object):
    def __init__ (self):
        self.num = 0

    def add(self, *add_num):
        for i in add_num:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.num = self.num + k
                else:
                    self.num = self.num + i
        return self

    def subtract(self, *sub_num):
        for i in sub_num:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.num = self.num - k
                else:
                    self.num = self.num - i
        return self


md = MathDojo()
print (md.add(2).add(2, 5).subtract(3, 2).num)