with open('diary.txt', 'r', encoding='utf-8') as file:

    content = file.read()
    print('文件内容：\n', content)

    file.seek(0)  #重置文件指针到开头
    #逐行读取

    print('\n逐行内容：')
    for line in file:
        print(line.strip())    #strip()去除末尾空白