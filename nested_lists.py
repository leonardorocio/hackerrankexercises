if __name__ == '__main__':
    new_lst = [[input(), float(input())] for _ in range(int(input()))]
    lows = sorted(new_lst, key = lambda x: x[1])
    nd_low = [[name,grade] for name, grade in lows if grade != lows[0][1]]
    names = [name for name, grade in nd_low if nd_low[0][1] == grade]
    print(*sorted(names), sep="\n")
