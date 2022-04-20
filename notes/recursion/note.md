## What is recursion
- always have a base case to end the problem
- backtrack when go to the end
- The same function fact is called multiple times
- Different frames keep track of the different arguments in each call
- What n evaluates to depends on which is the current enviornment
- Each call to fact solves a simpler problem than the last: smaller n

## Iteration vs Recursion
- Iteration is a special case of recursion

## Verify?
- verify the base case(s)
- Think of the fun is functional abstraction -> implementation
- Assume smaller n is correct
- Verify that n is correct based on above assumption

## Mutual Recursion
- two functions call each other
- The luhn Algorithm -> checksum for the credit card

## Convert Recursion to Iteration
- what state(passed into the recursive fun) must be maintained by the iterative function

## Convert Iteration to Recursion
- updates via assignment become arguements to a recursive call
