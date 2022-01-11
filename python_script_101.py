import argparse #สำหรับ รับ input
import subprocess #สำหรับ iyo terminal command

import flask  #สำหรับ ทำ web app และ web service

def print_orther():
    print('something else')
    
if __name__ == "__main__":  #main function
    parser = argparse.ArgumentParser(description='test program to learn about a  ')
    parser.add_argument(
        'M',
        type = int,
        help = 'value of x')

    parser.add_argument(
        '--x',
        type = int,
        help = 'value of x')

    parser.add_argument(
        '--yval', #--yval ตัวใหญ่ เล็ก ไม่มีผล
        type = int,
        default = 3,
        help = 'value of y')
    args = parser.parse_args()
    x = args.x
    y = args.yval
    print(f'M = {args.M}')
    print(f'calculate{x} x {y} = {x*y}')


    # print('test main function')
    # print_orther()