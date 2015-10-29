package sample_exam_questions;

interface Employee{
	
}

interface Printable extends Employee{
	String print();
}

class Programmer {
	String print(){
		return ("Programmer - Mala Gupta");
	}
}

class Author extends Programmer implements Printable, Employee{
	public String print(){
		return ("Author - Mala Gupta");
	}
}

public class chapter_6 {

	public static void main(String[] args) {
		
		Programmer a = new Programmer();
		Author b = new Author();
		
		a.print();
		b.print();
		

	}

}
