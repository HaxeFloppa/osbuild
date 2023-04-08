import os

program_counter = 0
print_str = ""
compile_lines = []
compile_file = "none"
print_count = 0

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
        elif compile_lines[program_counter].startswith("    "):
            print_count = 4
            for letter in range(len(compile_lines[program_counter]) - 4):
                print_str = print_str + compile_lines[program_counter][print_count]
                print_count += 1
            print(print_str)
            print_str = ""
            print_count = 0
        program_counter += 1