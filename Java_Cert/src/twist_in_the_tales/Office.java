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

interface Trainable{
	// methods of an interface are implicitly public
	void attendTraining(String[] trainingSchedule);
}


class HRExecutive extends Employee implements Interviewer{

	String[] specialization;
	
	public void conductInterview() {
		System.out.println("HR Executive - Conducting Interview");
	}
	
}

class Manager extends Employee implements Interviewer, Trainable{
	
	int teamSize;
	void reportProjectStatus(){}
	
	public void conductInterview(){
		System.out.println("Mgr - conductInterview");
	}
	
	
	public void attendTraining(String[] trainingSchedule){
		System.out.println("Mgr - attendTraining");
	}
	
}

class Office {

	public static void main(String[] args) {
		
		//A variable of HRExecutive can be used to refer to its object
		HRExecutive hr = new HRExecutive();
		
		//Access Variable defined in class HRExecutive
		hr.specialization = new String[] {"Staffing"};
		System.out.println(hr.specialization[0]);
		
		//Access Variable defined in class Employee
		hr.name = "Pavni Gupta";
		System.out.println(hr.name);
		
		//Access method defined in interface interviewer
		hr.conductInterview();
		
		//Variable of type employee can also be used to refer to an object
		//of class HRExecutive because class HRExecutive extends employee
		
		Employee emp = new HRExecutive();
		
		Interviewer interviewer = new HRExecutive();
		
		//Variable of a type interface (eg: Interviewer) can only access defined in interface Interviewer
		
		interviewer.conductInterview();
		
		
		
		
	
		
		
			
		
	}
}


