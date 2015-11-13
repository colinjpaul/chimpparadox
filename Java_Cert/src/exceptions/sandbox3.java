package exceptions;

import java.io.*;

public class sandbox3 {

	public static void main(String[] args) {
		FileInputStream fis = null;
		try{
			fis = new FileInputStream("file.txt");
			fis.close();
		}
		
		catch(FileNotFoundException fnfe){
			System.out.println("file not found");
		}
		
		catch(IOException ioe){
			System.out.println("IO Exception");
		}

		
	}

}
