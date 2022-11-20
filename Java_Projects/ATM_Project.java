
// ATM -- Automated Teller Machine

//importing required classes and packages   
import java.util.Scanner; 

//creating ATM class to implement the ATM functionality  
public class ATM_Project {

	//main method starts
	public static void main(String[] args) 
	    {  
	        //declaring and initializing balance, withdraw, and deposit  
	        int balance = 100000, withdraw, deposit;  
	          
	        //create scanner class object to get choice of user  
	        Scanner sc = new Scanner(System.in);  
	          
	        while(true)  
	        {  
	            System.out.println("Automated Teller Machine");  
	            System.out.println("Choose 1 for Withdraw");  
	            System.out.println("Choose 2 for Deposit");  
	            System.out.println("Choose 3 for Check Balance");  
	            System.out.println("Choose 4 for EXIT");  
	            System.out.print("Choose the operation you want to perform:");  
	              
	            //getting choice from user  
	            int choice = sc.nextInt();  
	            switch(choice)  
	            {  
	                case 1:  
		        System.out.print("Enter money to be withdrawn:");  
		                      
		        //getting the withdrawal money from user  
		        withdraw = sc.nextInt();  
		                      
		        //checking whether the balance is greater than or equal to the withdrawal amount  
		        if(balance >= withdraw)  
		        {  
		            //removing the withdrawal amount from the total balance  
		            balance = balance - withdraw;  
		            System.out.println("Please collect your money");  
		        }  
		        else  
		        {  
		            //showing custom error message   
		            System.out.println("Insufficient Balance");  
		        }  
		        System.out.println("");  
		        break;  
		   
		                case 2:  
		                      
		        System.out.print("Enter money to be deposited:");  
		                      
		        //getting deposit amount from te user  
		        deposit = sc.nextInt();  
		                      
		        //adding the deposit amount to the total balance  
		        balance = balance + deposit;  
		        System.out.println("Your Money has been successfully deposited");  
		        System.out.println("");  
		        break;  
		   
		                case 3:  
		        //displaying the total balance of the user  
		        System.out.println("Balance : "+balance);  
		        System.out.println("");  
		        break;  
		   
		                case 4:  
		        //exiting from the menu  
		        System.exit(0);  
	            }  
	        }
	    }  
	}  
