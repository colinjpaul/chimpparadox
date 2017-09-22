class Emp {
    String name;
    static int bankVault;
    static int getBankVaultValue(){
        return bankVault;

    }

    static double averageOfFirst100Integers(){
        int sum = 0;
        for (int i=1; i <=100; ++i){
            sum += i;
        }
        return (sum)/100;
    }

}
