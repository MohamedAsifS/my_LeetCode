class Solution {
    public int[] vowelStrings(String[] words, int[][] queries) {

        HashSet<Character> hs=new HashSet<>(Set.of('a','e','i','o','u'));
        
        int[] arr=new int[words.length];
        int count=0;
        int temp=0;
        for(String word:words){
            if (word.length()==1 && hs.contains(word)){
                temp++;
            }
            else if(hs.contains(word.charAt(0))&& hs.contains(word.charAt(word.length()-1))){
                temp++;
              
            }
            //   System.out.println((word.charAt(0)+ ""+ hs.contains(word.charAt(0))+" "+word.charAt(word.length()-1)));
             
            arr[count]=temp;
            count++;

            

        }

        // for(int i:arr){
        //     System.out.println(i);
        // }
        int[] final1=new int[queries.length];
        count=0;
        for(int[] j:queries){
           final1[count]=arr[j[1]];
           if(j[0]!=0){
            final1[count]-=arr[j[0]-1];
           }
           count++;

        }


       return final1; 
    }
}