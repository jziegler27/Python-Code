def digOrDict(op, dic):
    if op[0] == "-" and op[1].isdigit() or op[0].isdigit():
        return int(op)
    else:
        return dic[op]


def main():
    import sys
    filein = open(sys.argv[1])
    code_string = ""
    list_of_strings = []
    white_space_check = []
    label_dic = {}
    y = 0
    x = 0
    for line in filein:
        list_of_strings = code_string.upper().splitlines()
        white_space_check = code_string.upper().splitlines()
        if line.find("#") != -1:
            code_string += (line[0: line.index("#")-1:] + "\n").upper()
        else:
            code_string += line
    for i in range(0, len(list_of_strings)):
        list_of_strings[i] = list_of_strings[i].split()
        if not white_space_check[i][0].isspace():
            label_dic[f"{list_of_strings[i][0]}"] = i
            list_of_strings[i].remove(f"{list_of_strings[i][0]}")
    i = 0
    halt = False
    while i < len(list_of_strings) and halt is False:
        for j in range(0, len(list_of_strings[i])):
            if x > 32 or y > 32:
                halt = True
                print(f"{list_of_strings[i-1][j]} to ({x},{y}): = Out of bounds error")
            elif list_of_strings[i][j] == "YMOVE":
                y += digOrDict(list_of_strings[i][j+1], label_dic)
                i += 1
            elif list_of_strings[i][j] == "XMOVE":
                x += digOrDict(list_of_strings[i][j+1], label_dic)
                i += 1
            elif list_of_strings[i][j] == "PRINTLOC":
                print(x, y)
                i += 1
            elif list_of_strings[i][j] == "IF":
                if list_of_strings[i][j+2] == "<" and digOrDict(list_of_strings[i][j+1], label_dic) < digOrDict(list_of_strings[i][j+3], label_dic):
                    i = label_dic[f"{list_of_strings[i][j+4]}"]
                elif list_of_strings[i][j + 2] == ">" and digOrDict(list_of_strings[i][j + 1], label_dic) > digOrDict(list_of_strings[i][j + 3], label_dic):
                    i = label_dic[f"{list_of_strings[i][j + 4]}"]
                elif list_of_strings[i][j + 2] == "==" and digOrDict(list_of_strings[i][j + 1], label_dic) == digOrDict(list_of_strings[i][j + 3], label_dic):
                    i = label_dic[f"{list_of_strings[i][j + 4]}"]
                elif list_of_strings[i][j + 2] == "!=" and digOrDict(list_of_strings[i][j + 1], label_dic) != digOrDict(list_of_strings[i][j + 3], label_dic):
                    i = label_dic[f"{list_of_strings[i][j + 4]}"]
                else:
                    i += 1

            elif list_of_strings[i][j] == "GOTO":
                i = label_dic[f"{list_of_strings[i][j+1]}"]
                break
            elif list_of_strings[i][j] == "SET":
                label_dic[f"{list_of_strings[i][j+1]}"] = digOrDict(list_of_strings[i][j+2],label_dic)
                i += 1
                break
            elif list_of_strings[i][j] == "ADD":
                label_dic[f"{list_of_strings[i][j+1]}"] += digOrDict(list_of_strings[i][j+2], label_dic)
                i += 1
                break
            elif list_of_strings[i][j] == "SUB":
                label_dic[f"{list_of_strings[i][j + 1]}"] -= digOrDict(list_of_strings[i][j + 2], label_dic)
                i += 1
                break
            elif list_of_strings[i][j] == "HALT":
                halt = True
                break

            break


if __name__ == "__main__":
    main()

