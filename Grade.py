def gts():
    li = []
    while True:
        a = input("Write \"Done\" if you are finished\nPlease Enter students name:")
        if a == "Done":
            print("The sheet is ready")
            break
        b = int(input("Enter scores:"))
        if b >= 50:
            pas = "Pass"
        else:
            pas = "Fail"
        li.append([a,b,pas])
    return li
def calc_avg(li):
    total = 0
    for av in li:
        total = total +av[1]
    avg = total / len(li)
    return avg
def excel(li):
    import openpyxl
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Name","Scores","Result"])
    for stud in li:
        ws.append(stud)
    wb.save("Student Result.xlsx")
    return wb
def main():
    res = gts()
    excel(res)
    avg = calc_avg(res)
    print("Class average:", avg)

main()