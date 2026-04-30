def main():
    data = input().split()
    target = int(input())

    left = 0
    right = len(data)
    while left < right:
        mid = left + (right - left) // 2
        if int(data[mid]) < target:
            left = mid + 1
        else:
            right = mid
    print(left)


if __name__ == '__main__':
    main()
