/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
     // Initialize the search range for k. Start with 1 as the minimum possible speed.
    let left = 1;
    
    // The maximum possible speed could be eating the largest pile in one hour, so we find the largest number in piles.
    let right = Math.max(...piles);

    // Use a binary search to find the minimum speed. 
    // Continue the loop until left > right is false, meaning we've narrowed down to the minimum possible speed.
    while (left <= right) {
        // Calculate the mid-point of the current range as a candidate for the minimum speed.
        // Math.floor is used to ensure we have an integer value for the speed.
        let k = Math.floor((left + right) / 2);

        // Initialize a variable to count the total hours needed to eat all bananas at speed k.
        let hours = 0;

        // Calculate the total hours needed with the current speed k.
        for (let pile of piles) { // Iterate over each pile in piles.
            // For each pile, calculate the hours needed and add it to the total hours.
            // Math.ceil is used because if a pile is not fully eaten in an hour, it still counts as a full hour.
            hours += Math.ceil(pile / k);
        }

        // If the total hours is less than or equal to h, the current speed k is fast enough.
        // However, there might be a slower speed that also works, so we try to find the minimum.
        if (hours <= h) {
            right = k - 1; // Narrow down the search to the left half by adjusting the right boundary.
        } else {
            // If the total hours is more than h, the current speed is too slow.
            // We need to try a faster speed, so we adjust the left boundary.
            left = k + 1;
        }
    }

    // After exiting the loop, left is the minimum speed k that allows Koko to finish eating within h hours.
    return left;
};

/* Initialize the search range: left = 1 and right = max(piles).
While left < right, do:
    Calculate mid as the average of left and right (this is the proposed speed k).
    Calculate the total hours totalHours required to eat all bananas at speed k.
    If totalHours > h, the speed is too slow, so we need to increase it. Set left = mid + 1.
    Otherwise, the speed is fast enough, but we check if we can do better (slower but still within time). 
    Set right = mid.
Result: After the loop, left will be the minimum speed that allows Koko to eat all bananas within h hours.*/



