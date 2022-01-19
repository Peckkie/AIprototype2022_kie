import argparse #สำหรับ รับ input จากภายนอก
import subprocess #สำหรับ run terminal command

#import flask  #สำหรับ ทำ web app และ web service

def print_orther():
    print('something else')

def parse_input():
    parser = argparse.ArgumentParser(description='test program to learn about argparse and subprocess')
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
        default = 3, #ถ้าไม่มี default ต้องใส่ input , เมื่อมี default เป็น input ที่ไม่จำเป็นเพราะมีค่า default อยู่แล้ว
        help = 'value of y')

    args = parser.parse_args()
    return args

if __name__ == "__main__": #main function
    
    args = parse_input()

    x = args.x
    y = args.yval
    print(f'M = {args.M}')
    print(f'calculate {x} x {y} = {x*y}')

    #$python python_script_101.py 9 --x 11