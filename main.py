import random
import math

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# Const list
alpha = 10
mu1 = 5
mu2 = 5

# 1 - hours 60 - minutes
TimeConst = 1
CarCount = 20
MaxQ = 3


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

    Cars = []

    CarTimeGaz = []
    St1 = 0
    St2 = 0
    Q = {"4": [-1, 0], "6": [-1, 0], "8": [-1, 0]}
    Qi = 0

    for i in range(CarCount):
        CarTimeGaz.append(GazZ())
        if i == 0:
            Cars.append({"14": [0]})
        else:
            Cars.append({"14": [Cars[i - 1]["14"][1]]})
        Cars[i]["14"].append(round(Cars[i]["14"][0] + GazZ(), 2))
        Cars[i]["14"].append(round(Cars[i]["14"][1] - Cars[i]["14"][0], 2))

    for car in range(len(Cars)):
        Q = dict(sorted(Q.items(), key=lambda item: item[1][1]))
        for qcar in Q.keys():
            if (St1 < Cars[car]["14"][1] or St2 < Cars[car]["14"][1]) and Q[qcar][0] != -1:
                if St1 < St2:
                    t = Kol1()
                    Cars[Q[qcar][0]][qcar].append(St1)
                    Cars[Q[qcar][0]][qcar].append(round(St1 - Cars[Q[qcar][0]][qcar][0], 2))
                    Cars[Q[qcar][0]]["12"] = [St1, round(St1 + t, 2), t]
                    Cars[Q[qcar][0]]["2"] = round(St1 + t, 2)
                    St1 = round(St1 + t, 2)
                    Q[qcar] = [-1, 0]
                    Qi -= 1

                else:
                    t = Kol2()
                    Cars[Q[qcar][0]][qcar].append(St2)
                    Cars[Q[qcar][0]][qcar].append(round(St2 - Cars[Q[qcar][0]][qcar][0], 2))
                    Cars[Q[qcar][0]]["10"] = [St2, round(St2 + t, 2), t]
                    Cars[Q[qcar][0]]["2"] = round(St2 + t, 2)
                    St2 = round(St2 + t, 2)
                    Q[qcar] = [-1, 0]
                    Qi -= 1

        if St1 <= Cars[car]["14"][1] and Qi == 0:
            t = Kol1()
            Cars[car]["12"] = [Cars[car]["14"][1], round(Cars[car]["14"][1] + t, 2), t]
            Cars[car]["2"] = round(Cars[car]["14"][1] + t, 2)
            St1 = round(Cars[car]["14"][1] + t, 2)
        elif St2 <= Cars[car]["14"][1] and Qi == 0:
            t = Kol2()
            Cars[car]["10"] = [Cars[car]["14"][1], round(Cars[car]["14"][1] + t, 2), t]
            Cars[car]["2"] = round(Cars[car]["14"][1] + t, 2)
            St2 = round(Cars[car]["14"][1] + t, 2)
        elif Qi < MaxQ:
            if Q["8"][0] == -1:
                Cars[car]["8"] = [Cars[car]["14"][1]]
                Q["8"] = [car, Cars[car]["14"][1]]
                Qi += 1
            elif Q["6"][0] == -1 and MaxQ >= 2:
                Cars[car]["6"] = [Cars[car]["14"][1]]
                Q["6"] = [car, Cars[car]["14"][1]]
                Qi += 1
            elif Q["4"][0] == -1 and MaxQ >= 3:
                Cars[car]["4"] = [Cars[car]["14"][1]]
                Q["4"] = [car, Cars[car]["14"][1]]
                Qi += 1
            else:
                print("Error")
        else:
            Cars[car]["0"] = Cars[car]["14"][1]

    Q = dict(sorted(Q.items(), key=lambda item: item[1][1]))
    for qcar in Q.keys():
        if Q[qcar][0] != -1:
            if St1 < St2:
                t = Kol1()
                Cars[Q[qcar][0]][qcar].append(St1)
                Cars[Q[qcar][0]][qcar].append(round(St1 - Cars[Q[qcar][0]][qcar][0], 2))
                Cars[Q[qcar][0]]["12"] = [St1, round(St1 + t, 2), t]
                Cars[Q[qcar][0]]["2"] = round(St1 + t, 2)
                St1 = round(St1 + t, 2)
                Q[qcar] = [-1, 0]
                Qi -= 1

            else:
                t = Kol2()
                Cars[Q[qcar][0]][qcar].append(St2)
                Cars[Q[qcar][0]][qcar].append(round(St2 - Cars[Q[qcar][0]][qcar][0], 2))
                Cars[Q[qcar][0]]["10"] = [St2, round(St2 + t, 2), t]
                Cars[Q[qcar][0]]["2"] = round(St2 + t, 2)
                St2 = round(St2 + t, 2)
                Q[qcar] = [-1, 0]
                Qi -= 1

    # for car in Cars:
    # print(car)

    Exp_time = sorted([x['2'] for x in Cars if '2' in x.keys()])[-1]
    print(f'-Время эксперимента, Exp_time = {Exp_time}')
    # Statistic:
    # N1
    # Fueled cars / experiment's time
    Fueled_cars = len([0 for x in Cars if '2' in x.keys()])
    print(f'-Заправленные машины, Fueled_cars = {Fueled_cars}')
    Throughput = Fueled_cars / Exp_time
    print(f"Fueled cars per hour = {Throughput}")

    # N2
    # Fueled cars / All cars
    print(f'-Общее количество машин, len(Cars) = {len(Cars)}')
    Fueling_Chance = Fueled_cars / len(Cars)
    print(f"Chance to fuel your car = {Fueling_Chance}")

    # N3
    # Refused cars / All cars
    Refused_cars = len([0 for x in Cars if '0' in x.keys()])
    print(f'-Отказы машинам, Refused_cars = {Refused_cars}')
    Refusal_Chance = Refused_cars / len(Cars)
    print(f"Chance to get refusal = {Refusal_Chance}")

    # N4
    # Sum of fuiling time on station / experiment's time
    St1_Fuiling_Chance = sum([x['12'][2] for x in Cars if '12' in x.keys()]) / Exp_time
    St2_Fuiling_Chance = sum([x['10'][2] for x in Cars if '10' in x.keys()]) / Exp_time
    print(f"Chance of fuiling atm on station 1 = {round(St1_Fuiling_Chance, 2)}")
    print(f"Chance of fuiling atm on station 2 = {round(St2_Fuiling_Chance, 2)}")

    # N5
    # Sum of fuiling time on 1 station and double fuiling time on 2 station
    SumSt_Fuiling_Chance = St1_Fuiling_Chance + 2 * St2_Fuiling_Chance
    print(f"Chance of summary fuiling atm on station's = {round(SumSt_Fuiling_Chance, 2)}")

    # N6
    # Sum of afk time on station / experiment's time
    times = [[0, 0]]
    times += [[x['12'][0], x['12'][1]] for x in Cars if '12' in x.keys()]
    times.append([Exp_time, Exp_time])
    St1_afk_chance = sum([round(times[t + 1][0] - times[t][1], 2) for t in range(len(times) - 1)]) / Exp_time
    St1_afk_times = [[times[t][1], times[t + 1][0]] for t in range(len(times) - 1) if times[t][1] != times[t + 1][0]]

    times = [[0, 0]]
    times += [[x['10'][0], x['10'][1]] for x in Cars if '10' in x.keys()]
    times.append([Exp_time, Exp_time])
    St2_afk_chance = sum([round(times[t + 1][0] - times[t][1], 2) for t in range(len(times) - 1)]) / Exp_time
    St2_afk_times = [[times[t][1], times[t + 1][0]] for t in range(len(times) - 1) if times[t][1] != times[t + 1][0]]

    times = St1_afk_times + St2_afk_times
    SummaryAFKTime = 0
    for timeTMP1 in times:
        for timeTMP2 in times:
            tmp = []
            if timeTMP1 != timeTMP2:
                if timeTMP1[0] >= timeTMP2[0]:
                    tmp.append(timeTMP1[0])
                else:
                    tmp.append(timeTMP2[0])
                if timeTMP1[1] <= timeTMP2[1]:
                    tmp.append(timeTMP1[1])
                else:
                    tmp.append(timeTMP2[1])

                if tmp[1] - tmp[0] > 0:
                    SummaryAFKTime += tmp[1] - tmp[0]
    SummaryAFKTime /= 2
    SumSt_afk_chance = SummaryAFKTime / Exp_time

    print(f"Chance of station 1 to be afk atm = {round(St1_afk_chance, 2)}")
    print(f"Chance of station 2 to be afk atm = {round(St2_afk_chance, 2)}")
    print(f"Chance of summary station's to be afk atm = {round(SumSt_afk_chance, 2)}")

    # N7

    # New data
    # N8
    # Sum of time in queue / cars amount
    match MaxQ:
        case 3:
            Avg_queue1_time = sum([x['8'][2] for x in Cars if '8' in x.keys()]) / CarCount
            Avg_queue2_time = sum([x['6'][2] for x in Cars if '6' in x.keys()]) / CarCount
            Avg_queue3_time = sum([x['4'][2] for x in Cars if '4' in x.keys()]) / CarCount
            print(f"Average time spent in 1st queue = {round(Avg_queue1_time, 2)}")
            print(f"Average time spent in 2nd queue = {round(Avg_queue2_time, 2)}")
            print(f"Average time spent in 3rd queue = {round(Avg_queue3_time, 2)}")
            Avg_queue_time = (Avg_queue1_time + Avg_queue2_time + Avg_queue3_time) / 3
            print(f"Average time spent in queue = {round(Avg_queue_time, 2)}")
        case 2:
            Avg_queue1_time = sum([x['8'][2] for x in Cars if '8' in x.keys()]) / CarCount
            Avg_queue2_time = sum([x['6'][2] for x in Cars if '6' in x.keys()]) / CarCount
            print(f"Average time spent in 1st queue = {round(Avg_queue1_time, 2)}")
            print(f"Average time spent in 2nd queue = {round(Avg_queue2_time, 2)}")
            Avg_queue_time = (Avg_queue1_time + Avg_queue2_time) / 2
            print(f"Average time spent in queue = {round(Avg_queue_time, 2)}")
        case 1:
            Avg_queue1_time = sum([x['8'][2] for x in Cars if '8' in x.keys()]) / CarCount
            print(f"Average time spent in queue = {round(Avg_queue1_time, 2)}")
        case _:
            print("No queue")

    # N9
    # Time of car fuiling / cars amount
    Avg_St1_time = sum([x['12'][2] for x in Cars if '12' in x.keys()]) / CarCount
    Avg_St2_time = sum([x['10'][2] for x in Cars if '10' in x.keys()]) / CarCount
    Avg_St_time = (Avg_St1_time + Avg_St2_time) / 2
    print(f"Average time spent to fuel car on Station 1 = {round(Avg_St1_time, 2)}")
    print(f"Average time spent to fuel car on Station 2 = {round(Avg_St2_time, 2)}")
    print(f"Average time spent to fuel car on Stations = {round(Avg_St_time, 2)}")

    # N10
    # Sums of aLl car time on station / experiment's time
    Avg_car_time = sum([x['2'] - x['14'][0] for x in Cars if '2' in x.keys()] + [x['0'] - x['14'][0] for x in Cars if
                                                                                 '0' in x.keys()]) / CarCount
    print(f"Average time spent on station = {round(Avg_car_time, 2)}")

    ig, ax = plt.subplots()
    # ax.plot(range(10))
    ax.set_yticks([0, 2, 4, 6, 8, 10, 12, 14], labels=['Отказ', 'Обсл', 'МО3', 'МО2', 'МО1', 'КО2', 'КО1', 'ГЗ'])
    # rangeXticks = round(max(Car_arriveMu)) + 2
    # print(rangeXticks)
    # ax.set_xticks([x for x in range(rangeXticks)])

    for car in Cars:
        Xlist = []
        Ylist = []
        for key in car.keys():
            if key != "2" and key != "0":
                Xlist.append(car[key][0])
                Ylist.append(int(key))
                Xlist.append(car[key][1])
                Ylist.append(int(key))
            else:
                Xlist.append(car[key])
                Ylist.append(int(key))

        ax.plot(Xlist, Ylist)

    ax.grid(True, ls='--', )
    ax.set_ylim(0, 15)
    ax.set_xlim(0, round(Exp_time + 0.5, 0))

    plt.show()