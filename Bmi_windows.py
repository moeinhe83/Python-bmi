# Body Mass Index Detection Program

# Imported Library
import os
from pyfiglet import figlet_format
from termcolor2 import colored
from datetime import datetime

# Clear Terminal 
os.system('cls')

# Function's For Secret Progtamming
def main():
    "Function's For Secret Progtamming"

    # Try For Programming
    try:
        'Try For Programming'

        # While For Programming
        while True:
            'While For Programming'

            # Wellcome
            print(colored('==============================', color='white'))
            print(colored(figlet_format('Wellcome'), color='cyan'))
            print(colored('==============================', color='white'))

            # Data For Referral time
            print(colored(f'Referral time : {datetime.now()}', color='green'))
            print(colored('==============================', color='white'))

            # Input Info Body
            body_weight = float(input('Please Enter Body weight(KG) :~$ '))
            body_height = float(input('Please Enter Body height(MTR) :~$ '))

            # Result
            bmi = (body_weight / (body_height ** 2))

            print(colored('==============================', color='yellow'))

            # If's For Result

            # Underweight
            if bmi <= 18.5:
                print(colored(f'Bmi your body :~$ {bmi}', color='magenta'))
                print(colored('==============================', color='white'))
                print(colored('Condition :~# ', color='cyan'))
                print(colored(figlet_format('Underweight'), color='yellow'))
                print(colored('==============================', color='white'))

            # Normal
            elif 18.5 < bmi < 24.9:
                print(colored(f'Bmi your body :~$ {bmi}', color='magenta'))
                print(colored('==============================', color='white'))
                print(colored('Condition :~# ', color='cyan'))
                print(colored(figlet_format('Normal'), color='green'))
                print(colored('==============================', color='white'))

            # Overweight
            elif 25 < bmi < 29.9:
                print(colored(f'Bmi your body :~$ {bmi}', color='magenta'))
                print(colored('==============================', color='white'))
                print(colored('Condition :~# ', color='cyan'))
                print(colored(figlet_format('Overweight 1'), color='red'))
                print(colored('==============================', color='white'))

            # Overweight
            elif 30 < bmi < 34.9:
                print(colored(f'Bmi your body :~$ {bmi}', color='magenta'))
                print(colored('==============================', color='white'))
                print(colored('Condition :~# ', color='cyan'))
                print(colored(figlet_format('Overweight 2'), color='red'))
                print(colored('==============================', color='white'))

            # Overweight
            elif 35 < bmi < 39.9:
                print(colored(f'Bmi your body :~$ {bmi}', color='magenta'))
                print(colored('==============================', color='white'))
                print(colored('Condition :~# ', color='cyan'))
                print(colored(figlet_format('Overweight 3'), color='red'))
                print(colored('==============================', color='white'))

            # Overweight
            elif bmi >= 40:
                print(colored(f'Bmi your body :~$ {bmi}', color='magenta'))
                print(colored('==============================', color='white'))
                print(colored('Condition :~# ', color='cyan'))
                print(colored(figlet_format('Overweight 4'), color='red'))
                print(colored('==============================', color='white'))

            # Please enter the correct values
            else:
                print(colored('Please enter the correct values !'))

            print(colored('==============================', color='yellow'))

            # Continues
            Continue_e = input('Try Again (y/n) :~$ ')
            if Continue_e == 'n' or Continue_e == 'N':
                break

            elif Continue_e == 'y' or Continue_e == 'Y':
                continue

            else:
                print(colored('Please Enter The Y Or N Character, By Default Break Proramming', color='red'))
                break

    # Except For Programming
    except:
        print(colored('Please Try again !', color='blue'))


# call Function's main
if __name__ == '__main__':
    main()

else:
    print(colored("You Can't Imported This program", color='red'))

# Create By Moein Heshmati
# Finish