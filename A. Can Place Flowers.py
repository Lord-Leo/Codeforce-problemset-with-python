def canPlaceFlowers(fb, n):
    m = len(fb)

    for i in range(m):
        if n == 0:
            return True

        if fb[i] == 0:
            empty_left = (i == 0 or fb[i - 1] == 0)
            empty_right = (i == m - 1 or fb[i + 1] == 0)

            if empty_left and empty_right:
                fb[i] = 1
                n -= 1

    return n == 0


if __name__ == "__main__":
    size = int(input())
    fb = list(map(int, input().split()))
    n = int(input())

    result = canPlaceFlowers(fb, n)

    print("true" if result else "false")