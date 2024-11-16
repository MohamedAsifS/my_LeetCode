class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {

        List<Boolean> box=new ArrayList<>();

        int max=-1;

        for(int i=0;i<candies.length;i++){
            // max=Math.max(max,candies[i]);
            if(max<candies[i]){
                max=candies[i];
            }
        }
   
        for(int i=0;i<candies.length;i++){
            if((candies[i]+extraCandies)>=max){
                box.add(true);

            }
            else{
                box.add(false);
            }
        }




          


          return box;
    }
  

}