# print-formatted-numbers
Prints numbers in decimal, octal, hexadecimal, and binary using manual conversions.

# Number Formatter

A Python program that prints numbers from 1 to *n* in decimal, octal, hexadecimal (uppercase), and binary formats — all right-aligned.

## Features

- Manual base conversion without using built-in functions like `bin()`, `oct()`, or `hex()`
- Custom formatting with aligned output
- Easy to understand code demonstrating loops, conditions, and string formatting

## How to run

  1. Clone the repository:
 
    https://github.com/savinu-pixel/print-formatted-numbers/tree/main

  2.Run the script:

     python formatter.py

  3.Enter a positive integer when prompted,
          
      e.g.: 10
  
  4.The program will print:

      1 1 1 1
      2 2 2 10
      3 3 3 11
      4 4 4 100
      5 5 5 101
      6 6 6 110
      7 7 7 111
      8 10 8 1000
      9 11 9 1001
      10 12 A 1010


    -----------------Code snippet-----------------
    ----------------------------------------------
    def to_base(num, base):
        digits = "0123456789ABCDEF"
        result = ""
        while num > 0:
            result = digits[num % base] + result
            num //= base
        return result or "0"
    
    def print_formatted(number):
        width = len(to_base(number, 2))
        for i in range(1, number + 1):
            print(
                str(i).rjust(width),
                to_base(i, 8).rjust(width),
                to_base(i, 16).rjust(width),
                to_base(i, 2).rjust(width),
            )
    
    if __name__ == "__main__":
        n = int(input())
        print_formatted(n)
    ----------------------------------------------
  



