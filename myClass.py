from datetime import datetime as dt


class myClass:
    def __init__(self, name, a, b, c, d):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.d = d


classes = [
    myClass("AP Calculus AB", 1, None, 3, 2),
    myClass("AP Computer Science", 2, 1, None, 3),
    myClass("Driver Theory", 3, 2, 1, None),
    myClass("Chemistry Lab H", None, 3, 2, 1),
    myClass("English II H", 4, None, 6, 5),
    myClass("Spanish III H", 5, 4, None, 6),
    myClass("Introduction to Music", 6, 5, 4, None),
    myClass("US History I H", None, 6, 5, 4),
]
classesQ = [
    myClass("AP Calculus AB", 1, None, None, None),
    myClass("AP Computer Science", 3, 1, None, None),
    myClass("Driver Theory", None, 3, 1, None),
    myClass("Chemistry Lab H", None, None, 3, 1),
    myClass("English II H", 2, None, None, None),
    myClass("Spanish III H", 4, 2, None, None),
    myClass("Introduction to Music", None, 4, 2, None),
    myClass("US History I H", None, None, 4, 2),
]
classTQ = [
    [7, 17, 0], [9, 0, 0],
    [9, 10, 0], [10, 40, 0],
    [10, 45, 0], [11, 10, 0],
    [11, 15, 0], [11, 40, 0],
]

t = dt.now()
classT = [
    [7, 17, 0], [8, 2, 0],
    [8, 7, 0], [8, 50, 0],
    [8, 55, 0], [9, 38, 0],
    [9, 43, 0], [10, 26, 0],
    [10, 31, 0], [11, 14, 0],
    [11, 19, 0], [12, 2, 0],
]
classTimes = []
for i in range(0, len(classT), 2):
    classTimes.append(
        [
            dt(t.year, t.month, t.day, classT[i]
               [0], classT[i][1], classT[i][2]),
            dt(t.year, t.month, t.day, classT[i + 1]
               [0], classT[i + 1][1], classT[i + 1][2]),
        ]
    )


def headerText():
    print("")
    print("{0:<28}".format("CLASS") + "{0:<6}".format("START") + "{0:<9}"
          .format("") + "{0:<6}".format("END"))
    print("{0:-<28}".format("") + "{0:-<6}".format("") + "{0:-<6}"
          .format("") + "{0:-<5}".format("") + "{0:-<10}".format(""))


def formattedText(className, classStart, classEnd):
    print("{0:.<28}".format(className) + "{0:<6}"
          .format(classStart.strftime("%I:%M %p")) + "" + "{0:.<7}"
          .format("") + "{0:<6}"
          .format(classEnd.strftime("%I:%M %p")) + "" + "{0:.<4}".format(""))


def closest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))
