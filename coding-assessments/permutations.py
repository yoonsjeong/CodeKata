def sort_seq(seq):
  arr = [s for s in seq]
  arr.sort()
  return "".join(arr)

"""
Given strings representing genes, determine 
how many unique sequences there are, accounting for rotations. 
For example, given AAG, GAA, and CAA, there are two unique sequences, 
because GAA can be rotated to AAG.
"""
def unique_seq(seqs):
  store = {}
  count = 0
  for seq in seqs:
    check = sort_seq(seq)
    if check in store:
      continue
    else:
      store[check] = True
      count += 1
  return count


seqs = ["AAG", "GAA", "CAA", "AAC", "ACA", "AGA"]
output = unique_seq(seqs)
print(output)

