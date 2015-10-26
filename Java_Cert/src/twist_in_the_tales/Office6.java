package twist_in_the_tales;

interface MobileAppExpert{
	void deliverMobileApp();
}


class Employee implements MobileAppExpert {
	public void deliverMobileApp(){
		System.out.println("Employee now involved");
	}
	
}

class Programmer extends Employee{
	public void deliverMobileApp(){
		System.out.println("testing complete on real device");
	}
}

class Manager extends Employee{
	public void deliverMobileApp(){
		System.out.println("QA Complete");
		System.out.println("code delivered with release notes");
	}
}
public class Office6 {

	public static void main(String[] args) {
		
		// A reference variable of type 'MobileAppExpert' can be used...
		// ...to store objects of the classes 'Programmer' and 'Manager'
		
		Employee expert1 = new Programmer();
		Employee expert2 = new Manager();
		
		expert1.deliverMobileApp();
		expert2.deliverMobileApp();

	}

}
