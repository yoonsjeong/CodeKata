
var fourSumCount = function (A, B, C, D) {
  let counter = new Map()
  for (a of A) {
    for (b of B) {
      const sum = a+b;
      counter.set(sum, counter.get(sum) + 1 || 1)
    }
  }

  let count = 0
  for (c of C) {
    for (d of D) {
      const sum = c+d;
      count += counter.get(-sum) || 0
    }
  }
  return count;
};
