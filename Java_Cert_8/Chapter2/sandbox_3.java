package Chapter2;

import java.util.ArrayList;

public class sandbox_3 {

    public static void main(String[] args){
        /*Integer i1 = new Integer(100);
        Integer i2 = new Integer(100);

        Integer i3 = Integer.valueOf(100);
        Integer i4 = Integer.valueOf(100);

        Integer i5 = 100;
        Integer i6 = 100;

        System.out.println(i1.equals(i2));
        System.out.println(i3 == i4);
        System.out.println(i4 == i5);
        System.out.println(i5 == i6);

        Integer obj1 = 100;
        Short obj2 = 100;

        System.out.println(obj1.equals(obj2));

        Double d1 = new Double(12.67);
        Double d2 = new Double(12.67);

        System.out.println(d1 == d2);*/

        int myInt = 7;
        boolean result = true;
        if (result == true)
            do
                System.out.println(myInt);
            while (myInt > 10);


        final byte age1 = 10;
        final byte age2 = 20;
        short sum = age1 + age2;


        //Assignment
        Boolean bool1 = true;

        //Constructor
        Boolean bool2 = new Boolean(true);

        //Call static method
        Boolean bool3 = Boolean.valueOf(true);

        Long var1 = Long.valueOf(123);
        Long var2 = Long.valueOf("123");
        System.out.println(var1 == var2);

        Long var3 = Long.valueOf(223);
        Long var4 = Long.valueOf("223");
        System.out.println(var3 == var4);

        System.out.println(var3.equals(var4));






    }


}


