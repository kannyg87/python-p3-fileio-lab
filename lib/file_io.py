def write_file(file_name, file_content):
    # with open(f'{file_name}.txt', 'w') as f:
    #     f.write(file_content)
    f = open(f'{file_name}.txt', 'w')
    f.write(file_content)
    f.close()

def append_file(file_name, append_content):
    f = open(f'{file_name}.txt', 'a')
    f.write(append_content)
    f.close()

def read_file(file_name):
    f= open(f'{file_name}.txt', 'r')
    content = f.read()
    f.close()
    return content
