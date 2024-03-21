import random
import math

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# Const list
alpha = 10
mu1 = 5
mu2 = 5
TimeConst = 1
CarCount = 60


# Task Graph
def randomTime():
    number = round(random.uniform(0.01, 0.95), 2)
    return (number)


def GazZ():
    timeGazZ = round((-1 / alpha) * math.log(randomTime()), 2)
    # print(f'time of gazZ = {(round(TimeConst * timeGazZ, 2))}')
    return (TimeConst * timeGazZ)


def Kol1():
    timeKol1 = round((-1 / mu1) * math.log(randomTime()), 2)
    # print(f'time of Kol1 = {(round(TimeConst * timeKol1, 2))}')
    return (TimeConst * timeKol1)


def Kol2():
    timeKol2 = round((-1 / mu2) * math.log(randomTime()), 2)
    # print(f'time of Kol2 = {(round(TimeConst * timeKol2, 2))}')
    return (TimeConst * timeKol2)


if __name__ == '__main__':
    CarTimeGaz = []
    Car_arrive = [0]
    Car_arriveMu1 = [0]
    Car_arriveMu2 = [0]
    Car_Appendix = []
    Cars_in_arriveMu1 = []
    Cars_in_arriveMu2 = []
    Car_in_Appendix = []

    for i in range(CarCount):
        CarTimeGaz.append(GazZ())
        Car_arrive.append(round(Car_arrive[-1] + CarTimeGaz[-1], 2))
    Car_arrive.pop(0)

    for car in Car_arrive:
        if Car_arriveMu1[-1] <= car:
            Car_arriveMu1.append(round(car + Kol1(), 2))
            Cars_in_arriveMu1.append(Car_arrive.index(car) + 1)
        elif Car_arriveMu2[-1] <= car:
            Car_arriveMu2.append(round(car + Kol2(), 2))
            Cars_in_arriveMu2.append(Car_arrive.index(car) + 1)
        else:
            Car_Appendix.append(car)
            Car_in_Appendix.append(Car_arrive.index(car) + 1)

    Car_arrive.append(0)
    Car_arrive.sort()

    Car_arriveMu1.pop(0)
    Car_arriveMu2.pop(0)

    carsFueled = len(Cars_in_arriveMu1) + len(Cars_in_arriveMu2)
    Car_arriveMu = []
    Car_arriveMu += Car_arriveMu1
    Car_arriveMu += Car_arriveMu2

    CarsPerHour = max(Car_arriveMu)

    Percents = round(carsFueled / CarsPerHour, 2)
    print(Percents)

    #

    fig, ax = plt.subplots()
    # ax.plot(range(10))
    ax.set_yticks([0, 2, 4, 6, 8], labels=['Отказ', 'Обсл', 'КО2', 'КО1', 'ГЗ'])
    rangeXticks = round(max(Car_arriveMu)) + 2
    # print(rangeXticks)
    ax.set_xticks([x for x in range(rangeXticks)])

    print(f'CARS = {Car_arrive}')
    print(f'Mu1 = {Car_arriveMu1}')
    print(f'Mu2 = {Car_arriveMu2}')
    print(f'Appendix = {Car_Appendix}')
    print(f'cars in Mu1 = {Cars_in_arriveMu1}')
    print(f'cars in Mu2 = {Cars_in_arriveMu2}')
    print(f'cars in Appendix = {Car_in_Appendix}')

    for num in range(CarCount):
        Ylist = []
        Xlist = []
        if num + 1 in Cars_in_arriveMu1:
            Ylist.append(8)
            Xlist.append(Car_arrive[num])
            Ylist.append(8)
            Xlist.append(Car_arrive[num + 1])
            Ylist.append(6)
            Xlist.append(Car_arrive[num + 1])
            Ylist.append(6)
            Xlist.append(Car_arriveMu1[Cars_in_arriveMu1.index(num + 1)])
            Ylist.append(2)
            Xlist.append(Car_arriveMu1[Cars_in_arriveMu1.index(num + 1)])

            ax.plot(Xlist, Ylist)
        elif num + 1 in Cars_in_arriveMu2:
            Ylist.append(8)
            Xlist.append(Car_arrive[num])
            Ylist.append(8)
            Xlist.append(Car_arrive[num + 1])
            Ylist.append(4)
            Xlist.append(Car_arrive[num + 1])
            Ylist.append(4)
            Xlist.append(Car_arriveMu2[Cars_in_arriveMu2.index(num + 1)])
            Ylist.append(2)
            Xlist.append(Car_arriveMu2[Cars_in_arriveMu2.index(num + 1)])

            ax.plot(Xlist, Ylist)
        else:
            Ylist.append(8)
            Xlist.append(Car_arrive[num])
            Ylist.append(8)
            Xlist.append(Car_arrive[num + 1])
            Ylist.append(0)
            Xlist.append(Car_arrive[num + 1])

            ax.plot(Xlist, Ylist)

    ax.grid(True, ls='--', )
    ax.set_ylim(0, 10)
    ax.set_xlim(0, round(max(Car_arriveMu)) + 1)

    plt.show()
