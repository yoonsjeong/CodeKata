const rob_rec = (nums: number[], i: number) => {
  if (i < 0) return 0;
  return Math.max(rob_rec(nums, i - 2) + nums[i], rob_rec(nums, i - 1));
};

// figure out what houses to rob to maximize stash
function rob(nums: number[]): number {
  return rob_rec(nums, nums.length - 1)
}

const nums = [2,7,9,3,1]
const out = rob(nums);
console.log(out);