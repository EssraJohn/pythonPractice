# hashing  immutable object like tuple

if __name__ == '__main__':
    n = int(input("Enter integer: "))
    integer_list = map(int, input("enter: ").split())
    print(list(integer_list))
    t = tuple(integer_list)
    hash_val = hash(t)
    print(hash_val)
