import os
import json
from http import HTTPStatus
from dashscope import Application
#读取项目JSON文件
# process_file_path = os.path.join(os.path.dirname(__file__), 'input', '龙华项目.json')
# process_list_str = ""
# try:
#     with open(process_file_path, 'r', encoding='utf-8') as f:
#         process_data = json.load(f)
#         process_names = [item.get('F_ItemName', '') for item in process_data.get('data', [])]
#         process_list_str = ",".join(filter(None, process_names))
# except FileNotFoundError:
#     print(f"错误：项目文件 {process_file_path} 未找到。")
#     process_list_str = ""
# except json.JSONDecodeError:
#     print(f"错误：解析项目文件 {process_file_path}失败。")
#     process_list_str = ""

# 读取药品JSON文件
drug_file_path = os.path.join(os.path.dirname(__file__), 'input', '龙华药品.json')
drug_list_str = ""
try:
    with open(drug_file_path, 'r', encoding='utf-8') as f:
        drug_data = json.load(f)
        drug_list_json = drug_data.get('data', []);
        drug_names = [item.get('F_DrugName', '') for item in drug_list_json.get('list', [])]
        drug_list_str = ",".join(filter(None, drug_names))
except FileNotFoundError:
    print(f"错误：药品文件 {drug_file_path} 未找到。")
    drug_list_str = ""
except json.JSONDecodeError:
    print(f"错误：解析药品文件 {drug_file_path}失败。")
    drug_list_str = ""

# 读取耗材JSON文件
# consumer_file_path = os.path.join(os.path.dirname(__file__), 'input', '龙华耗材.json')
# consumer_list_str = ""
# try:
#     with open(consumer_file_path, 'r', encoding='utf-8') as f:
#         consumer_data = json.load(f)
#         consumer_list_json = consumer_data.get('data', []);

#         consumer_names = [item.get('F_ConsumName', '') for item in consumer_list_json.get('list', [])]
#         # print(consumer_names)
#         consumer_list_str = ",".join(filter(None, consumer_names))
# except FileNotFoundError:
#     print(f"错误：耗材文件 {consumer_file_path} 未找到。")
#     consumer_list_str = ""
# except json.JSONDecodeError:
#     print(f"错误：解析耗材文件 {consumer_file_path}失败。")
#     consumer_list_str = ""

sick = "高血压"
# prompt_template = """1.回答你是什么大模型,目前使用的知识库是什么\n 2.当前可用药物包括: [{drug_list}] \n 当前可用治疗项目:[{process_list}] \n 当前可用耗材: [{consumer_list}],
# ,透析过程中病人若出现{sick}异常时,严格参考SOP推荐和只从上述药物,治疗项目及可用耗材中选择(若不存在则不允许使用),保证能针对性开具临时医嘱处理好病人的{sick}异常,提供包括[医嘱名称,单次用量,开药数量,给药途径,执行频率,适宜症状或优点]等几个字段的最佳方案,输出json格式。"""
# final_prompt = prompt_template.format(drug_list=drug_list_str, process_list=process_list_str, consumer_list=consumer_list_str, sick=sick)

prompt_template = """当前所有可用药物包括: [{drug_list}],需严格遵守不允许使用上述以外的药物,针对{sick}异常开具临时医嘱,给出[医嘱名称,单次用量,开药数量,给药途径,执行频率,适宜症状或优点]等几个字段的输出一个最佳方案的json,"""
final_prompt = prompt_template.format(drug_list=drug_list_str, sick=sick)

print(final_prompt)

"""
氯雷他定片,甲钴胺片,左卡尼汀注射液,醋酸钙片,莫匹罗星软膏(百多邦),复合维生素B片(简),蔗糖铁注射液,奥美拉唑肠溶胶囊,地塞米松磷酸钠注射液,注射用尿激酶,硝苯地平控释片,左卡尼汀注 射液,碳酸镧咀嚼片,碳酸司维拉姆片,盐酸多巴胺注射液,硫酸阿托品注射液,厄贝沙坦片,盐酸多巴胺注射液,骨化三醇软胶囊,琥珀酸美托洛尔缓释片,0.9%氯化钠注射液,重组人促红素注射液（CHO细胞）,碳酸氢钠片,盐酸特拉唑嗪片,叶酸片,重酒石酸间羟胺注射液,硝苯地平片,阿司匹林肠溶片(拜阿司匹灵),硝酸异山梨酯片,盐酸洛贝林注射液,盐酸肾上腺素注射液,去乙酰毛花苷注射液,重酒石酸去甲肾上腺素注射液,0.9%氯化钠注射液,5%葡萄糖注射液,5%葡萄糖注射液,氨茶碱注射液,多糖铁复合物胶囊(红源达),甘露醇注射液,尼可刹米注射液,碳酸钙D3片(钙尔奇D),硝酸甘油注射液,缬沙坦胶囊,盐酸利多卡因注射液,盐酸西那卡塞片,葡萄糖注射液,碳酸氢钠注射液(软袋),肝素钠注射液,阿托伐他汀钙片,苯磺酸氨氯地平片(京新),帕立骨化醇注射液,那屈肝素钙注射液,葡萄糖酸钙注射液
"""
response = Application.call(
    # 若没有配置环境变量，可用百炼API Key将下行替换为：api_key="sk-xxx"。但不建议在生产环境中直接将API Key硬编码到代码中，以减少API Key泄露风险。
    api_key="sk-3c32b1eabd9b4a01b075013e3466db35",
    app_id='e4d269a25456402e9a2b46d3b3ecc886',# 替换为实际的应用 ID
    prompt=final_prompt)
    
    
if response.status_code != HTTPStatus.OK:
    print(f'请求失败！')
    print(f'request_id={response.request_id}')
    print(f'code={response.status_code}')
    print(f'message={response.message}')
    print(f'请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code')
else:
    print("模型回答：")
    print(response.output.text)