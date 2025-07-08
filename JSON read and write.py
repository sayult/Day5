import json

student_data = {
    'name': '李田所',
    'courses': ['Python', '数据结构','算法'],
    'scores':{'Python' : 90,'数据结构':90},
    'is_active': True
}

with open('student.json', 'w', encoding='utf-8') as file:
    #json.dump()：将Python对象序列化为JSON并写入文件    ensure_ascii=False：允许直接存储非ASCII字符（如中文）
    #indent=2：使用2空格缩进格式化输出，提高可读性
    json.dump(student_data, file, ensure_ascii=False, indent=2)

with open('student.json', 'r', encoding='utf-8') as file:
    data = json.load(file)     #json.load(file)：从文件加载JSON数据并解析为Python对象
    print(f'学生：{data['name']}')#访问顶层键值
    print(f'Python成绩:{data['scores']['Python']}')


