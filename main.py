def selectSortReverse(lst):
    for i in range(len(lst)):
        max = lst[i]
        for j in range(i, len(lst)):
            if lst[j] > max:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


def bubbleSortReverse(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


def insertSortReverse(lst):
    for i in range(1, len(lst)):
        for j in range(0, i):
            if lst[j] <= lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


def main():
    # Ask the user for input
    userInput = input("Enter numbers to be sorted: ")
    userList = userInput.split()
    for i in range(len(userList)):
        userList[i] = eval(userList[i])

    # Use Selection, Insertion, and Bubble sort algorithms
    # and show results
    print("Selection sort = {}".format(selectSortReverse(userList)))
    print("Insertion sort = {}".format(insertSortReverse(userList)))
    print("Bubble sort = {}".format(bubbleSortReverse(userList)))


main()
