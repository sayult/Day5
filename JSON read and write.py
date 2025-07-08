import json

student_data = {
    'name': '李田所',
    'courses': 'Python',
    'scores': '114514',
    'is_active': True
}

with open('student.json', 'w', encoding='utf-8') as file:
    json.dump(student_data, file, ensure_ascii=False, indent=2)

with open('student.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(f'学生：{data['name']}')
    print(f'Python成绩:{data['scores']['Python']}')


