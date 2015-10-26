package twist_in_the_tales;

class Employee{
	public void reachOffice(){
		System.out.println("reached office - Gurgaon, India");
	}
	
	public void startProjectWork(){
		System.out.println("procure hardware");
		System.out.println("install software");
	};
}

class Programmer extends Employee{
	
	//Access modifiers for an overriding method must be the same or 
	//less restrictive than the method being overriden
	
	public void startProjectWork(){
		defineClasses();
		unitTestCode();
	}
	
	private void defineClasses() {
		System.out.println("define classes");
	}
	
	private void unitTestCode(){
		System.out.println("unit test code");
	}
		
}

class Manager extends Employee{
	public void startProjectWork(){
		meetingWithCustomer();
		defineProjectSchedule();
		assignRespToTeam();
	}

	private void meetingWithCustomer() {
		System.out.println("Meet customer");
		
	}	
	
	private void defineProjectSchedule() {
		System.out.println("Project Schedule");
		
	}
	
	private void assignRespToTeam() {
		System.out.println("Team work starts");
		
	}
	
}


public class Office4 {

	public static void main(String[] args) {
		
		
		Employee emp1 = new Programmer();
		Employee emp2 = new Manager();
		
		emp1.reachOffice();
		emp2.reachOffice();
		
		newemp.startProjectWork();
		emp1.startProjectWork();
		emp2.startProjectWork();
		
	}

}
