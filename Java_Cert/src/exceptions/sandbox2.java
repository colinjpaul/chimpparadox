package exceptions;

import java.io.*;

public class sandbox2 {

	public static void main(String[] args) {
		FileInputStream fis = null;
		try{
			fis = new FileInputStream("C:\\Users\\cjadmin\\Documents\\GitHub\\chimpparadox\\testfiles\\file.txt");
			System.out.println("File Opened");
			fis.read();
			System.out.println("Read File ");
		}
		
		catch (FileNotFoundException fnfe){
			System.out.println("File not found");
		}
		
		catch (IOException ioe){
			System.out.println("File closing exception");
		}
		
		finally{
			System.out.println("finally");
		}
		
		System.out.println("Next task...");
		

	}

}
