package twist_in_the_tales;

class Employee{
	
	String name;
	String address;
	
	Employee(){
		name = "NoName";
		address = "NoAddress";
	}
	
	Employee(String name){
		this.name = name;		
	}
	
	Employee(String name, String address){
		this();
		if (name !=null) this.name = name;
		if (address !=null) this.address = address;
	}
	
}

public class Office3 {

	public static void main(String[] args) {

		Employee newEmployee = new Employee("some name", "some address");
		
		System.out.println(newEmployee.name);
		System.out.println(newEmployee.address);

	}

}
