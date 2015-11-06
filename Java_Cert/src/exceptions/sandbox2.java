package exceptions;

import java.io.*;



public class sandbox2 {

	public static void main(String[] args) {
		
		openFile();	
		

	}
	
	private static void openFile(){
		FileInputStream fis = null;
		try{
			fis = new FileInputStream("\\..\\..\\..\\..\\testfiles\\file.txt");
		}
		catch(FileNotFoundException fnfe){
			System.out.println("File not found");
			return;
		}
		finally {
			System.out.println("finally");
		}
		
		System.out.println("next task");
		
		
	}

}
