class Solution {
    public int maxOperations(int[] nums, int k) {
        
        HashMap <Integer,Integer> box=new HashMap<>();

        int res=0;

        for(int i=0;i<nums.length;i++){
            if(box.containsKey(nums[i]) && box.get(nums[i])>=1){
                res++;
                box.put(nums[i],box.getOrDefault(nums[i],0)-1);
            }
            else if(!box.containsKey(k-nums[i])){
                box.put(k-nums[i],1);
            }
            else if(box.containsKey(k-nums[i])){
               box.put(k-nums[i],box.getOrDefault(k-nums[i],0)+1);
            }
        }
        return res;
    }
}