def to_string(num):
    # convert 4 to '04' and 39 to '39'
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)

class ClockIterator():
    def __iter__(self):
        self.curr = '00:00'
        return self

    def __next__(self):
        if self.curr == '23:59':
            x = self.curr
            self.curr = '00:00'
            return x
        else:
            minute = int(self.curr[-2:])
            if minute < 59: # eg 04:58
                x = self.curr
                self.curr = self.curr[:-2] + to_string(int(minute) + 1)
                return x
            else:
                x = self.curr
                self.curr = to_string(int(self.curr[:2]) + 1) + ':00'
                return x


def main():
    clock = ClockIterator()
    for time in clock:
        print(time)

if __name__ == "__main__":
    main()
