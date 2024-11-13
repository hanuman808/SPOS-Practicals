def fcfs_scheduling():
    processes = int(input("Enter the number of processes (up to 6): "))

    bt = [0] * processes  # Burst times
    wt = [0] * processes  # Waiting times
    tt = [0] * processes  # Turnaround times
    arrival_times = list(range(processes))  # Arrival times: 0, 1, 2, ..., processes-1

    print("Enter burst times:")
    for i in range(processes):
        bt[i] = int(input(f"Process {i + 1}: "))

    exit_times = [0] * processes
    for i in range(processes):
        if i == 0:
            exit_times[i] = arrival_times[i] + bt[i]
        else:
            exit_times[i] = max(arrival_times[i], exit_times[i - 1]) + bt[i]
        tt[i] = exit_times[i] - arrival_times[i]
        wt[i] = tt[i] - bt[i]

    total_wt = sum(wt)
    total_tt = sum(tt)

    print("\nProcess\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
    for i in range(processes):
        print(f"{i + 1:<7}\t{bt[i]:<12}\t{arrival_times[i]:<14}\t{wt[i]:<14}\t{tt[i]:<15}")

    print(f"\nAverage Waiting Time: {total_wt / processes:.2f}")
    print(f"Average Turnaround Time: {total_tt / processes:.2f}")

def main():
    while True:
        print("\nSelect Scheduling Algorithm:")
        print("1. FCFS")
        print("2. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            fcfs_scheduling()
        elif choice == 2:
            print("Exiting the program.")
            break  # Exit the loop
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()

#Enter your choice: 1
# Enter the number of processes (up to 6): 5
# Enter burst times:
# Process 1: 4
# Process 2: 3
# Process 3: 1
# Process 4: 2
# Process 5: 5

# Process  Burst Time      Arrival Time    Waiting Time    Turnaround Time
# 1       	   4               	0               	0               	4
# 2       	   3               	1               	3               	6
# 3       	   1               	2               	5               	6
# 4       	   2               	3               	5               	7
# 5       	   5               	4               	6               	11

# Average Waiting Time: 3.80
# Average Turnaround Time: 6.80