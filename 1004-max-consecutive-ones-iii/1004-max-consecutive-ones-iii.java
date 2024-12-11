class Solution {
    public int longestOnes(int[] nums, int k) {
        int res=-1;
        int zero=0;
        int l=0;
        for(int r=0;r<nums.length;r++){
            if (nums[r]==0){
                zero++;
            }
            while(zero > k){
                if (nums[l]==0){
                    zero--;
                }
                l++;
            }
            res=Math.max(res,r-l+1);
        }

        return res;
        
    }
}