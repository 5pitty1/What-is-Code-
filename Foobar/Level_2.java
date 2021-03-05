import java.util.Arrays;
import java.util.Stack;

public class Level_2 {

    static int getLastRadius(int peg, int radius, int[] pegs) {
//        String tabs = "\t".repeat(peg);
        System.out.println(pegs[peg] + " : " + radius);

        if(radius < 1) {
            return -1;
        }

        if(peg == pegs.length - 1) {
            return radius;
        }

        int currPeg = pegs[peg];
        int nextPeg = pegs[peg + 1];

        int nextRadius = (nextPeg - currPeg) - radius;

        return getLastRadius(peg + 1, nextRadius, pegs);
    }

    public static int[] solution(int[] pegs) {
        int firstPeg = pegs[0];
        int secondPeg = pegs[1];

        for (int radius = 1; radius < secondPeg - firstPeg; radius++) {
            int lastRadius = getLastRadius(0, radius, pegs);

            System.out.println("First Radius: " + radius);
            System.out.println("Last Radius: " + lastRadius);
            System.out.println();

//            if(radius == lastRadius*2) {
//            if(lastRadius > 0) {
//                return new int[]{radius, 1};
//            }
        }

        return new int[]{-1, -1};
    }

    public static void main(String[] args) {
        int[] pegs = {12, 24, 25, 35, 50};
//        int[] pegs = {4, 30, 50};

        solution(pegs);
    }
}