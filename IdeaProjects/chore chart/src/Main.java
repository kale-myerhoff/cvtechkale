import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // set how many people there is going to be and how many weeks generated X

        // run code that gets a name and adds it to an array X

        // generate an amount of chores based on the amount of people using a point value that will
        //have different amounts of required points based on the amount of people present (im thinking dividing the total amount of
        // points by the amount of people)

        // print this data to an external text file

        //run this code for a set number of weeks

        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        //hashmap//
        HashMap<String, Integer> hashMap = new HashMap<>();
        hashMap.put("chore 1", 1);
        hashMap.put("chore 2", 1);
        hashMap.put("chore 3", 1);
        hashMap.put("chore 4", 1);
        hashMap.put("chore 5", 1);
        hashMap.put("chore 6", 1);
        hashMap.put("chore 7", 1);
        hashMap.put("chore 8", 1);
        hashMap.put("chore 9", 1);
        hashMap.put("chore 10", 1);
        hashMap.put("chore 11", 1);
        hashMap.put("chore 12", 1);
        hashMap.put("bigChore 1", 4);
        hashMap.put("bigChore 2", 4);
        hashMap.put("bigChore 3", 4);
        //hashmap//







        //variables start//
        int peopleNumb = 1;
        int totalWeekNumb = 1;
        boolean yesOrNo = false;
        int totalPoints = 0;
        int requiredPoints = 0;
        ArrayList<String> choreList = new ArrayList<>(hashMap.keySet());
        ArrayList<String> nameList = new ArrayList<>();

        //variables end//






        for ( int y: hashMap.values()) {
            totalPoints = totalPoints + y;
        }

        System.out.println("Welcome to the chore chart generator!");
        System.out.println(" ");

        // amount of people and weeks//
        do {
        System.out.println("How many people are going to be included? :");
        try {
            peopleNumb = Math.abs(scanner.nextInt());
        } catch (Exception e) {
            System.out.println("ERROR!!! please use a valid number!");
        }

        System.out.println("Is " + peopleNumb + " people correct? :");
        if (scanner.nextLine().equalsIgnoreCase("yes") || scanner.nextLine().equalsIgnoreCase("y")) {
            yesOrNo = true;
        }

            } while (!yesOrNo); yesOrNo = false; // re-Asks the question if not given affirmative and resets yesOrNo to false afterward


        do {
        System.out.println("How many weeks are going to be generated? :");
        try {
        totalWeekNumb = Math.abs(scanner.nextInt());
        } catch (Exception e) {
            System.out.println("ERROR!!! please use a valid number!");
        }

        System.out.println("Is " + totalWeekNumb + " weeks correct? :");
        if (scanner.nextLine().equalsIgnoreCase("yes") || scanner.nextLine().equalsIgnoreCase("y")) {
            yesOrNo = true;
        }

            } while (!yesOrNo); yesOrNo = false; // re-Asks the question if not given affirmative and resets yesOrNo to false afterward

        requiredPoints = totalPoints / peopleNumb;
        //amount of people and weeks//


        //people names//
        for (int i = 1; i < peopleNumb + 1; i++ )/* for the amount of people selected run the code */ {
            System.out.println("what is person #" + i + "'s name? :");
            String name = scanner.nextLine();

            nameList.add(name);

            System.out.println("the current people added are :" + nameList);
            System.out.println();
        }
        //people names//


        //chores//
        for (int i = 0; i < nameList.size(); i++) {
            System.out.println(nameList.get(i));

            int currentPoints = 0;

            do {
                int selectedChore = random.nextInt(1, choreList.size());
                
                currentPoints += hashMap.get(choreList.get(selectedChore));
                System.out.println(hashMap.get(choreList.get(selectedChore)));
            } while (currentPoints < requiredPoints);




            
        }
        //chores//


        scanner.close();
        }
    }
