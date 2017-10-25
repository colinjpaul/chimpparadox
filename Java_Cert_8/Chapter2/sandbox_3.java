public class sandbox_3 {

    public static void main(String[] args){
        Integer i1 = new Integer(10);
        Integer i2 = new Integer(10);

        Integer i3 = Integer.valueOf(10);
        Integer i4 = Integer.valueOf(10);

        Integer i5 = 10;
        Integer i6 = 10;

        System.out.println(i1 == i2);
        System.out.println(i3 == i4);
        System.out.println(i4 == i5);
        System.out.println(i5 == i6);

        Integer var3 = Integer.valueOf(10);
        Integer var4 = Integer.valueOf(10);

        System.out.println(var3 == var4);
    }


}


