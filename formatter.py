def print_formatted(number):
    #find binary value of  entered number
    max_binary = ""
    binary_num = number 
    while binary_num > 0:
        max_binary = str(binary_num % 2) + max_binary
        binary_num = round((binary_num - (binary_num % 2)) / 2)
    width = len(max_binary)

    count = 1
    while count<=number:

        # Binary calculation
        binary = ""
        is_running = True
        binary_num  = count
        while is_running:
            binary = str(binary_num % 2) + binary
            binary_num = round((binary_num - (binary_num % 2)) / 2)
            if binary_num < 1:
                is_running = False

        # Octal calculation
        octal = ""
        is_running = True
        octal_num = count
        while is_running:
            octal = str(octal_num % 8) + octal
            octal_num = round((octal_num - (octal_num % 8)) / 8)
            if octal_num < 1:
                is_running = False

        # Hexadecimal (capitalized)
        hexadecimal = ""
        is_running = True
        hexadecimal_num = count
        while is_running:
            value = ""
            common_division = (hexadecimal_num % 16)
            if 10 <= common_division <= 15:
                if common_division == 10:
                    value = "A"
                elif common_division == 11:
                    value = "B"
                elif common_division == 12:
                    value = "C"
                elif common_division == 13:
                    value = "D"
                elif common_division == 14:
                    value = "E"
                else:
                    value = "F"
            else:
                value = str(hexadecimal_num % 16)
            hexadecimal = value + hexadecimal
            hexadecimal_num = round((hexadecimal_num - (hexadecimal_num % 16)) / 16)
            if hexadecimal_num < 1:
                is_running = False

        print( f"{count}".rjust(width),f"{octal}".rjust(width),f"{hexadecimal}".rjust(width),f"{binary}".rjust(width))
        count+=1




if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
