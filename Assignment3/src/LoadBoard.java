import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by tamhu on 02-Oct-16.
 */
public class LoadBoard {

    private ArrayList<ArrayList<Node>> board = new ArrayList<>();

    public LoadBoard(String in){
        try {
            Scanner scanner = new Scanner(new FileReader(in));
            int tall = 0;
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                ArrayList<Node> test = new ArrayList<>();

                for (int i=0; i<line.length(); i++)
                {
                    if(line.charAt(i) == '#') {
                        test.add(new Node(tall, i, line.charAt(i), Double.POSITIVE_INFINITY));
                    }
                    else{
                        test.add(new Node(tall, i, line.charAt(i), 1));
                    }
                }
                board.add(test);
                tall +=1;
            }
            scanner.close();
        }
        catch (FileNotFoundException e)
        {
            System.err.println("Error: file 'test.txt' could not be opened. Does it exist?");
            System.exit(1);
        }
    }

    public ArrayList<ArrayList<Node>> getBoard(){
        return board;
    }

    public void printBoard() {
        for(int i=0;i<board.size();i++){
            String signs = "";
            for(int j=0;j<board.get(i).size();j++) {
                signs += board.get(i).get(j).c;
            }
            System.out.println(signs);
        }
    }

    public ArrayList<Integer> getA(){
        for(int i=0;i<board.size();i++){
            for(int j=0;j<board.get(i).size();j++) {
                if(board.get(i).get(j).c =='A'){
                    return board.get(i).get(j).location;
                }
            }
        }
        return null;
    }

    public ArrayList<Integer> getB(){
        for(int i=0;i<board.size();i++){
            for(int j=0;j<board.get(i).size();j++) {
                if(board.get(i).get(j).c =='B'){
                    return board.get(i).get(j).location;
                }
            }
        }
        return null;
    }

    public ArrayList<ArrayList<String>> visualize(String in) {
        ArrayList<ArrayList<String>> board2 = new ArrayList<>();

        try {
            Scanner scanner = new Scanner(new FileReader(in));
            int tall = 0;
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                ArrayList<String> test = new ArrayList<>();

                for (int i = 0; i < line.length(); i++) {
                    test.add(String.valueOf(line.charAt(i)));
                }
                board2.add(test);
                tall += 1;
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            System.err.println("Error: file 'test.txt' could not be opened. Does it exist?");
            System.exit(1);
        }
        return board2;
    }

}
