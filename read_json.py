
import os
import json
#读取药品JSON文件
print("------start----------")
process_file_path = os.path.join(os.path.dirname(__file__), 'input', '龙华项目.json')
process_list_str = ""
try:
    with open(process_file_path, 'r', encoding='utf-8') as f:
        process_data = json.load(f)
        process_names = [item.get('F_ItemName', '') for item in process_data.get('data', [])]
        process_list_str = ",".join(filter(None, process_names))
except FileNotFoundError:
    print(f"错误：项目文件 {process_file_path} 未找到。")
    process_list_str = ""
except json.JSONDecodeError:
    print(f"错误：解析项目文件 {process_file_path}失败。")
    process_list_str = ""
print(process_list_str)

print("------------------")
# 读取药品JSON文件
drug_file_path = os.path.join(os.path.dirname(__file__), 'input', '龙华药品.json')
drug_list_str = ""
try:
    with open(drug_file_path, 'r', encoding='utf-8') as f:
        drug_data = json.load(f)
        drug_list_json = drug_data.get('data', {}).get('list', [])
        drug_names = [item.get('F_DrugName', '') for item in drug_list_json]
        drug_list_str = ",".join(filter(None, drug_names))
except FileNotFoundError:
    print(f"错误：药品文件 {drug_file_path} 未找到。")
    drug_list_str = ""
except json.JSONDecodeError:
    print(f"错误：解析药品文件 {drug_file_path}失败。")
    drug_list_str = ""
print(drug_list_str)

print("------------------")
# 读取药品JSON文件
consumer_file_path = os.path.join(os.path.dirname(__file__), 'input', '龙华耗材.json')
consumer_list_str = ""
try:
    with open(consumer_file_path, 'r', encoding='utf-8') as f:
        consumer_data = json.load(f)
        consumer_list_json = consumer_data.get('data', []);

        consumer_names = [item.get('F_ConsumName', '') for item in consumer_list_json.get('list', [])]
        # print(consumer_names)
        consumer_list_str = ",".join(filter(None, consumer_names))
except FileNotFoundError:
    print(f"错误：药品文件 {consumer_file_path} 未找到。")
    consumer_list_str = ""
except json.JSONDecodeError:
    print(f"错误：解析药品文件 {consumer_file_path}失败。")
    consumer_list_str = ""
print(consumer_list_str)

print("---------end---------")