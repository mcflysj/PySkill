import pandas as pd
import json

# 从文件读取JSON数据
with open('data2.json', 'r') as file:
    json_data = json.load(file)

# 提取数据
table_data = json_data['tables_result'][0]['body']

# 创建数据框
df = pd.DataFrame(columns=['科目', '院校专业', '要求', '组代码', '专业代码', '院校专业组及专业名称', '收费标准', '计划', '学制', '备注'])

# 填充数据
row_data = []
for row in table_data:
    words = row['words'].split('\n')
    if len(words) == len(df.columns):
        row_data.append(words)
    else:
        # 处理跨越多行的单元格
        prev_row = row_data[-1]
        start_index = len(prev_row) - len(df.columns) + 1
        if start_index >= 0:
            merged_row = prev_row[:start_index] + [prev_row[start_index] + ' ' + ' '.join(words)] + words[start_index+1:]
            merged_row = merged_row[:len(df.columns)]  # 修复可能超出列数的问题
            row_data[-1] = merged_row
        else:
            print("异常行数据:", words)

# 将数据添加到数据框
for row in row_data:
    df.loc[len(df)] = row

# 保存为Excel文件
df.to_excel('output.xlsx', index=False)
# 写入日志
print(f"数据已成功写入Excel文件")




