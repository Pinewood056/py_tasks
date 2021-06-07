class DateTask:

    def __init__(self, dd, mm, yyyy):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

    def check(self):
        if self.dd <= 30 and self.mm == 1 or self.dd <= 30 and self.mm == 4 or self.dd <= 30 and self.mm == 6 or\
                self.dd <= 30 and self.mm == 9 or self.dd <= 30 and self.mm == 11:
            return True
        elif self.dd <= 29 and self.mm == 2 and self.yyyy % 4 == 0:
            return True
        elif self.dd <= 31 and self.mm == 3 or self.dd <= 31 and self.mm == 5 or self.dd <= 31 and self.mm == 7 or\
                self.dd <= 31 and self.mm == 8 or self.dd <= 31 and self.mm == 10 or self.dd <= 31 and self.mm == 12:
            return True
        elif self.dd <= 28 and self.mm == 2 and self.yyyy % 4 != 0:
            return True
        elif self.dd >= 32 or self.mm >= 13:
            return False
        else:
            return False
        
