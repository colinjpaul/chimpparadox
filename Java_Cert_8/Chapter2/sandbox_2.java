
class sandbox_2 {

    public static void main(String[] args) {

        int baseDecimal = 267;
        int octVal = 0413;
        int hexVal = 0x10B;
        int binVal = 0b100001011;

        System.out.println(baseDecimal + octVal);
        System.out.println(hexVal + binVal);

        char c3 = (char)-122;

        System.out.println(c3);

        byte exam_total = 7;
        System.out.println(exam_total);

        final byte age1 = 10;
        final byte age2 = 2;

        System.out.println(age1);

        short sum = age1 + age2;

        int a = 10;
        a = ++a + a + --a - --a + a++;
        System.out.println(a);

        String name = "hello";
        if (name != null && name.length() > 0)
            System.out.println(name.toUpperCase());



    }


}
