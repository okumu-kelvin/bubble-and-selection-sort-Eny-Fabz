import random
def selection_sort(yours):
    x = len(yours)
    for i in range(x):
        min_index = i
        for j in range(i+1, x):
            if yours[j] < yours[min_index]:
                min_index = j
        yours[i], yours[min_index] = yours[min_index], yours[i]
    return yours

if __name__ == '__main__':
    my_list = [i for i in range(1,25,2)]
    random.shuffle(my_list)

    print("My original shuffled list:", my_list)
    s_sorted_list = selection_sort(my_list.copy())
    print("Sorted list:", s_sorted_list)