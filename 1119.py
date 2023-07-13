def processOneFile(filename):# 写一个函数，传进去一个文件名，然后矗立着一个文件
    import pandas as pd
    data1 = pd.read_excel(f"{filename}", usecols='I')
    data2 = pd.read_excel(f"{filename}", usecols='J')
    sum1 = data1.sum()
    sum2 = data2.sum()
    oneValue = float(sum1) - float(sum2)
    print(filename.split("_")[1].split(".")[0], "对应的应收款项-实收款项=", oneValue)
    return oneValue

def filePath():
    from pathlib import Path
    folder_path = Path('C:\\Users\\pkuco\\Desktop\\codes\\pycharm_test\\')#这里写你自己的文件夹路径，注意改成两个反斜杠
    file_list = folder_path.glob('*.xlsx*')#这里写文件的后缀名
    lists = [] #把所有的文件名放进lists里面
    for i in file_list:  # 遍历已获取的文件路径
        file_name = i.name  # 提取工作簿的文件名
        lists.append(file_name)  # 将已提取的文件名添加到列表中
    return lists

paths = filePath()
for path in paths:
    processOneFile(path)

