class Solution {
    public boolean checkIfExist(int[] arr) {

        HashSet<Integer> box = new HashSet<>();

        for (int i : arr) {
            if ((box.contains(i / 2) && i % 2 == 0) || box.contains(i * 2)) {

                return true;
            } else {

                box.add(i);
            }

        }
        return false;
    }
}