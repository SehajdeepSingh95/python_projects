total_numbers=int(input("Please enter how many numbers you wanna sort: "))
NumberList  = []
j=0
order=input("in which order do you wanna sort, Ascending or Descending: ")
if(order.lower()=="ascending" or order.lower() == "ascending"):
    while (len(NumberList) <= total_numbers - 1):
        i = int(input("Please enter the number"))
        NumberList.insert(j, i)
        j = j + 1

    NumberList.sort()
    print(NumberList)
elif(order.lower() == "descending" or order.lower() == "descendings"):
        while (len(NumberList) <= total_numbers - 1):
            i = int(input("Please enter the number"))
            NumberList.insert(j, i)
            j = j + 1

        NumberList.sort()
        NumberList.reverse()
        print(NumberList)
else:
    print("Only inputs ascending and descending are allowed")

