package sample_exam_questions;

class Base {
	String var = "EJava";
	void printVar(){
		System.out.println(var);
	}
}

class Derived extends Base{
	String var = "Guru";
	void printVar(){
		System.out.println(var);
	}
	
}

public class chapter_6 {

	public static void main(String[] args) {
		
		Base base = new Base();
		Base derived = new Derived();
		
		//Prints EJava - instance variable binds at compile time
		System.out.println(base.var);
		
		//Prints EJava - instance variable binds at compile time
		System.out.println(derived.var);
		
		//Prints EJava - methods bind at run time
		base.printVar();
		
		//Prints Guru - methods bind at run time
		derived.printVar();
	
		

	}

}
