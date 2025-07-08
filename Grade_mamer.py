import json
import csv
import os

class GradeManager:

    def __init__(self, filename = 'grades.csv'):
        self.filname = filename
        self.students = []
        self.load_data()

#CSV文件数据加载与检测是否有文件数据
    def load_data(self):

        try:
            if os.path.exists(self.filname):
                with open(self.filname, 'r' , encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    self.students = list(reader)
                    print(f'成功加载 {len(self.students)}条学生记录')
            else:
                print('未找到文件数据，将创建新文件。')
        except Exception as e:
            print(f'文件加载失败！：{e}')
            self.students = []


    def save_data(self):

        try:
            with open(self.filname, 'w' , encoding='utf-8', newline='') as file:
                fieldnames = ['id', 'name', 'grade']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.students)
            print(f'成功保存 {len(self.students)}条记录')
        except Exception as e:
            print(f'保存失败：{e}')


    def add_student(self):

        try:
            student_id = input('学号：').strip()
            name = input('姓名:').strip()
            grade = float(input('成绩：'))

            if not 0 <= grade <= 100:
                raise ValueError('成绩必须在0-100之间！')
            
            if any(s['id'] == student_id for s in self.students):
                raise ValueError('学号已存在！')
            
            self.students.append({
                'id': student_id,
                'name': name,
                'grade': str(grade)
            })
            print('添加成功！')
        except ValueError as e:
            print(f'输入错误！：{e}')


    def export_to_json(self, json_file = 'grades,json'):

        try:

            export_data = {
                'count': len(self.students),
                'students': self.students,
                'average': self.calculate_average()
            }

            with open(json_file, 'w', encoding='utf-8') as file:
                json.dump(export_data, file, ensure_ascii=False, indent= 2)
                print(f'成功导出到{json_file}')
        except Exception as e:
            print(f'导出失败：{e}')


    def calculate_average(self):

        try:
            total = sum(float(s['grade']) for s in self.students)
            return round(total / len(self.students), 2) if self.students else 0
        except:
            return 0 
        
    def display_grades(self):

        if not self.students:
            print('暂无学生记录')
            return
        
        print('\n学生成绩单')
        print('-' * 30)
        print(f'{'学号':<10}{'姓名':<10}{'成绩':<6}')
        for student in self.students:
            print(f'{student['id']:<10}{student['name']:<10}{student['grade']:<6}')
            print('-' * 30)
            print(f'平均分：{self.calculate_average()}')


    def run(self):

        while True:
            print('\n学生成绩管理系统')
            print('1.添加学生')
            print('2.显示成绩单')
            print('3.保存数据')
            print('4.导出为JSON')
            print('5.退出系统')

            choice = input('请选择操作（1、2、3、4、5）')
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.display_grades()
            elif choice == '3':
                self.save_data()
            elif choice == '4':
                self.export_to_json()
            elif choice == '5':
                self.save_data()
                print('系统已保存与退出。')
            else:
                print('无效输入！')

if __name__ == '__main__':
    manager = GradeManager()
    manager.run()

            




            
                

