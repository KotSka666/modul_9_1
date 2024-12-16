def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

if __name__ == "__main__":
    result_1 = apply_all_func([6, 20, 15, 9], max, min)
    print(result_1)

    result_2 = apply_all_func([6, 20, 15, 9], len, sum, sorted)
    print(result_2)

