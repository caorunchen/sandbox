fo = open("channel_brkt_modal.fem")
ls = []
for line in fo:
    if "CQUAD4" in line[:6]:
        line_array=(line.split(" "))
        for i in range(line_array.count("")):
            line_array.remove("")
        ls.append(list(map(eval,line_array[1:3])))
cbeam_element_id = tuple(ls)
for i in range(len(cbeam_element_id)):
    if cbeam_element_id[i][0] == 37:
        print(cbeam_element_id[i][1])

