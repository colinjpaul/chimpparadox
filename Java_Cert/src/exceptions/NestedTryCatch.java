package exceptions;

import java.io.*;
public class NestedTryCatch {
	FileInputStream players, coach;
	public void myMehtod(){
		try{
			players = new FileInputStream("C:\\Users\\cjadmin\\Documents\\GitHub\\chimpparadox\\testfiles\\players.txt");
			System.out.println("players.txt found");
			try{
				coach.close();
				
			}
			catch (IOException e){
				System.out.println("coach.txt not found");
			}
			
			
			
			
		}
		catch(FileNotFoundException fnfe){
			System.out.println("players.txt not found");
		}
		
		catch(NullPointerException ne){
			System.out.println("NullPointerException");
		}
		
	}

}
