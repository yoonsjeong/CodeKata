def permute(nums):
    ans = [[]]

    for n in nums:
        new_ans = []
        for a in ans:
            alen = len(a)
            for i in range(alen+1):
                new_ans.append(a[:i] + [n] + a[i:])
                if i < len(a) and a[i] == n: break
        ans = new_ans
        print("ans:", ans)
    return ans


output = permute([1, 1, 3])
print(output)

# expect [[1,1,2],[1,2,1],[2,1,1]]
