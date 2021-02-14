class Meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos


def maxMeeting( l, n):
    ans = []
    l.sort(key=lambda x: x.end)
    print(l)


if __name__ == '__main__':
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    n = len(s)
    l = []
    for i in range(n):
        l.append(Meeting(s[i], f[i], i))
    maxMeeting(l, n)
