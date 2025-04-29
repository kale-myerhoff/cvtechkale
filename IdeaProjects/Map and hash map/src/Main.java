import java.util.HashMap;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        HashMap<String, Integer> empIds = new HashMap<>();

        empIds.put("Bartolomeo", 12345);
        empIds.put("Adeline", 12346);
        empIds.put("Carlyetta", 12347);

        System.out.println(empIds);
        System.out.println(empIds.get("Bartolomeo"));
        System.out.println(empIds.containsKey("Jerry"));

        empIds.put("Carlyetta", 84112);
        System.out.println(empIds);

        empIds.replace("lordFuckwad", 6969696);
        System.out.println(empIds);

        empIds.putIfAbsent("lordFuckwad", 6969696);
        System.out.println(empIds);



    }
}