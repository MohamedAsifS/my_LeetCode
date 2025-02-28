class Solution {
    public List<String> findRepeatedDnaSequences(String s) {

        HashMap<String,Integer> hash=new HashMap<>();
        HashSet<String> res=new HashSet<>();
         
        System.out.println(hash);
        int l=10;
        for(int i=0;i<(s.length())-9;i++){
            String slicer=s.substring(i,l);
            if (hash.containsKey(slicer)){
               hash.put(slicer,hash.getOrDefault(slicer,0)+1);
                res.add(slicer);
            }
            else{
                hash.put(slicer,1);
               
            }
            l+=1;
        }
   
        List<String> res1=new ArrayList<>(res);

       
        return res1;
        
    }
}