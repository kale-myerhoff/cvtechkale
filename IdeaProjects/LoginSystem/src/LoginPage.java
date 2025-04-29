import java.util.HashMap;
import java.util.Objects;
import java.util.Scanner;

public class LoginPage {
        IDandPasswords input = new IDandPasswords(); //used to grab and send info to and from IDandPasswords

    HashMap<String, String> loginInfo = new HashMap<>();

    public LoginPage(HashMap<String, String> loginInfoOriginal) {
        loginInfo = loginInfoOriginal;
        Scanner scanner = new Scanner(System.in);
        String oldOrNewAccount;

        do {

            System.out.println("Input 1 to create a new account, input 2 to use existing account > ");

            oldOrNewAccount = scanner.nextLine();

            if (!oldOrNewAccount.equalsIgnoreCase("1") && !oldOrNewAccount.equalsIgnoreCase("2")){
                System.out.println("ERROR!!! not a valid input!!");
            }

        } while (!oldOrNewAccount.equalsIgnoreCase("1") && !oldOrNewAccount.equalsIgnoreCase("2")); //if neither options are chosen it reruns code

        if (oldOrNewAccount.equalsIgnoreCase("1")) {
            IDandPasswords.addNewAccount();
            loginTest();

        } else if (oldOrNewAccount.equalsIgnoreCase("2")) {
            loginTest();

        } else {
            System.out.println("ERROR!!! input not valid!");
        }
        scanner.close();
    }



    public static void loginTest() /*asks for and tests if the username and password is in the hashmap*/ {
        Scanner scanner =new Scanner(System.in);

        boolean userIsValid = false;
        boolean passwordIsValid = false ;

        String testUser = "test";
        String testPassword = "test";
        String userInput;
        String passwordInput;


        do {


            System.out.println("Please input your username > ");

            userInput = scanner.nextLine();

            System.out.println(userInput);

            if (Objects.equals(userInput, testUser)) {
                userIsValid = true;

            } else {
                System.out.println("Error username " + userInput + " does not exist!");
            }
        } while (!userIsValid); //if the username doesn't exist it asks again

        do {


            System.out.println("Please input your password for " + userInput + " > ");

            passwordInput = scanner.nextLine();

            System.out.println(passwordInput);

            if (Objects.equals(passwordInput, testPassword)) {
                passwordIsValid = true;
            } else {
                System.out.println("Error password " + passwordInput + " is not correct!");
            }
        } while (!passwordIsValid); // if username and password do not match it reports and asks again


        WelcomePage.welcome();
    }
}


