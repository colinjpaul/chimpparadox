package twist_in_the_tales;

class Employee {
	
	String name;
	String address;
	String phoneNumber;  
	float experience;
	
	/*Employee(){
		name = "NoName";
		address = "No Address";
		
	}*/
	
	/*Employee (String name){
		
		//In the scope of the method block the local variable 'name'
		//will take precedence over the instance variable name so need
		//to prefix with 'this'
		this.name = name;
		
	}
	
	Employee (String name, String Address){
		this(name);
		
		this.address = address;
		
	}*/
		

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
	
	int teamSize = 10;
		
	public void conductInterview(){
		System.out.println("Mgr - conductInterview");
	}
}


class Office2 {

	public static void main(String[] args) {
		
		Interviewer[] interviewers = new Interviewer[2];
		
		interviewers[0] = new Manager();
		interviewers[1] = new HRExecutive();
		
		for (Interviewer interviewer : interviewers)
		{
			if (interviewer instanceof Manager){
				int teamSize = ((Manager)interviewer).teamSize;
				
				if (teamSize > 10){
					interviewer.conductInterview();
				}
				else{
					System.out.println("Manager with a team less than 10 can't interview ");
				}
				
				
			}
			
			else if (interviewer instanceof HRExecutive){
				interviewer.conductInterview();
			}
						
		}
		
	}
}


