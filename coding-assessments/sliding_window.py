def checkInclusion(s1, s2):
  n1 = len(s1)
  n2 = len(s2)
  if n1 > n2: return False

  count = [0]*26
  for i in range(n1):
    count[ord(s1[i]) - ord("a")] += 1
    count[ord(s2[i]) - ord("a")] -= 1
  
  if allZero(count): return True

  for i in range(n1, n2):
    count[ord(s2[i]) - ord("a")] -= 1
    count[ord(s2[i] - n1) - ord("a")] += 1
    if allZero(count): return True

  return False

def allZero(arr):
  for i in arr:
    if i != 0:
      return False
  return True

x = checkInclusion("ab", "bcatman")
print(x)