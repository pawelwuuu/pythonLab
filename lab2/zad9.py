def unique_permutations(elements: list):
    def backtrack(path, remaining, result, seen):
        if not remaining:
            perm_tuple = tuple(path)
            if perm_tuple not in seen:
                seen.add(perm_tuple)
                result.append(perm_tuple)
            return
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:], result, seen)
    
    result = []
    seen = set()
    backtrack([], elements, result, seen)
    return result

print(unique_permutations([1, 2, 2]))