class Solution {
    public int longestSubarray(int[] nums) {
        int res=-1;
        int zero=0;
        int l=0;
        int current=0;

        for(int r=0;r<nums.length;r++){
            if (nums[r]==0){
                zero++;
                current=r;

            }
            while(zero>1){
                if (nums[l]==0){
                    zero--;
                }
                l++;
            }
            
           
            res=Math.max(res,r-l);
        }

        return res;
        
    }
}