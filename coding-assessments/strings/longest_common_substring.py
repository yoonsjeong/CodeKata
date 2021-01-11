str1 = "abchellozzzzxyzabc"
str2 = "zzzzxyzhelloxyz"

def cmn_substr(str1, str2):
  n1 = len(str1)
  n2 = len(str2)
  dp = [[None]*n2 for _ in range(n1)]
  
  max_len = 0
  for i in range(n1):
    for j in range(n2):
      if str1[i] != str2[j]:
        dp[i][j] = 0
      else:
        if i-1 >= 0 and j-1 >= 0:
          dp[i][j] = dp[i-1][j-1] + 1
        else:
          dp[i][j] = 1
        
        if dp[i][j] > max_len:
          max_len = dp[i][j]
          ret = str1[i-max_len+1:i+1]        
  return ret

out = cmn_substr(str1, str2)
print(out)
