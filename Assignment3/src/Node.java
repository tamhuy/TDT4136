import java.util.ArrayList;
import java.util.Arrays;

/**
 * Created by tamhu on 02-Oct-16.
 */
public class Node {

    public ArrayList<Integer> location= new ArrayList<>();
    public char c;
    public double w;
    public double g;
    public double f = Double.POSITIVE_INFINITY;
    public double h;
    public ArrayList<Node> children = new ArrayList<>();
    public Node parent = null;

    public Node(int y,int x,char c,double w){
        this.c = c;
        this.w = w;
        location.add(y);
        location.add(x);
    }

    public void setF(double f){
        this.f = f;
    }



   // public static void main(String[] args) {
    //    Node a =new Node(5,4,'a',10);
    //    System.out.println("Node.main");
    //    System.out.print(a.location.get(0));
    //}
}
