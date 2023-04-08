import statistics
from queue import PriorityQueue

process_list = [[10, 29, 3, 7, 12], [2, 1, 8, 4, 5]]
priority_list = [[5, 1, 3, 4, 2], [2, 1, 4, 2, 3]]

que = PriorityQueue()

for process, priority in zip(process_list, priority_list):

    for i in range(len(process)):
        que.put((priority[i], process[i], i+1))

    AT = []
    BT = []
    ET = []
    TAT = []
    WT = []

    process_priority = []
    process_number = []

    while not que.empty():
        pri, pro, number = que.get()
        process_priority.append(pro)
        process_number.append(number)

    arrival_time = 0
    exit_time = 0

    for p in process_priority:
        # 도착 시간
        AT.append(arrival_time)

        # 실행 시간q
        BT.append(p)
        exit_time += p

        # 종료 시간
        ET.append(exit_time)

        # 프로세스 종료 시간
        TAT.append(exit_time - arrival_time)

        # 대기 시간
        WT.append(exit_time - arrival_time - p)


    print("Process | Arrival | Burst | Exit | Turn Around | Wait |")
    for i in range(len(process)):
        print("   ","P",process_number[i],"   |   ",AT[i]," |    ",BT[i]," |    ",ET[i],"  |    ",TAT[i],"  |   ",WT[i],"   |  ")
    print("Average Waiting Time: ", statistics.mean(WT))
