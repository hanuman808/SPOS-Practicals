def print_frame_table(table, noofpages, capacity):
    print("\n----------------------------------------------------------------------")
    for i in range(capacity):
        for j in range(noofpages):
            if table[j][i] == -1:
                print("   -  ", end="")
            else:
                print(f"{table[j][i]:5d} ", end="")
        print()
    print("----------------------------------------------------------------------")


def optimal_page_replacement(noofpages, pages, capacity):
    frame = [-1] * capacity
    table = [[-1] * capacity for _ in range(noofpages)]

    hit, fault, ptr = 0, 0, 0
    is_full = False

    print("\n----------------------------------------------------------------------")
    for i in range(noofpages):
        search = -1
        for j in range(capacity):
            if frame[j] == pages[i]:
                search = j
                hit += 1
                print("  H  ", end="")
                break

        if search == -1:
            if is_full:
                index = [None] * capacity
                for j in range(i + 1, noofpages):
                    for k in range(capacity):
                        if pages[j] == frame[k] and index[k] is None:
                            index[k] = j
                            break

                max_index = -1
                ptr = -1
                for j in range(capacity):
                    if index[j] is None:
                        ptr = j
                        break
                    elif index[j] > max_index:
                        max_index = index[j]
                        ptr = j

            frame[ptr] = pages[i]
            fault += 1
            print("  F  ", end="")

            if not is_full:
                ptr += 1
                if ptr == capacity:
                    ptr = 0
                    is_full = True

        for j in range(capacity):
            table[i][j] = frame[j]

    print("\n----------------------------------------------------------------------")
    print_frame_table(table, noofpages, capacity)

    hit_ratio = (hit / noofpages) * 100
    fault_ratio = (fault / noofpages) * 100
    print(f"Page Fault: {fault}\nPage Hit: {hit}")
    print(f"Hit Ratio: {hit_ratio:.2f}% \nFault Ratio: {fault_ratio:.2f}%")


# Function to choose algorithm based on user choice
def page_replacement_simulation():
    while True:
        print("\n1. Optimal Page Replacement")
        print("2. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 2:
            print("Exiting program.")
            break

        noofpages = int(input("Enter the number of pages you want to enter: "))
        pages = list(map(int, input("Enter the pages (space-separated): ").split()))
        capacity = int(input("Enter the capacity of frame: "))

        if choice == 1:
            optimal_page_replacement(noofpages, pages, capacity)
        else:
            print("Invalid choice, please select again.")

# Run the function with switch cases
page_replacement_simulation()

# Enter your choice: 3
# Enter the number of pages you want to enter: 20        
# Enter the pages (space-separated): 1 2 3 4 2 1 5 6 2 1 2 3 7 6 3 2 1 3 3 6 
# Enter the capacity of frame: 3

# ----------------------------------------------------------------------------------------------------------
#    F     F    F     F     H    H    F    F     H     H    H    F    F    H     H    F    F     H    H    H
# ----------------------------------------------------------------------------------------------------------
#    1     1     1     1     1     1     1     1     1     1     1     3     3     3     3     3     3     3     3     3
#    -      2     2     2     2     2     2     2     2     2     2     2     7     7     7     2     1     1     1     1
#    -     -      3     4     4     4     5     6     6     6     6     6     6     6     6     6     6     6     6     6
# ----------------------------------------------------------------------------------------------------------

# Page Fault: 10
# Page Hit: 10
# Hit Ratio: 50.00%
# Fault Ratio: 50.00%