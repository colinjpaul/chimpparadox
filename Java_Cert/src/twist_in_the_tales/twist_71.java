package twist_in_the_tales;

import java.io.*;

public class twist_71 {

	public static void main(String[] args) {
		FileInputStream fis = null;
		
		try{
			fis = new FileInputStream("C:\\Users\\cjadmin\\Documents\\GitHub\\chimpparadox\\testfiles\\file.txt");
			System.out.println("File Opened");
			fis.read();
			System.out.println("Read file");
		}
		
		catch (FileNotFoundException fnfe){
			System.out.println("File not found");
		}
		
		catch (IOException ioe){
			System.out.println("File closing exception");
		}
		
		finally {
			System.out.println("Finally");
		}
				
		System.out.println("Next task...");

	}

}
