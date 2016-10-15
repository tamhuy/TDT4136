import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * Created by tamhu on 02-Oct-16.
 */
public class Main {

    public static void main(String[] args) {
        String file = "boards/board-1-1.txt";
        LoadBoard test = new LoadBoard(file);
        test.printBoard();
        ArrayList<ArrayList<Node>> board = test.getBoard();
        System.out.println(board.get(5).get(1).location);
        System.out.println(test.getB());
        AStar program = new AStar();
        program.aStar(test.getBoard(),test.getA(),test.getB());

        ArrayList<ArrayList<String>> board2 = test.visualize(file);
        Node c = test.getBoard().get(test.getB().get(0)).get(test.getB().get(1));
//        System.out.println(c.c);
//        System.out.println(c.parent.c);

//        for(int i =0; i< 20; i++){
//            System.out.println(c.location);
//            c = c.parent;
//        }
        while(c.parent != null) {
            System.out.println(c.location);
            c = c.parent;
        }
//        PriorityQueue<Node> asd = new PriorityQueue<Node>(1, new Comparator<Node>() {
//            @Override
//            public int compare(Node o1, Node o2) {
//                return ((Double)(o1.w)).compareTo((Double)o2.w);
//            }
//        });
//        asd.add(new Node(0,0,'a',500));
//        asd.add(new Node(1,1,'b',100));
//        asd.add(new Node(2,2,'c',15));
//        for(int i = 0; i<3;i++) {
//            System.out.println(asd.remove().c);
//        }
//
//        System.out.println(asd);
    }
}
