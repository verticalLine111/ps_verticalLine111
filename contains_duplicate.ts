function containsDuplicate(nums: number[]): boolean {
    const map: any = {}
    for(let i = 0; i < nums.length; i++){ 
        if(map[`${nums[i]}`] === undefined) {
            map[`${nums[i]}`] = 1;
        }else {
            map[`${nums[i]}`] += 1;
        }
    }

    const keys = Object.keys(map)
    for(let i = 0; i < keys.length; i++) {
        if(map[keys[i]] > 1) {
            return true;
        }
    }

    return false;
};