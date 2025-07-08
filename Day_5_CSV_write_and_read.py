import csv

#文件创建
students = [
    {'学号': '114514', '姓名':'李田所', '成绩':'80'},
    {'学号': '114515', '姓名':'李田所一', '成绩':'90'},
    {'学号': '114516', '姓名':'李田所二', '成绩':'100'},
]

#文件写入(以CSV格式)                                                 #newline=''：禁用换行符转换（确保跨平台兼容性）
with open('greads.csv', 'w', encoding='utf-8', newline='') as file: #使用上下文管理器打开文件，确保文件操作结束后自动关闭
    fieldnames = ['学号', '姓名', '成绩']#定义CSV文件的列标题。
    writer = csv.DictWriter(file, fieldnames=fieldnames) #创建字典写入器对象。实际写入顺序由fieldnames决定，而非字典键顺序。

    writer.writeheader() #将字段名作为标题行写入CSV文件
    writer.writerows(students)#批量写入多行数据，每个字典必须包含fieldnames中定义的所有键。

#文件读取
with open('greads.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  #csv.DictReader()：创建字典读取器对象，将CSV的每一行转换为字典。使用CSV第一行作为字典的键，后续每行对应字典的值。
    for row in reader: #遍历CSV文件的每一行。row变量：每次迭代时，row包含当前行的字典数据。
        print(f'学生：{row['姓名']}, 成绩：{row['成绩']}')#row['姓名']：从当前行字典中获取"姓名"字段的值。













