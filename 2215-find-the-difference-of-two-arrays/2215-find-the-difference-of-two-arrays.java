class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        HashSet <Integer> num1=new HashSet<>();
        HashSet <Integer> num2=new HashSet<>();

        List <List<Integer>> res=new ArrayList<>(); 

        for(int i:nums1){
            num1.add(i);
        }
        
        for(int i:nums2){
            num2.add(i);
        }
        System.out.println(num1);
        System.out.println(num2);
        List <Integer> temp=new ArrayList<>();
       for(int i:num1){
        if (!num2.contains(i)){
            temp.add(i);

        }}
        res.add(temp);
        List <Integer> temp1=new ArrayList<>();

            for(int i:num2){
        if (!num1.contains(i)){
            temp1.add(i);

        }
           
       }
       res.add(temp1);
        return res;
    }
}