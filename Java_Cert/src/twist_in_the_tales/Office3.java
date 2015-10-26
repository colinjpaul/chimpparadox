package twist_in_the_tales;

class Employee{
	
	String name = "Emp";
	String address = "EmpAddress";
		
}
	


class Programmer extends Employee{
	
	String name = "Prog";
	void printValues(){
		System.out.print(this.name + ":");
		System.out.print(this.address  + ":");
		System.out.print(super.name + ":");
		System.out.print(super.address);
	}
	
}

public class Office3 {

	public static void main(String[] args) {

		new Programmer().printValues();
		
	}

}
