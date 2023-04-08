import statistics
import matplotlib.pyplot as plt
import numpy as np
from queue import PriorityQueue

avg = []

# fcfs
process_list = [[10, 29, 3, 7, 12], [2, 1, 8, 4, 5]]

avg_set1 = []
avg_set2 = []

for idx, process in enumerate(process_list):
    AT = []
    BT = []
    ET = []
    TAT = []
    WT = []

    arrival_time = 0
    exit_time = 0

    for p in process:
        # 도착 시간
        AT.append(arrival_time)

        # 실행 시간
        BT.append(p)
        exit_time += p

        # 종료 시간
        ET.append(exit_time)

        # 프로세스 종료 시간
        TAT.append(exit_time - arrival_time)

        # 대기 시간
        WT.append(exit_time - arrival_time - p)
    
    if idx % 2 == 0:
        avg_set1.append(statistics.mean(WT))
    else:
        avg_set2.append(statistics.mean(WT))
# rr
time_Quantum = [1, 2, 5, 10, 30]
for t in time_Quantum:

    process_list = [[10, 29, 3, 7, 12], [2, 1, 8, 4, 5]]

    for idxe, process in enumerate(process_list):
        
        ready = []

        for idx, p in enumerate(process):
            ready.append([idx+1, 0, p, 0, -1])

        now = 0
        completion = []

        while ready:

            if ready[0][2] > t:
                ready[0][2] -= t
                ready[0][3] += t
                ready.append(ready.pop(0))
                now += t
            
            else:
                now += ready[0][2]
                ready[0][3] += ready[0][2]
                ready[0][2] = 0
                ready[0][4] = now
                ready[0].append(ready[0][4] - ready[0][1])
                ready[0].append(ready[0][5] - ready[0][3])
                completion.append(ready.pop(0))
        
        avg_wt = 0
        for p in sorted(completion):
            avg_wt += p[6]
        
        if idxe % 2 == 0:
            avg_set1.append(avg_wt/len(completion))
        else:
            avg_set2.append(avg_wt/len(completion))

print(len(avg_set1), len(avg_set2))

# sjf
process_list = [[10, 29, 3, 7, 12], [2, 1, 8, 4, 5]]

for idx, process in enumerate(process_list):

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
    
    if idx % 2 == 0:
        avg_set1.append(statistics.mean(WT))
    else:
        avg_set2.append(statistics.mean(WT))

# Priority
process_list = [[10, 29, 3, 7, 12], [2, 1, 8, 4, 5]]
priority_list = [[5, 1, 3, 4, 2], [2, 1, 4, 2, 3]]

que = PriorityQueue()

for idx, (process, priority) in enumerate(zip(process_list, priority_list)):

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

        # 실행 시간
        BT.append(p)
        exit_time += p

        # 종료 시간
        ET.append(exit_time)

        # 프로세스 종료 시간
        TAT.append(exit_time - arrival_time)

        # 대기 시간
        WT.append(exit_time - arrival_time - p)
    
    if idx % 2 == 0:
        avg_set1.append(statistics.mean(WT))
    else:
        avg_set2.append(statistics.mean(WT))

x = np.arange(len(avg_set1))
print(avg_set1)
p_name = ["fcfs", "rr_t1", "rr_t2", "rr_t5", "rr_t10", "rr_t30", "sjf", 'priority']
plt.bar(x, avg_set1)
plt.xticks(x, p_name)

plt.show()

x = np.arange(len(avg_set2))
p_name = ["fcfs", "rr_t1", "rr_t2", "rr_t5", "rr_t10", "rr_t30", "sjf", 'priority']
plt.bar(x, avg_set2)
plt.xticks(x, p_name)

plt.show()
