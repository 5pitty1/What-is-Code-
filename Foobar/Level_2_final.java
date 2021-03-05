public class Level_2_final {

    public static int[] getLastRange(int peg, int[] pegs, int min, int max) {

        if(max - min < 0) {
            return new int[]{-1, -1};
        }
        if(peg == pegs.length - 1) {
            return new int[]{min, max};
        }

        int currPeg = pegs[peg];
        int nextPeg = pegs[peg + 1];
        int diff = nextPeg - currPeg;

        int intersectMax = Integer.min(max, diff - 1);
        int intersectMin = Integer.max(min, 1);

        return getLastRange(peg + 1, pegs, diff - intersectMax, diff - intersectMin);
    }

    public static int[] getFirstRange(int peg, int[] pegs, int min, int max) {
        if(peg == 0) {
            return new int[]{min, max};
        }

        int currPeg = pegs[peg];
        int prevPeg = pegs[peg - 1];
        int diff = currPeg - prevPeg;

        int intersectMax = Integer.min(max, diff - 1);
        int intersectMin = Integer.max(min, 1);

        return getFirstRange(peg - 1, pegs, diff - intersectMax, diff - intersectMin);

    }

    private static int[] findFirstSize(int[] firstRange, int[] lastRange, int numPegs) {
        int[] firstPegSize = {-1, -1};

        if(numPegs%2 == 0) {
            int pegNum = (2*lastRange[1] - firstRange[0]) + 3*firstRange[0];
            double pegSize = pegNum / 3;
            System.out.println(pegNum);
            if(pegSize > firstRange[0] && pegSize < firstRange[1]) {
                firstPegSize[0] = pegNum%3==0 ? pegNum/3 : pegNum;
                firstPegSize[1] = pegNum%3==0 ? 1 : 3;
            }
        } else {
            int pegSize = (firstRange[0] - 2*lastRange[0]) + firstRange[0];
            if(pegSize > firstRange[0] && pegSize < firstRange[1]) {
                firstPegSize[0] = pegSize;
                firstPegSize[1] = 1;
            }
        }

        return firstPegSize;
    }


    public static int[] solution(int[] pegs) {
        if (pegs.length <= 1) {
            return new int[]{-1, -1};
        }

        int[] lastRange = getLastRange(0, pegs, 1, Integer.MAX_VALUE);

        int[] firstRange = getFirstRange(pegs.length - 1, pegs, lastRange[0], lastRange[1]);

        System.out.printf("%d: (%d, %d)\n", pegs[0], firstRange[0], firstRange[1]);
        System.out.printf("%d: (%d, %d)\n", pegs[pegs.length - 1], lastRange[0], lastRange[1]);

        return findFirstSize(firstRange, lastRange, pegs.length);
    }

    public static void main(String[] args) {
//        int[] pegs = {4, 15, 35, 50};
        int[] pegs = {4, 30};
//        int[] pegs = {4, 15, 23, 25, 30, 40, 50};

        int[] solution = solution(pegs);
        System.out.println(solution[0] + " : " + solution[1]);
    }
}