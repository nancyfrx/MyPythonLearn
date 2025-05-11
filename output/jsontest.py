import json
import pandas as pd

# 序列化
data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["coding", "reading"],
    "is_student": False
}

# 将字典转为 JSON 字符串
json_str = json.dumps(data, indent=4)  # indent 格式化缩进
print(json_str)

# 写入 JSON 文件
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)




#反序列化
# JSON 字符串转字典
json_str = '{"name": "Bob", "age": 25}'
dict =json.loads(json_str)
print(dict["name"])  # 输出: Bob

# 从文件读取 JSON 数据
with open("data.json", "r") as f:
    data = json.load(f)
print(data["hobbies"])  # 输出: ["coding", "reading"]


#嵌套场景
json3 = '''
{
    "company": "Tech Corp",
    "employees": [
        {"name": "Alice", "role": "Engineer"},
        {"name": "Bob", "role": "Manager"}
    ]
}
'''
data = json.loads(json3)
print(data["employees"][0]["role"])  # 这里注意要加上中括号


#大文件处理
#快捷键注释 CMD + /
# with open("data.json","r") as fe:
#     for line in fe:
#         item = json.loads(line)


#CSV 和JSON 互转，使用pandas 第三方库
df = pd.read_json("data.json")
df.to_csv("data.csv",index=False)