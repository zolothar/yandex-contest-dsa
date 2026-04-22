def main():
    elements_count = int(input())
    data = input().split()
    previouse = data[0]
    result = list()
    result.append(previouse)
    dashes = list()
    for i in range(1, elements_count):
        if data[i] != previouse:
            result.append(data[i])
        else:
            dashes.append('_')
        previouse = data[i]
    list.extend(result, dashes)
    print(*result, sep=' ')


if __name__ == '__main__':
    main()
