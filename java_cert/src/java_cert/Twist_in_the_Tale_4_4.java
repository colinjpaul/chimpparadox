package java_cert;

import java.util.ArrayList;

public class Twist_in_the_Tale_4_4 {
	
	public static void main (String args[]){
		
		System.out.println("hello");
		
		ArrayList<String> myArrList = new ArrayList<String>();
		
		String one = "One";
		String two = new String("Two");
		
		myArrList.add(one);
		myArrList.add(two);
		
		ArrayList<String> yourArrList = myArrList;
		
		one.replace("0", "B");
		
		for (String val : myArrList)
			System.out.print(val + ":");
		
		for (String val : yourArrList)
		
			System.out.print(val + ":");
		
		

	}
}