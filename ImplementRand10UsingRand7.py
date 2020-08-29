"""

Given the API rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10. You can only call the API rand7 and you shouldn't call any other API. Please don't use the system's Math.random().

Notice that Each test case has one argument n, the number of times that your implemented function rand10 will be called while testing.

Follow up:

    1. What is the expected value for the number of calls to rand7() function?
    2. Could you minimize the number of calls to rand7()?



Example 1:

Input: n = 1
Output: [2]

Example 2:

Input: n = 2
Output: [2,8]

Example 3:

Input: n = 3
Output: [3,8,10]



Constraints:

    1 <= n <= 10^5


"""
import random

def rand7():
    return random.randrange(1, 8)


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class ImplementRand10UsingRand7:
    def rand10(self) -> int:
        while True:
            ret = (rand7() - 1) * 7 + rand7()
            if ret <= 40:
                return ret % 10 if ret % 10 != 0 else 10



if __name__ == "__main__":
    n = 10
    test = ImplementRand10UsingRand7()
    print([test.rand10() for _ in range(n)])
