package twist_in_the_tales;

class Employee implements MyInterface{
	
	String name;
	String address;
	String phoneNumber;  
	float experience;
	
	public String getName(){
		return name;
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

class Programmer extends Employee implements Trainable{
	
	String[] programmingLanguages;
	void writeCode(){
		
	}
	
	
	// When implementing methods belonging to an interface you must use the 'public' access modifier
	public void attendTraining(String[] trainingSchedule){
		System.out.println("Prog - attendTraining");
	}
	
}

interface BaseInterface1{
	String getName();
}

interface BaseInterface2{
	String getName();
}

interface MyInterface extends BaseInterface1, BaseInterface2{}


interface Trainable{
	// methods of an interface are implicitly public
	public void attendTraining(String[] trainingSchedule);
}

interface Interviewer{
	public void conductInterview();
}

class Office {

	public static void main(String[] args) {
		
		Programmer Colin = new Programmer();
		Colin.name = "my name";
		
		String programmersName = Colin.getName();
		
		System.out.println(programmersName);
		
		
	}
}


