

# Import Panel
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Control Center
color_square=Fore.BLUE
color_title=Fore.MAGENTA
color_thanking=Fore.GREEN

line = '| '
no_line = ''
line_main=line

speed_main=0.07
speed_other=1.5

# Main Code
def main_function(a):
    print()
    y = 1

    title_name ='Multiplication Table'
    head_space = int((a*(4+len(line_main))))
    title = title_name.center(head_space,'-')
    print(color_title+(' '+'x'+title+'x'))
    print()
    time.sleep(speed_other)

    for j in range(1, a + 1):
        x = 1
        print('  ', end='')

        for i in range(1, a + 1):
            mul = y * x
            str_mul = str(mul)
            space = ' ' * (3 - len(str_mul))

            if x == y:
                print(color_square + f'{str_mul}{space}',line_main, end='')
            else:
                print(f'{str_mul}{space}',line_main, end='')
            time.sleep(speed_main)

            x = x + 1
        y = y + 1
        print('\r')
    print()
    if 5 <= s <= 20 and s % 1 == 0:
        time.sleep(speed_other)
        thanking_name = ('JazakAllah')
        thanking_space = int((a * (4 + len(line_main))))
        thanking = thanking_name.center(thanking_space, '-')
        print(color_thanking + ' ' + 'x' + thanking + 'x')

# Error Center
while True:
    user = input(' Enter a number up to 20 : ')
    try:
        s=eval(user)
        if 5 <= s <= 20 and s % 1 == 0:
            main_function(s)
            break
        elif s<5 and s % 1 == 0:
            main_function(s)
            time.sleep(2)
            print(Fore.BLUE+' For better results type a natural number from 5 to 20.')
            time.sleep(2)
            print()
        else:
            print(Fore.RED + ' Type a positive natural number less than or equal to 15.')
            print()
            time.sleep(2)

    except NameError:
        print(Fore.RED+' Type a number.')
        print()
        time.sleep(2)
    except SyntaxError:
        print(Fore.RED+' Type a number.')
        print()
        time.sleep(2)
    except ValueError:
        print(Fore.RED + ' Type a number.')
        print()
        time.sleep(2)

time.sleep(40)