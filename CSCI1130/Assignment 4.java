package musicapp;

import java.util.Scanner;
import java.io.*;

public class MusicApp{
    public static int noOfWrong=0;
    public static String userInput;
    
     public static void main(String []args) 
     {
        if(noOfWrong<=3)
        {
            try{
                getInput();
            }
            catch(IOException io_excption_object_ref)
            {
                System.out.println("Something Wrong!");
                noOfWrong+=1;
            }
        }
        else
        {
            System.exit(1);
        }
     }
     
     public static void getInput() throws IOException
     {
        
        Scanner keyboard= new Scanner(System.in);
        
        try{
            System.out.print("Song filename: ");
            userInput=keyboard.nextLine();
            InputStream f = new FileInputStream(userInput);  
        }
        catch (IOException io_exception_object_ref)
        {
            throw new IOException();
        }
        
            
        
     }
     
     
}
