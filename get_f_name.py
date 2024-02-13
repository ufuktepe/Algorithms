import os

def create_file(s):
    f_name = s.replace(' ', '_').lower() + '.py'
    print(f_name)
    f_path = os.path.join(os.getcwd(), 'l_code', f_name)
    f = open(f_path, 'w')
    f.close()


create_file('1004' + '_' + 'Max Consecutive Ones III')


