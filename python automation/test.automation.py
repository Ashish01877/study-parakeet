finput = input("Enter the file name: ")

if finput == 'na na boo boo or easter eggs':
    print("NA NA BOO BOO TO YOU, you've been punked ! LOL")

else:
    try:
        fopen = open(finput, "r", encoding="utf-8")
    except:
        print("File cannot be read:", finput)
        exit()

    count = 0
    for line in fopen:
        count += 1

    print("There were total", count, "lines")
