# CPE 101-01
# LAB 9
# Name: Tyler Baxter
# Section: 03


def main():
    try:
        file = open('infile', 'r')
        open_file(file)
    except SyntaxError:
        print("Unable to open infile")
        exit()


def open_file(file):
    file_list = file.readlines()
    int_cnt = 0
    float_cnt = 0
    other_cnt = 0
    for i in file_list:
        file_list_all = i.split()
        for entry in file_list_all:
            if entry.isdigit():
                int_cnt += 1
            else:
                try:
                    float(entry)
                    float_cnt += 1
                except ValueError:
                    other_cnt += 1
    print("Ints: " + str(int_cnt))
    print("Floats: " + str(float_cnt))
    print("Other: " + str(other_cnt))


if __name__ == '__main__':
    main()
