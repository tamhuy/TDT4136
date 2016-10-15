import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.PriorityQueue;

import static java.lang.Math.abs;

/**
 * Created by tamhuy on 02-Oct-16.
 */
public class AStar {

    public void aStar(ArrayList<ArrayList<Node>> board, ArrayList<Integer> a, ArrayList<Integer> b){

        PriorityQueue<Node> open = new PriorityQueue<Node>(10, new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2) {
                return ((Double)(o1.f)).compareTo((Double)o2.f);
            }
        });
        ArrayList<Node> closed = new ArrayList<>();

        board.get(a.get(0)).get(a.get(1)).g = 0;
        board.get(a.get(0)).get(a.get(1)).h = 0;
        board.get(a.get(0)).get(a.get(1)).f = board.get(a.get(0)).get(a.get(1)).g + board.get(a.get(0)).get(a.get(1)).h;
        open.add(board.get(a.get(0)).get(a.get(1)));

        while (true){
            if(open.isEmpty()){
                break;
            }

            Node x = open.remove();
            if(x.location == b){
                break;
            }
            closed.add(x);
            ArrayList<Node> children = new ArrayList<>();

            if(x.location.get(0) != 0) {
                if (board.get(x.location.get(0)-1).get(x.location.get(1)).c != '#'){
                    children.add(board.get(x.location.get(0)-1).get(x.location.get(1)));
                }
            }
            if(x.location.get(0) != board.size()) {
                if (board.get(x.location.get(0)+1).get(x.location.get(1)).c != '#'){
                    children.add(board.get(x.location.get(0)+1).get(x.location.get(1)));
                }
            }
            if(x.location.get(1) != 0) {
                if (board.get(x.location.get(0)).get(x.location.get(1)-1).c != '#'){
                    children.add(board.get(x.location.get(0)).get(x.location.get(1)-1));
                }
            }
            if(x.location.get(1) != board.size()) {
                if (board.get(x.location.get(0)).get(x.location.get(1)+1).c != '#'){
                    children.add(board.get(x.location.get(0)).get(x.location.get(1)+1));
                }
            }
            for(int i = 0;i<children.size();i++){
                x.children.add(children.get(i));

                if (!open.contains(children.get(i)) && !closed.contains(children.get(i))){
                    attachAndEval(children.get(i),x,b);
                    open.add(children.get(i));
                }
                else if (x.g + children.get(i).w < children.get(i).g){
                    attachAndEval(children.get(i),x,b);
                }
            }

        }

    }

    public void attachAndEval(Node node, Node parent, ArrayList<Integer> b){
        node.parent = parent;
        node.g = parent.g + node.w;
        node.h = heuristic(node.location, b);
        node.f = node.g + node.h;
    }


    public int heuristic(ArrayList<Integer> start,ArrayList<Integer> end){
        return abs(start.get(0) - end.get(0)) + abs(start.get(1) - end.get(1));
    }
}
