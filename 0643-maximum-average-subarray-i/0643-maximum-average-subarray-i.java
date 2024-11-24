class Solution {
    public double findMaxAverage(int[] nums, int k) {

        double res=-10000000;
        int n=k;
        int summer=0;
        int l=0;

        for(int r=0;r<nums.length;r++){
            summer+=nums[r];
            if (r==(k-1)){
                res=Math.max(res,summer);
                summer-=nums[l];
                l++;
                k++;
            }
        }
        return res/n;
    }
}