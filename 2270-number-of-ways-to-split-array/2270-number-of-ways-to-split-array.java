class Solution {
    public int waysToSplitArray(int[] nums) {
        long secondHalf=0,firstHalf=0;
        int res=0;

        for(int i:nums){
            secondHalf+=i;
        }
      

        for(int i=0;i<nums.length-1;i++){
            secondHalf-=nums[i];
            firstHalf+=nums[i];

            if (firstHalf >= secondHalf){
                res++;
            }
        }
return res;
        
    }
}