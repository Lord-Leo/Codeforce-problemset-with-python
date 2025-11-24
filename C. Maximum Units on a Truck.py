def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True)#timsort
#here "key" tells pythone how i want to arrange the elements and "reverse" is descending or ascending
#lamda is a unnamed function used in sort and i can teach lamda which element to compare to sort
    totalUnits = 0

    for numberOfBoxes, unitsPerBox in boxTypes:
        if truckSize == 0:
            break

        take = min(numberOfBoxes, truckSize)
        totalUnits += take * unitsPerBox
        truckSize -= take

    return totalUnits


if __name__ == "__main__":
    n, truckSize = map(int, input().split())

    boxTypes = []
    for _ in range(n):
        a, b = map(int, input().split())
        boxTypes.append([a, b]) #append- means how it would look in the code


    print(maximumUnits(boxTypes, truckSize))
