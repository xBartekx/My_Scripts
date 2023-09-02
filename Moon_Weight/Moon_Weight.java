import java.util.Scanner;

public class MoonWeight {
    public static void main(String[] args) {


        Scanner scanner1 = new Scanner(System.in);
        System.out.println("Enter your weight in kilograms: ");
        int weight = scanner1.nextInt();

        System.out.println("Your weight on Earth totals: " + weight + " kilograms");

    double bodyMassOnEarth;
    double weightOnTheMoon;
    double moonGravitation;
    double earthGravitaion;
    earthGravitaion = 9.807;
    moonGravitation = 1.62;

    bodyMassOnEarth = weight/earthGravitaion;
    weightOnTheMoon = bodyMassOnEarth * moonGravitation;
    weightOnTheMoon = Math.round(weightOnTheMoon);

        System.out.println("Your weight on the moon totals: " + weightOnTheMoon + " kilograms");





    }
}
