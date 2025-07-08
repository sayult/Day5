import csv
with open('greads.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:

            score = int(row['成绩'])
            if not 0 <= score <= 100:
                raise ValueError('分数不合理！')
        except (ValueError , KeyError) as e:
            print(f'数据错误：学生{row.get('姓名' , '未知')} - {e}')
        else:
            print(f'有效数据：{row['姓名']} - {score}')