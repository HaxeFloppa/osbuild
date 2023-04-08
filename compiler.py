import os
import sys

program_counter = 0
print_str = ""
compile_lines = []
compile_file = "none"
print_count = 0
strings = []
integers = []
str_add = ""
str_count = 0
str_print_str = ""
str_print_count = 0
print_var = ""
int_count = 0
int_add_str = ""
int_add = 0
throw_count = 0
throw_error = ""
int_print_count = 0
int_print_str = ""
int_print = 0

os.system("clear")
while True:
    prompt = input("Type in a file name (no format) > ")
    compile_file = open(f'{prompt}.os', 'r')
    for line in compile_file:
        compile_lines.append(line)
    for line in compile_lines:
        if compile_lines[program_counter] == "BOOTLOADER_PRINT":
            if compile_lines[program_counter + 1] == "{":
                print("START")
        elif compile_lines[program_counter] == "}":
            print("END")
        elif compile_lines[program_counter].startswith("    DISPLAY"):
            print_count = 11
            for letter in range(len(compile_lines[program_counter]) - 11):
                print_str = print_str + compile_lines[program_counter][print_count]
                print_count += 1
            print(print_str)
            print_str = ""
            print_count = 0
        elif compile_lines[program_counter].startswith("    STR_DEF "):
            str_count = 12
            for letter in range(len(compile_lines[program_counter]) - 12):
                str_add = str_add + compile_lines[program_counter][str_count]
                str_count += 1
            strings.append(str_add)
            str_add = ""
            str_count = 0
        elif compile_lines[program_counter].startswith("    STRING_CALL"):
            str_print_count = 15
            for letter in range(len(compile_lines[program_counter]) - 15):
                str_print_str = str_print_str + compile_lines[program_counter][str_print_count]
                str_print_count += 1
            print_var = int(str_print_str)
            print(strings[print_var])
            print_var = 0
            str_print_count = 0
            str_print_str = ""
        elif compile_lines[program_counter].startswith("    INT_DEF"):
            int_count = 11
            for letter in range(len(compile_lines[program_counter]) - 11):
                int_add_str = int_add_str + compile_lines[program_counter][int_count]
                int_count += 1
            int_add = int(int_add_str)
            integers.append(int_add)
            int_add_str = ""
            int_add = 0
            int_count = 0
        elif compile_lines[program_counter].startswith("    THROW"):
            throw_count = 9
            for letter in range(len(compile_lines[program_counter]) - 9):
                throw_error = throw_error + compile_lines[program_counter][throw_count]
                throw_count += 1
            print(f'Exceptional Error: {throw_error}. Therefore, the program will close.')
            throw_error = ""
            throw_count = 0
            sys.exit()
        elif compile_lines[program_counter].startswith("    INT_CALL"):
            int_print_count = 12
            for letter in range(len(compile_lines[program_counter]) - 12):
                int_print_str = int_print_str + compile_lines[program_counter][int_print_count]
                int_print_count += 1
            int_print = int(int_print_str)
            print(integers[int_print])
            int_print = 0
            int_print_str = ""
            int_print_count = 0
        program_counter += 1