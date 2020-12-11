import sys
from myClass import classes, classTimes, t, headerText, formattedText, closest


def myFunc(e):
    return getattr(e, day)


try:
    day = sys.argv[1].lower()
    blockWanted = None
    try:
        blockWanted = sys.argv[2]
    except IndexError:
        blockWanted = None
    if((day == "a") or (day == "b") or (day == "c") or (day == "d")):
        currentDayClasses = []

        for i in classes:
            currentClassBlock = getattr(i, day)
            if(currentClassBlock is None):
                continue
            currentDayClasses.append(i)
        currentDayClasses.sort(key=myFunc)
        headerText()

        if(blockWanted is not None):
            if(blockWanted != "c"):
                blockWanted = int(blockWanted)
                formattedText(
                    currentDayClasses[blockWanted].name,
                    classTimes[blockWanted][0],
                    classTimes[blockWanted][1]
                )
            else:
                currentClassTimes = []
                for i in classTimes:
                    for j in i:
                        currentClassTimes.append(j)
                closestTime = closest(currentClassTimes, t)
                x = None

                for index, i in enumerate(classTimes):
                    try:
                        x = i.index(closestTime)
                        formattedText(
                            currentDayClasses[index].name,
                            classTimes[index][0],
                            classTimes[index][1],
                        )
                        break
                    except ValueError:
                        continue
                if (x is None):
                    print("no class rn")
        else:

            for index, j in enumerate(currentDayClasses):
                formattedText(
                    currentDayClasses[index].name,
                    classTimes[index][0],
                    classTimes[index][1],
                )
        print("")
    else:
        print("Invalid args")
except IndexError:
    print("invalid args")
