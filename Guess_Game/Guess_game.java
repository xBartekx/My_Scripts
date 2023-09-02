import java.io.IOException;

public class GuessGame {
    public static void main(String[] args) throws IOException {

        char ch, ignore, answer = 'k';

        do {
            System.out.println("I'am thinking about a letter from compartment of 'A' to 'Z'.");
            System.out.println("Try to guess what letter it is:");

            ch = (char) System.in.read();

            do {
                ignore = (char) System.in.read();
            }
            while(ignore != '\n');

            if (ch == answer) {
                System.out.println("Great! This is that letter!");
            } else {
                System.out.println("...This is not that letter. ");
                if (ch < answer == true) {
                    System.out.println("Too low.");
                } else {
                    System.out.println("Too high.");
                }
            }
        }
        while
        (answer != ch);

    }
}
