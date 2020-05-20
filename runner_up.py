if __name__ == '__main__':
    def remove_repetidos(lista):
        new_list = []
        for item in lista:
            if item not in new_list:
                new_list.append(item)
        return sorted(new_list)
    
    def imprime_runner_up():
        n = int(input())
        arr = map(int, input().split())
        arr = list(remove_repetidos(arr))
        for item in range(len(arr)):
            if arr[item] > 0:
                if arr[item] < arr[-1]:
                    runner_up = arr[item]
            else:
                if arr[item] < arr[-1]:
                    runner_up = arr[item]
        print(runner_up)

imprime_runner_up()



        
