# palindrome_check
This program is about to check a palindrom number. 
There will be input from user, and program will giving output with "True" or "False" statement. 

Example: 
Input : 2552
Output : True

Input : -2552
Output : False

Input : 1000
Output : False

Input : 110011
Output : True

The process of this code is begin from input number from user. 
Then the number is store in variable that name temp.
Here i make a new variable that name temp_reverse to store the reverse number.
It begin from 0, so that I can use this continuously.
After I store severel variable that I mention, then i do looping to check digit and also to reverse number
The loop will end when the number changes is below 0. 
To calculate the digit, I use eliminate from every digit. Begin from units, then to dozens, then hundreds, and so on. 
How to eliminate is by using modulus of 10 first to number. And then i store the rest of number to temp_reverse. 
Now the number is become smaller, until the number goes to unit.

