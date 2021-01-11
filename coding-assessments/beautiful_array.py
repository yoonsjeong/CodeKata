def permute(nums):
    ans = [[]]

    for n in nums:
        new_ans = []
        for a in ans:
            alen = len(a)
            for i in range(alen+1):
                new_ans.append(a[:i] + [n] + a[i:])
                if i < len(a) and a[i] == n:
                    break
        ans = new_ans
    # print("ans:", ans)
    return ans


def is_beautiful_array(arr):
    n = len(arr)
    for i in range(n):
        start = arr[i]
        for j in range(i+1, n-1):
            middle = arr[j]
            for k in range(j+1, n):
                end = arr[k]
                if start + end == middle * 2:
                    return False
                else:
                    continue
    return True


def gen_beautiful(to):
    ps = permute(list(range(1, to+1)))
    # is_beautiful_array([3,1,2,5,4])
    ps_beautiful = list(filter(is_beautiful_array, ps))
    # print("PERMUTATIONS:", ps)
    # print("BEAUTIFUL ARRAYS:", ps_beautiful)
    return ps_beautiful


def helper(arr):
    n = len(arr)
    if n == 1: return arr
    even_indices = []
    odds_indices = []
    for i in range(n):
        if i % 2 == 0:
            even_indices.append(arr[i])
        else:
            odds_indices.append(arr[i])
    return helper(even_indices) + helper(odds_indices)


def ret_beautiful(N):
    arr = list(range(1, N+1))
    return helper(arr)


# for i in range(1,10):
i = 8
# num = gen_beautiful(i)
# print("({0}, {1})".format(i, len(num)))
print("Range:", i)
# print("Number of Beautiful Arrays:", (num))
# iswhat = is_beautiful_array([2,4,6,1,3,5])
is_b = ret_beautiful(10)
is_t = is_beautiful_array(is_b)
print("Here is array:", is_b)
print("Is it?", is_t)
