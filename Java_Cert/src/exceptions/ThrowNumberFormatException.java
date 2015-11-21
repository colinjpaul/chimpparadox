package exceptions;

class MyException extends RuntimeException{}

public class ThrowNumberFormatException {
	
	static void recursion(){
		recursion();
	}
	
	
	/*
	//  static initializer block
	
	static{
		int num = Integer.parseInt("sd",16);
	}
	
	//  Initialization of a static variable
	static String name = null;
	static int nameLength = name.length();
	
	
	
	static String name = getName();
	
	static String getName(){
		throw new MyException();
	}*/
	
		
	public static int convertToNum(String val){
		int num = 0;
		try{
			num = Integer.parseInt(val, 16);
		}
		catch(NumberFormatption e){
			throw new NumberFormatException(val+ " cannot be converted to hexadecimal number");
			
		}
		return num;
	}
	
	public static void main(String[] args) {
		
		recursion();
		
		System.out.println(convertToNum("16b"));
		System.out.println(convertToNum("16f"));
		
	
		
	}

}


