def quick_sort(lst):
    low = []
    high = []

    try:
        pivot = lst[0]
        for i in lst[1:]:
            high.append(i) if i > pivot else low.append(i)
        return quick_sort(low) + [pivot] + quick_sort(high)
    except IndexError:
        return []

if __name__ == "__main__":
    import timeit
    from random import randint
    times = 500

    def test1():
        quick_sort([2, 1])

    def test2():
        quick_sort([randint(0, 1000000) for i in range(1000)])

    avg_time = timeit.Timer(test1).timeit(times)
    avg_time_big = timeit.Timer(test2).timeit(times)

    print("""Quick sort picks a point as a pivot and branches off both
        left and right.""")
    print()

    print("Input: [2, 1]")
    print("\tnumber of runs: {}".format(times))
    print("\taverage time  : {}".format(avg_time))
    print()
    print("Input: [randint(0, 1000000) for i in range(1000)]")
    print("\tnumber of runs: {}".format(times))
    print("\taverage time  : {}".format(avg_time_big))
