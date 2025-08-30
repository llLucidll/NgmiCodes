public class FizzBuzz {
    
    // This method decides what to print for each number
    public String evaluate(int number) {
        // We start our conditions with 15 (divisble by 3 and 5)
        if (number % 15 == 0) {
            return "FizzBuzz";
        } 
        if (number % 5 == 0) {
            return "Buzz";
        } 
        if (number % 3 == 0) {
            return "Fizz";
        }

        return String.valueOf(number);
    }

    public void printSequence(int n) {
        for (int i = 1; i <= n; i++) {
            System.out.println(evaluate(i));
        }
    }
    
    public static void main(String[] args) {
        FizzBuzz fizzBuzz = new FizzBuzz();
        fizzBuzz.printSequence(100);
    }
}