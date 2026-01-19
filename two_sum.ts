function twoSum(nums: number[], target: number){
    const numMap:any = {}
    const orderMap: any = {}
    for(let i = 0; i <nums.length; i++) {
        numMap[nums[i]] = target - nums[i];
        orderMap[i] = nums[i]
    }
    
    for(let i = 0; i < nums.length; i++) { 
        // i 는 인덱스 
        // ordermap[i] 에 넣으면 숫자가 나옴 
    }
};

// 반대로 인덱스가 키라면? 
// order map 에서 하나씩 탐색( order map 의 키는 nums 의 인덱스)
// twoSum([2,7,11,15], 9);
twoSum([3,3], 6);