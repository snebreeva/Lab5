nums1, nums2 = [9, 5 , 789, 786, 787, 788], [] 

def medians(nums1, nums2):
    newnums = nums1 + nums2
    newnums = sorted(newnums)
    
    if len(newnums) == 0:
        print('ну ты шо а')
        
    elif len(newnums) == 1:
        a = newnums[0]
        print(a)
        
    elif len(newnums) % 2 == 1:
        c = newnums[len(newnums) // 2]
        print(f'объединенный список = {newnums}, медиана {c}.')        
        
    elif len(newnums) % 2 == 0:
        b1 = newnums[len(newnums) // 2 - 1]
        b2 = newnums[len(newnums) // 2]
        b = (b1 + b2) / 2
        print(f'объединенный список = {newnums}, медиана ({b1} + {b2}) / 2 = {b}.')


if __name__ == "__main__":
    medians(nums1, nums2)
