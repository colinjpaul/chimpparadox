import java.util.ArrayList;


public class unboxing{
    public static void main (String args[]){
        ArrayList<Double> list = new ArrayList<Double>();
        list.add(12.12);
        list.add(11.24);
        Double total = 0.0;
        for (Double d : list)
            total += d;

        System.out.println(total);

        System.out.println("test java");

    }




}