import json
import csv
import os

# 定义字段名映射
FIELD_MAPPING = {
    "F_DrugId": "药品ID",
    "F_DrugName": "药品名称",
    "F_DrugNumber": "药品编号",
    "F_DrugSpec": "药品规格",
    "F_PreparaUnit": "制剂单位",
    "F_DrugForm": "剂型",
    "F_PackUnit": "包装单位",
    "F_DrugFormCount": "剂型数量",
    "F_DrugCategory": "药品类别",
    "F_AnticType": "抗菌药物类型",
    "F_DrugDirectoryType": "药品目录类型",
    "F_TempMedinsCode": "临时医保编码",
    "F_DrugDirectoryCode": "药品目录编码",
    "F_DrugPrice": "药品价格",
    "F_TempPrice": "临时价格",
    "F_RetailUnit": "零售单位",
    "F_Dmin": "最小剂量",
    "F_OnceUsing": "单次用量",
    "F_SpecUnit": "规格单位",
    "F_DrugChangjia": "药品厂家",
    "F_ApprovalNumber": "批准文号",
    "F_LimitUseSign": "限制使用标志",
    "F_LimitUseScope": "限制使用范围",
    "F_Hosipital": "医院",
    "F_EnabledMark": "启用标志",
    "F_EnabledName": "启用名称",
    "F_IsAudit": "是否审核",
    "F_PurchasePrice": "采购价格",
    "F_AuditTime": "审核时间",
    "F_AuditPrice": "审核价格",
    "F_AuditMedInsCode": "审核医保编码",
    "F_StockUnit": "库存单位",
    "F_StockDmin": "库存最小剂量",
    "F_PriceRatio": "价格比例",
    "F_AuditRatio": "审核比例",
    "F_LastModifyTime": "最后修改时间"
}

def convert_json_to_csv(json_file_path, csv_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f_json:
            data = json.load(f_json)
    except FileNotFoundError:
        print(f"错误：未找到JSON文件 {json_file_path}")
        return
    except json.JSONDecodeError:
        print(f"错误：JSON文件 {json_file_path} 格式无效")
        return

    if 'list' not in data or not isinstance(data['list'], list):
        print(f"错误：JSON文件 {json_file_path} 结构不符合预期，缺少 'list' 键或其值不是列表")
        return

    drug_list = data['list']
    if not drug_list:
        print(f"警告：JSON文件 {json_file_path} 中的药品列表为空")
        # 创建一个空的CSV文件，但包含表头
        with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as f_csv:
            if FIELD_MAPPING:
                writer = csv.writer(f_csv)
                writer.writerow(FIELD_MAPPING.values())
        return

    # 获取所有可能的原始字段名，以确保CSV表头完整性
    all_original_keys = set()
    for item in drug_list:
        all_original_keys.update(item.keys())
    
    # 根据FIELD_MAPPING生成有序的中文表头，未在MAPPING中的字段将保持原样并放在末尾
    header_chinese = []
    processed_original_keys = set()

    # 先添加在MAPPING中定义的字段
    for original_key in FIELD_MAPPING.keys():
        if original_key in all_original_keys:
            header_chinese.append(FIELD_MAPPING[original_key])
            processed_original_keys.add(original_key)
    
    # 添加不在MAPPING中但存在于数据中的字段
    remaining_keys = sorted(list(all_original_keys - processed_original_keys))
    header_chinese.extend(remaining_keys) # 将这些字段名直接作为表头

    # 构建一个从原始键到中文键的完整映射，用于数据行转换
    full_key_map = {**FIELD_MAPPING}
    for key in remaining_keys:
        full_key_map[key] = key # 未映射的字段使用原名

    # 确保输出目录存在
    output_dir = os.path.dirname(csv_file_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as f_csv:
        writer = csv.DictWriter(f_csv, fieldnames=header_chinese)
        writer.writeheader()

        for item in drug_list:
            translated_item = {}
            for original_key, value in item.items():
                chinese_key = full_key_map.get(original_key, original_key) # 如果原始键不在映射中，则使用原始键
                translated_item[chinese_key] = value
            writer.writerow(translated_item)
    
    print(f"成功将 {json_file_path} 转换为 {csv_file_path}")

if __name__ == '__main__':
    json_input_path = r'd:\medical\medical-ai-prescription\input\龙华药品.json'
    csv_output_path = r'd:\medical\medical-ai-prescription\output\龙华药品_cn.csv'
    convert_json_to_csv(json_input_path, csv_output_path)