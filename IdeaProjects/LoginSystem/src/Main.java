public class Main {
    public static void main(String[] args) {



        // ask for username and password
        // have an option to create a new account

        IDandPasswords idandPasswords = new IDandPasswords();



        LoginPage loginPage = new LoginPage(idandPasswords.getLoginInfo());

        System.out.println();



        //


}}