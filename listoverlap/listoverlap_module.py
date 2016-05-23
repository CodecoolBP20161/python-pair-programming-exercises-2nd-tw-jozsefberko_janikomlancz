import random
def listoverlap(list1, list2):
    common_list = (set(list1) & set(list2))
    if len(common_list) == 0:
        common_list = "There are not any common number(s) in the lists!"
    return list(common_list)

def main():
    a = []
    b = []
    for i in range(random.randint(0, 11)):
        a.append(random.randint(0, 100))
        b.append(random.randint(0, 100))
    print("A list = %s\nB list = %s"%(a, b))
    print(listoverlap(a, b))
    return


if __name__ == '__main__':
    main()
