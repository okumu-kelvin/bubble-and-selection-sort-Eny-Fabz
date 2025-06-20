import random
def bubble_sort(mine):
    x = len(mine)
    for i in range(x):
        for j in range(0, x - i - 1):
            if mine[j] > mine[j + 1]:
                mine[j], mine[j + 1] = mine[j + 1], mine[j]
    return mine

if __name__ == '__main__':
    my_list = [i for i in range(1,25,2)]
    random.shuffle(my_list)

    print("My original shuffled list:", my_list)
    b_sorted_list = bubble_sort(my_list.copy())
    print("Sorted list:", b_sorted_list)