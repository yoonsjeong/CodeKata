def unique(arr):
  store = {}
  count = 0
  for i in arr:
    codon = list(i)
    codon.sort()
    codon = "".join(codon)
    if codon in store:
      continue
    else:
      store[codon] = True
      count += 1
  return count


arr = ["GAA", "AAG", "CAA"]
print(unique(arr))
