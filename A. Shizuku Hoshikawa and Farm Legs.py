def combinations(n):
    count = 0
    for cows in range(0, n // 4 + 1):
        remaining_legs = n - cows * 4
        if remaining_legs % 2 == 0:
            count += 1
    return count

if __name__ == "__main__":  #its kind of like int main() in cpp
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(combinations(n))
