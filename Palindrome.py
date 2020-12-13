def is_palindrome(num):
    temp = num
    temp_reverse=0
    while(num>0):
        digit=num%10
        temp_reverse = temp_reverse*10+digit
        num=num//10
    return print("True") if (temp == temp_reverse) else print("False")


bilangan = int(input("Bilangan: "))
is_palindrome(bilangan)
