/**
 * Recursion is when you break down a problem into smaller bits and make the function call itself to compute the result.
 * There are two types of recursion:
 * Once branch
 * Two branch
 */
public class Recursion {
    /**
     * Formula: n! = n * (n-1)!
     * Example: 5! = 5 * 4! and so on.
     * Base case: 0(n)
     * Time complexity: 0(n)
     * Space complexity: 0(n)
     */
    public int recursiveFactorial(int n) {
        if(n <= 1) {
            return 1;
        }
        return n * recursiveFactorial(n - 1);
    }

    /**
     * Finds the factorial with iteration
     * @return result of factorial of n
     */
    public int iterativeFactorial(int n) {
        int result = 1;

        while(n > 1) {
            result = result * n;
            n--;
        }
        return result;
    }


    /**
     * Formula: F(n): F(n-1) + F(n-2)
     * This is asn example of two branch recursion
     * Base case: F(0) = 0, F(1) = 1
     */
    public int calculateFibonacci(int n) {
        if(n <= 1) {
            return n;
        }

        return calculateFibonacci(n - 1) + calculateFibonacci(n - 2);
    }
}
