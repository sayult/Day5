

try:
    #模拟可能出错的情况
    #进行一个小小的除法运算~
    num = int(input('请输入整数：'))
    result = 100 / num
    print(f'结果是：{result}')

except ValueError:    #值转换错误
    print('错误！请输入有效的整数！')
except ZeroDivisionError:   #除数为零
    print('错误，0不能作为被除数！')
except Exception as e:  #这部分代码的意思是：捕获所有类型的异常,并赋值给e。
     print(f'发生未知错误！{type(e).__name__} - {e}') #type(e).__name__：获取异常的具体类型名称（如 ValueError, KeyError 等）          
else:                                               #{e}：获取异常的详细信息（错误消息）
    print('计算成功完成！') 
finally: #finally 语句块是异常处理结构 (try-except-finally) 中的一个重要组成部分，它的作用是确保无论是否发生异常，其中的代码都会被执行。
    print('程序执行结束。')                                                         
                                                              
                                                               
    