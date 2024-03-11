/*
 * @param {number[]} nums
 * @return {number[][]}
var threeSum = function(nums) { 
};
*/

/*
inputs: array of nums
outputs: an array of arrays where the numbers within the array returned are going to equal to 0.

Work on eliminating the first number to then simplify down to the 2 sum approach
sort the array. 
Loop the array. 
If there is a duplicate, if the 1st index is the same as the 0th index, continue through the loop

Use two pointer approach like in 2 sum
 */
function threeSum(nums) {
    const results = [];
    //sort the array so that we can quickly find dupes
    nums.sort((a, b) => a - b); // Correct sorting
    //for loop through the array of numbers. start at 0th index, go until the 3rd to last index in the array and iterate by 1 each loop
    for (let i = 0; i < nums.length - 2; i++) {
        // if Skip duplicate values for the first number
        const leftNeighbor = nums[i - 1];
        const current = nums[i];
        if (i > 0 && current === leftNeighbor) continue;

        let leftPtr = i + 1;
        let rightPtr = nums.length - 1;

        while (leftPtr < rightPtr) {
            const sum = current + nums[leftPtr] + nums[rightPtr];
            if (sum === 0) {
                results.push([current, nums[leftPtr], nums[rightPtr]]);
                leftPtr++;
                rightPtr--;

                // Skip duplicate values for the second and third numbers
                while (leftPtr < rightPtr && nums[leftPtr] === nums[leftPtr - 1]) leftPtr++;
                while (leftPtr < rightPtr && nums[rightPtr] === nums[rightPtr + 1]) rightPtr--;
            } else if (sum < 0) {
                leftPtr++;
            } else {
                rightPtr--;
            }
        }
    }

    return results;
}
