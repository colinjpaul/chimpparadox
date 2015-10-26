package twist_in_the_tales;


class Employee{
	String name = "Employee";
	void printName(){
		System.out.println(name);
	}
}

class Programmer extends Employee{
	String name = "Programmer";
	void printName(){
		System.out.println(name);
	}
}
public class Office5 {

	public static void main(String[] args) {
		//Reference variable of type employee; object of type employee
		Employee emp = new Employee();
		
		//Reference variable of type employee; object of type programmer
		Employee programmer = new Programmer();
		
		//Access variable name defined in class employee
		System.out.println(emp.name);
		
		//Variables are bound at compile time
		//Because type of variable programmer is Employee...
		//...this accesses the variable name defined in Employee
		System.out.println(programmer.name);
		
		//Methods are bound at run time
		//Which method executes depends on the type of object on which it's called
		emp.printName();
		programmer.printName();

	}

}
