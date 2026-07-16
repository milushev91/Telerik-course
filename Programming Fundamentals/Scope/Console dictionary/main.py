import instruction_runner

line = input()

while line != "exit":

    instruction_runner.execute_instruction(line)
    line = input()
