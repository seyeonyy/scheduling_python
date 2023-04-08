import statistics

process_list = [[10, 29, 3, 7, 12], [2, 1, 8, 4, 5]]

for process in process_list:

    process_number = sorted(range(len(process)), key=lambda k: process[k])
    process = sorted(process)
    arrival_time = 0

    AT = [0 for i in range(len(process))]
    BT = []
    ET = []
    TAT = []
    WT = []

    exit_time = 0

    for p in process:

        # 실행 시간
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
        print("   ","P",process_number[i]+1,"   |   ",AT[i]," |    ",BT[i]," |    ",ET[i],"  |    ",TAT[i],"  |   ",WT[i],"   |  ")
    print("Average Waiting Time: ", statistics.mean(WT))
