package twist_in_the_tales;

class Employee {
	
	String name;
	String address;
	String phoneNumber;  
	float experience;
}

interface Interviewer{
	public void conductInterview();
}


class HRExecutive extends Employee implements Interviewer{

	String[] specialization;
	
	public void conductInterview() {
		System.out.println("HR Executive - Conducting Interview");
	}
	
}

class Manager implements Interviewer{
	
	int teamSize;
		
	public void conductInterview(){
		System.out.println("Mgr - conductInterview");
	}
	
	
	
}

class Office2 {

	public static void main(String[] args) {
		
		Interviewer interviewer = new HRExecutive();
		
		((HRExecutive)interviewer).specialization = new String[]{"Staffing"};
		
		System.out.println("bed time");
		
		
	}
}


