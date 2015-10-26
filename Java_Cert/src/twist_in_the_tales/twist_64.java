package twist_in_the_tales;


class Employee{
	
	String run(){
		System.out.println("Emp-run");
		return null;
	}
}

class Programmer extends Employee{
	String run(){
		System.out.println("Programmer-run");
		return null;
	}
}


public class twist_64 {
	public static void main(String[] args) {
		new Programmer().run();

	}
}

