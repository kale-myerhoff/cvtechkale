import java.util.HashMap;
import java.util.Scanner;

public class IDandPasswords {
    HashMap<String , String> loginInfo = new HashMap<>();


    protected HashMap getLoginInfo(){
        return loginInfo;
    }



    public static void  addNewAccount(){
        Scanner scanner = new Scanner(System.in); //adds a scanner to get the users accountId And password

        String yesOrNo;
        String newAccountID;
        String newPasswordID;

        do {



        System.out.println("please choose a new ID for the account >");
        newAccountID = scanner.nextLine(); // grabs the accountId


        do {


        System.out.println("Is " + newAccountID + " correct? (y/n?) >");
         yesOrNo = scanner.nextLine();

        if (yesOrNo.equalsIgnoreCase("y")) {
            System.out.println("Y");



            // checks if the user inputted y

        } else if (yesOrNo.equalsIgnoreCase("n")){
            System.out.println("n");
            // checks if the user inputted n and if it is incorrect it runs it again


        } else {
            System.out.println("Error wrong input!!!");
            // performs an error if neither is used
        }

        } while (!yesOrNo.equalsIgnoreCase("y") && !yesOrNo.equalsIgnoreCase("n")  );
        //if the user doesn't choose y OR n it will run the code again at the verification

        } while (!yesOrNo.equalsIgnoreCase("y") );
        //If the user doesn't input y it will run the code again at the beginning


        //this is the end of choosing the Account's userId now we will choose a password

        do {



            System.out.println("please choose a new ID for the password >");
            newPasswordID = scanner.nextLine(); // grabs the passwordId


            do {


                System.out.println("Is " + newPasswordID + " correct? (y/n?) >");
                yesOrNo = scanner.nextLine();

                if (yesOrNo.equalsIgnoreCase("y")) {
                    System.out.println("Y");
                    // checks if the user inputted y

                } else if (yesOrNo.equalsIgnoreCase("n")){
                    System.out.println("n");
                    // checks if the user inputted n and if it is incorrect it runs it again


                } else {
                    System.out.println("Error wrong input!!!");
                    // performs an error if neither is used
                }

            } while (!yesOrNo.equalsIgnoreCase("y") && !yesOrNo.equalsIgnoreCase("n")  );
            //if the user doesn't choose y OR n it will run the code again at the verification

        } while (!yesOrNo.equalsIgnoreCase("y") );
        //If the user doesn't input y it will run the code again at the beginning


        System.out.println(newAccountID + " " + newPasswordID); // displays the new account and password







        System.out.println();

        System.out.println("End of addNewAccount");

    }
}
