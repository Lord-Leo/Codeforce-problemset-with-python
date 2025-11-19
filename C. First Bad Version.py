# Global variable to simulate the bad version
bad = 0

def isBadVersion(version: int) -> bool:
    return version >= bad

def firstBadVersion(n: int) -> int:
    left, right = 1, n #start index , last index
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == "__main__":
    n = int(input("Enter total versions: "))
    bad = int(input("Enter first bad version: "))
    print(f"The first bad version is: {firstBadVersion(n)}")