class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const smap = {}
        for(let i=0;i<s.length; i++) {
            if(smap[`${s[i]}`] === undefined) {
                smap[`${s[i]}`] = 1;
            } else  {
                smap[`${s[i]}`] += 1;
            }
        }
        const tmap = {}
        for(let i = 0; i<t.length ; i++) {
            if(tmap[`${t[i]}`] === undefined) {
                tmap[`${t[i]}`] = 1;
            } else  {
                tmap[`${t[i]}`] += 1;
            }
        }
        
        const keys = Object.keys(smap).length < Object.keys(tmap).length ? Object.keys(tmap) : Object.keys(smap);
        for(let i = 0;i < keys.length ; i++) {
            const key = keys[i];
            if(smap[key] !== tmap[key]) {
                return false;
            }
        }
        
        return true; 
    }
}

const res = new Solution().isAnagram("jar","jam");
// const res = new Solution().isAnagram("a","ab");
console.log(res);