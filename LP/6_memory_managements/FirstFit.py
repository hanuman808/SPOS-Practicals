class FirstFit:
    def firstFit(self, blockSize, processSize):
        m = len(blockSize)
        n = len(processSize)
        allocation = [-1] * n

        for i in range(n):
            for j in range(m):
                if blockSize[j] >= processSize[i]:
                    allocation[i] = j
                    blockSize[j] -= processSize[i]
                    break

        print("\nProcess No.\tProcess Size\tBlock no.")
        for i in range(n):
            print(f"{i + 1}\t\t{processSize[i]}\t\t", end="")
            if allocation[i] != -1:
                print(allocation[i] + 1)
            else:
                print("Not Allocated")

def main():
    first = FirstFit()

    while True:
        print("\nEnter the number of Blocks: ")
        m = int(input())
        print("Enter the number of Processes: ")
        n = int(input())

        blockSize = list(map(int, input("Enter the Size of all the blocks (space-separated): ").split()))
        processSize = list(map(int, input("Enter the Size of all the processes (space-separated): ").split()))

        print("\nMenu")
        print("1. First Fit")
        print("2. Exit")
        choice = int(input("Select the algorithm you want to implement: "))

        if choice == 1:
            print("First Fit Output")
            first.firstFit(blockSize[:], processSize)  # Pass a copy to avoid modifying the original list
        elif choice == 2:
            print("Exiting the code...")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
# Enter the number of Blocks:
# 5
# Enter the number of Processes:
# 4
# Enter the Size of all the blocks (space-separated): 100 500 200 300 600
# Enter the Size of all the processes (space-separated): 212 417 112 426

# Menu
# 1. First Fit
# 2. Next Fit
# 3. Worst Fit
# 4. Best Fit
# 5. Exit
# Select the algorithm you want to implement: 1
# First Fit Output

# Process No.     Process Size    Block no.
# 1               	212            	 2
# 2               	417             	 5
# 3               	112             	 3
# 4               	426             Not Allocated
