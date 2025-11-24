def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True)

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