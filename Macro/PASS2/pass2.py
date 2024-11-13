# Read input file
with open("input.txt", "r") as f:
    file = f.readlines()

# Initialize file handling
with open("mdt.txt", "w") as f:
    pass  # Just to create the file

with open("mnt.txt", "w") as mnt, open("mdt.txt", "w") as mdt, open("ic.txt", "w") as ic:
    pass  # Close them immediately after creation

mdpt = 1  # Initialize MDT pointer
ala = []
flag = 0

# Process the input file
with open("mdt.txt", "w") as mdt, open("mnt.txt", "w") as mnt, open("ic.txt", "w") as ic:
    for line in file:
        l = line.strip()  # Remove leading/trailing whitespace
        if l == "MACRO":
            flag = 1
        elif l == "MEND":
            mdt.write(l + "\n")
            mdpt += 1
            flag = 0
        elif flag == 1:
            mdt.write(l + "\n")
            temp = l.split()
            mnt.write(temp[0] + " " + str(mdpt) + "\n")
            ala = temp[1].split(",")  # Define ALA
            mdpt += 1
            flag += 1
        elif flag > 1:
            temp = l.split()
            if len(temp) < 2:
                continue  # Skip malformed lines

            part2 = temp[1].split(",")
            mdt.write(temp[0] + " ")
            buffer = ""
            for i in part2:
                for j in range(len(ala)):
                    t = ala[j].split("=")
                    if t[0] == i:
                        buffer += "#" + str(j) + ","
            mdt.write(buffer.rstrip(",") + "\n")
            mdpt += 1
        else:
            ic.write(line)

# Reopen files to read
with open("ic.txt", "r") as ic, open("mnt.txt", "r") as mnt, open("mdt.txt", "r") as mdt:
    i = ic.readlines()
    n = mnt.readlines()
    m = mdt.readlines()

# Generate output
with open("output.txt", "w") as f:
    for line in i:
        flag = 0
        temp = line.strip().split()
        if len(temp) < 2:
            f.write(line)  # Write the line directly if it doesn't match expected format
            continue

        for i2 in n:
            t = i2.split()
            if t[0] == temp[0]:
                flag = 1
                mdpt = int(t[1])
                break

        if flag == 1:
            ala = temp[1].split(",")
            flag += 1

        if flag > 1:
            lis = []
            for i2 in range(mdpt - 1, len(m)):
                st = m[i2].strip()
                if st == "MEND":
                    break
                else:
                    lis.append(st)

            ala2 = []
            for item in range(len(lis)):
                tmp = lis[item].split()
                if item == 0:
                    ala2 = tmp[1].split(",")
                if item > 0:
                    f.write(tmp[0] + " ")
                tmp_args = tmp[1].split(",")
                buffer = ""
                for k in tmp_args:
                    for ii in range(len(ala2)):
                        if k == "#" + str(ii):
                            if len(ala) < len(ala2):
                                for l in range(len(ala2)):
                                    aflag = 0
                                    if '=' in ala2[l]:
                                        aflag = 1
                                        ala2[l] = ala2[l].split("=")[1]
                                    else:
                                        ala2[l] = ala[l]
                                ala = ala2

                            h = ala[ii].split("=")
                            if len(h) == 2:
                                buffer += (h[1] + ",")
                            else:
                                buffer += (h[0] + ",")
                if item > 0:
                    f.write(buffer.rstrip(",") + "\n")
        elif flag == 0:
            f.write(line)
