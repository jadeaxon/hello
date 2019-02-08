Feature: User can calculate the nth term in the Fibonacci series
  As a user
  I want to calculate the nth term in the Fibonacci series
  So that I know what the value is

  Scenario Outline: Value calculated for <number>
    Given I have a <number> as n
    When I pass n to the fib function
    Then It calculate the <result> as value of the nth term

    Examples:
      |number |result |
      |0      |0      |
      |1      |1      |
      |2      |1      |
      |3      |2      |
      |4      |3      |
      |8      |21     |
      |9      |34     |
      |51     |20365011074 |