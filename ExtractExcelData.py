import xlrd
import xlwt
import os

wb = xlrd.open_workbook('C:\\Users\\Autobio-A3517\\Desktop\\test.xlsx') # 找到Excel表所在路径
table1 = wb.sheets()[0] # 选择Excel工作簿中的第1个工作表
n_rows = table1.nrows # 计算工作表的行数
n_cols = table1.ncols # 计算工作表的列数

def CreateTxt():
    for i in range(1,n_rows):
        name = table1.cell(i,1).value # 提取工作表第二列所有单元格内容
        path = 'C:\\Users\\Autobio-A3517\\Desktop\\test\\' # 定义输出的txt文档存放的位置
        full_path = path + str(name) + '.txt' # 以第二列单元格内命名.txt文件名
        SeqData = table1.cell(i,2).value  # 提取工作表中第3列中的基因序列数据
        with open(full_path,'w') as f:  # 打开已命名的.txt文件写入基因序列数据
            f.write(SeqData)         

if __name__=="__main__":
    CreateTxt()
    
        

    

