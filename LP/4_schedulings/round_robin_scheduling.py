def round_robin_scheduling():
    processes = int(input("Enter the number of processes: "))
    quantum = int(input("Enter the quantum time: "))
    at = [0] * processes  
    bt = [0] * processes  
    rem_bt = [0] * processes  

    print("Enter the arrival times:")
    for i in range(processes):
        at[i] = int(input(f"Process {i + 1} arrival time: "))

    print("Enter the burst times:")
    for i in range(processes):
        bt[i] = int(input(f"Process {i + 1} burst time: "))
        rem_bt[i] = bt[i]  

    wt = [0] * processes
    ct = [0] * processes
    tt = [0] * processes
    t = 0
    complete = 0
    ready_queue = []
    arrived = [False] * processes

    while complete < processes:
        for i in range(processes):
            if at[i] <= t and not arrived[i]:
                ready_queue.append(i)
                arrived[i] = True

        if ready_queue:
            i = ready_queue.pop(0)
            if rem_bt[i] > quantum:
                t += quantum
                rem_bt[i] -= quantum
                for j in range(processes):
                    if at[j] <= t and not arrived[j]:
                        ready_queue.append(j)
                        arrived[j] = True
                ready_queue.append(i)
            else:
                t += rem_bt[i]
                rem_bt[i] = 0
                ct[i] = t
                tt[i] = ct[i] - at[i]
                wt[i] = tt[i] - bt[i]
                complete += 1
        else:
            t += 1  

    print("\nProcess\tArrival\tBurst\tCompletion\tWaiting\tTurnaround")
    for i in range(processes):
        print(f"P{i + 1}\t\t{at[i]}\t\t{bt[i]}\t\t{ct[i]}\t\t\t{wt[i]}\t\t{tt[i]}")

    total_wt = sum(wt)
    total_tt = sum(tt)
    print(f"\nAverage Waiting Time: {total_wt / processes:.2f}")
    print(f"Average Turnaround Time: {total_tt / processes:.2f}")

def main():
    while True:
        print("\nSelect Scheduling Algorithm:")
        print("1. Round Robin")
        print("2. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            round_robin_scheduling()
        elif choice == 2:
            print("Exiting the program.")
            break  # Exit the loop
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
# Enter your choice: 3
# Enter the number of processes: 4
# Enter the quantum time: 2
# Enter the arrival times:
# Process 1 arrival time: 0 
# Process 2 arrival time: 1
# Process 3 arrival time: 2
# Process 4 arrival time: 4
# Enter the burst times:
# Process 1 burst time: 5
# Process 2 burst time: 4
# Process 3 burst time: 2
# Process 4 burst time: 1

# Process    Arrival     Burst   Completion      Waiting    Turnaround
# P1              0               5               12                      7               12
# P2              1               4               11                      6               10
# P3              2               2               6                       2               4
# P4              4               1               9                       4               5

# Average Waiting Time: 4.75
# Average Turnaround Time: 7.75