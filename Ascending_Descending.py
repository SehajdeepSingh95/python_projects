total_numbers=int(input("Please enter how many numbers you wanna sort: "))
NumberList  = []
j=0
order=input("in which order do you wanna sort, ascending or descending: ")
if order.lower()=="ascending" or order.lower() == "ascendings":
    while len(NumberList) <= total_numbers - 1:
        i = int(input("Please enter the number"))
        NumberList.insert(j, i)
        j = j + 1

    NumberList.sort()
    print(NumberList)
elif order.lower() == "descending" or order.lower() == "descendings":
        while len(NumberList) <= total_numbers - 1:
            i = int(input("Please enter the number"))
            NumberList.insert(j, i)
            j = j + 1

         NumberList.sort(reverse=True)
        #OR
        # NumberList.sort()
        # NumberList.reverse()
        numberlist=str(NumberList)
        print(numberlist)
else:
    print("Only inputs ascending and descending are allowed")

