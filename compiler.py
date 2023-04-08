import os

program_counter = 0
print_str = ""
compile_lines = []
compile_file = "none"
print_count = 0
strings = []
str_add = ""
str_count = 0
str_print_str = ""
str_print_count = 0
print_var = ""

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
        elif compile_lines[program_counter].startswith("    STR "):
            str_count = 8
            for letter in range(len(compile_lines[program_counter]) - 8):
                str_add = str_add + compile_lines[program_counter][str_count]
                str_count += 1
            strings.append(str_add)
            str_add = ""
            str_count = 0
        elif compile_lines[program_counter].startswith("    STINT "):
            str_print_count = 10
            for letter in range(len(compile_lines[program_counter]) - 10):
                str_print_str = str_print_str + compile_lines[program_counter][str_print_count]
                str_print_count += 1
            print_var = int(str_print_str)
            print(strings[print_var])
            print_var = 0
            str_print_count = 0
            str_print_str = ""
        program_counter += 1