class Timer:
    def __init__(self, h, m, s):
        self.hh = h
        self.mm = m
        self.ss = s

    def __str__(self):
        return str(f'{self.hh}:{self.mm}:{self.ss}')

    def next_second(self):
        if self.ss == 59:
            self.mm += 1
            self.ss = 0
            if self.mm == 60:
                self.hh += 1
                self.mm = 0
                if self.hh == 24:
                    self.hh = 0
        else:
            self.ss += 1

    def prev_second(self):
        if self.ss == 0:
            self.mm -= 1
            self.ss = 59
            if self.mm == -1:
                self.mm = 59
                self.hh -= 1
                if self.hh == -1:
                    self.hh = 23
        else:
            self.ss -= 1


timer = Timer(23, 56, 58)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

