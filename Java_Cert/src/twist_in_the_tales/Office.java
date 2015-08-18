package twist_in_the_tales;

class Employee {
	
	String name;
	String address;
	protected String phoneNumber;  //can be accessed by all derived classes regarded of package
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

class Office {

	public static void main(String[] args) {
		
		new Programmer ("Harry").getName();
		
		
		
	}

}
