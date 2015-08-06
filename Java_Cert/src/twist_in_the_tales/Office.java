package twist_in_the_tales;

class Employee {
	String name;
	String address;
	protected String phoneNumber;
	public float experience;
}


class Programmer extends Employee{
	Programmer (String val){
		name = val;
	}
	
	String getName(){
		return name;
	}
}


public class Office {

	public static void main(String[] args) {
		
	 String programmerName = new Programmer ("someoneelse").getName();
	 
	 System.out.println(programmerName);
	 
	
		
	}

}
