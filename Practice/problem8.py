if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    p = max(arr)
    while p in arr:
        arr.remove(p)
    print(max(arr))
