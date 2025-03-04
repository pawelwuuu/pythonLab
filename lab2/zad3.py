def longest_increasing_subsequence(sequence: list[int]):
    maxx = 1
    
    curr_max = 2
    for i in range(len(sequence) - 1):
        a = sequence[i]
        b = sequence[i+1]
        if a < b:
            curr_max += 1
        else:
            if curr_max > maxx:
                maxx = curr_max
            curr_max = 2
    
    if curr_max > maxx:
        return curr_max
    
    return maxx


print(longest_increasing_subsequence([10,12,134,15,1,12,-13,-14,15,16,17,18]))
        
    