def medians(nums1, nums2):
    a = []
    a = nums1 + nums2
    a1 = sorted(a)
    b = len(a1)
    # если это нулевые списки, значит где-то закралась ошибка
    if b == 0:
        print('бегом переделывать')
    # теперь проверим длину списка
    elif b % 2 == 1:
        m = a1[b // 2]
    elif b % 2 == 0:
        m = (a1[b // 2 ] + a1[b // 2 - 1]) / 2
    # выведем результат
    print(m)


if __name__ == "__main__":
    nums1, nums2 =  [5, 5], [4, 4]
    medians(nums1, nums2)
