package sample_exam_questions;

public class chapter_7 {
	
	int tryAgain(){
		int a = 10;
	
	try{
		++a;
	}
	
	finally{
		a++;
	}
	return a;
	}

	public static void main(String[] args) {
		System.out.println(new chapter_7().tryAgain());

		
		
	}

		
	

}
