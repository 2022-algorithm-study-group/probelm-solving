def create_all_problem_list():
    week = "week"
    url_header = "https://leetcode.com/problems/"
    file = open("generator/solved_problems.txt", "w")
    for i in range(1, 30):
        folder_name = str(i) + week
        try:
            f = open(folder_name + "/problemlist.md", "r")
            file.write("#" + str(i) + "week" + "\n")
            while True:
                line = f.readline()
                if not line:
                    break
                idx = line.find(url_header)
                if idx != -1:
                    line = line.strip()
                    if line[-1] == ")":
                        file.write(line[idx:-1] + "\n")
                    else:
                        file.write(line[idx:] + "\n")
        except:
            break

create_all_problem_list()