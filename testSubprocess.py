import subprocess #สำหรับ run terminal command

if __name__ == "__main__":
    #subprocess.run(["ls", "-l"])
    # for i in [2, 5, 6, 8]:
    #     subprocess.run(['python', 'python_script_101.py', '9', '--x', f'{i}', '--yval', '5'])

    # pro = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    # out, err = pro.communicate()
    # print(out)


    #print เฉพาะตัวเลขผลลัพธ์การคูณโดยไม่แก้โปรแกรมเก่า
    for i in [2, 5, 6, 8]:
        pro = subprocess.Popen(['python', 'python_script_101.py', '9', '--x', f'{i}', '--yval', '2'], stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        out, err = pro.communicate()
        a = str(out).split("=")[2].split("\\r")[0]
        print(a)

