package exceptions;

import java.io.*;
import java.util.ArrayList;


class SMS{
	 
	private String msg;
	private boolean inTransit = false;
	
	public void create(){
		msg = "A new message";
	}
	
	public void transmit(){
		inTransit = true;		
	}
	
	public void modify(){
		if (!inTransit)
			msg = "A new MODIFIED message";
		else
			throw new IllegalStateException("Can't modify - In transit");
		
	}
	
	
}

public class sandbox3 {

	
	
	
	public static void main(String[] args){
		
		
		String[][] oldLaptops = {	{"Dell", "Toshiba", "Vaio"}, null, {"IBM"}, new String[10]	};
		
		System.out.println(oldLaptops[0][2]);
		System.out.println(oldLaptops[1]);
		System.out.println(oldLaptops[3][6]);
		System.out.println(oldLaptops[3][0]);
		
		System.out.println(Integer.parseInt("-123"));
		
		System.out.println(Integer.parseInt("12ABCD", 16));
		
		
		
		
	}
		
		

}


