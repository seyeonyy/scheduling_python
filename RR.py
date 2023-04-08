import statistics

time_Quantum = [1, 2, 5, 10, 30]
for t in time_Quantum:

    process_list = [[10, 29, 3, 7, 12], [2, 1, 8, 4, 5]]

    for process in process_list:
        
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
        
        print("Time Quantum", t)
        print("Process | Arrival | Burst | Exit | Turn Around | Wait |")
        avg_wt = 0
        for p in sorted(completion):
            print("   ","P",p[0],"   |   ",p[1]," |    ",p[3]," |    ",p[4],"  |    ",p[5],"  |   ",p[6],"   |  ")
            avg_wt += p[6]
        print("Average Waiting Time: ", avg_wt/len(completion))



            



