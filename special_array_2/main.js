/**
 * @param {number} x
 * @return {boolean}
 */
const isEven = (x) => x%2==0;

/**
 * @param {boolean} x
 * @return {boolean}
 */
const isInvalid = (x) => x===false;

/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var isArraySpecial = function(nums, queries){
  const result = [];
  const memo = Array(nums.length).fill(true);


  for(let query of queries){
    [start, end] = query;
    let allDifferentParity = true;

        
    const memoValues = memo.slice(start, end+1);
    if(memoValues.some(isInvalid)){
      result.push(false);
      continue;
    }

    const selectedOnes = nums.slice(start, end+1);

    for(let i = 0; i < selectedOnes.length-1; i++) {
      const curr = selectedOnes[i];
      const next = selectedOnes[i+1];

      const sameParity = isEven(curr) == isEven(next);
      if(sameParity){
        memo[i] = false;
        allDifferentParity = false;
        break;
      }
    }
    result.push(allDifferentParity);
  }

  return result;
};

console.assert(isArraySpecial([3,4,1,2,6], [[0,4]])[0] == false, "Failed #1")
console.assert(isArraySpecial([4,3,1,6], [[0,2],[2,3]])[0] == false, "Failed #2-1")
console.assert(isArraySpecial([4,3,1,6], [[0,2],[2,3]])[1] == true, "Failed #2-2")
