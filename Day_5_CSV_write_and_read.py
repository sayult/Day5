import csv

#文件创建
students = [
    {'学号': '114514', '姓名':'李田所', '成绩':'80'},
    {'学号': '114515', '姓名':'李田所一', '成绩':'90'},
    {'学号': '114516', '姓名':'李田所二', '成绩':'100'},
]

#文件写入(以CSV格式)
with open('greads.csv', 'w', encoding='utf-8', newline='') as file:
    fieldnames = ['学号', '姓名', '成绩']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

#文件读取
with open('greads.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f'学生：{row['姓名']}, 成绩：{row['成绩']}')













