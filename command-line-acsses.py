import subprocess
import sys
import turtle





while True:
    try:
        command = input(">>> ")

        if command == "rm -rf":
            print("Forbidden command")
            sys.exit()
        
        output = subprocess.check_output(command, shell=True, text=True)

        print(output)

    except:
        pass
    if command == "exit":
        sys.exit()