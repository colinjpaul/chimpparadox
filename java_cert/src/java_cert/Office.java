package java_cert;

public class Office {
	
		public static void main (String args[]){
			System.out.println("test");			
		}	
	}

interface Trainable{
	public void attendTraining(String[] trainingSchedule);
}

interface Interviewer{
	public void conductInterview();
}

class Employee{
	String name;
	String address;
	String phoneNumber;
	float experience;	
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

class Programmer extends Employee implements Trainable{
	String[] programmingLanguages;
	void writeCode(){}
	public void attendTraining(String[] trainingSchedule){
		System.out.println("Prog - attendTraining");
	}
}
