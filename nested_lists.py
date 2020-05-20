if __name__ == '__main__':
    new_list = new_test = names = []
    for _ in range(int(input())):
        names = input()
        scores = float(input())
        new_list.append([names,scores])
    new_list.sort()
    for i in new_list:
        for j in range(1,len(i)):
            new_test.append(i[j])
    minimun = min(new_test)
    while minimun in new_test:
        new_test.remove(minimun)
    for i in new_list:
        if min(new_test) in i:
            names.append(i[0])
    print(*names,sep = "\n")
