import csv
import json
import os

# Directory containing JSON files
input_dir = 'input'
output_dir = 'output'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# File field mappings - define which fields to extract for each file type
field_mappings = {
    '龙华药品.json': ['F_DrugName', 'F_DrugNumber', 'F_DrugSpec', 'F_DrugPrice', 'F_DrugDirectoryType', 'F_Unit'],
    '龙华耗材.json': ['F_ConsumName', 'F_ConsumNumber', 'F_ConsumSpec', 'F_ConsumType', 'F_DrugPrice', 'F_Unit'],
    '龙华项目.json': ['F_ItemName', 'F_ItemType', 'F_UnitPrice', 'F_Unit', 'F_DrugDirectoryType']
}

# Process each JSON file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename.replace('.json', '.csv'))
        
        print(f"Processing {filename}...")
        
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Extract data based on file structure
                if 'list' in data.get('data', {}):
                    # Structure like 龙华药品.json and 龙华耗材.json
                    items = data['data']['list']
                else:
                    # Structure like 龙华项目.json
                    items = data.get('data', [])
                
                # Get fields for this file type or use all fields from first item
                fields = field_mappings.get(filename, None)
                if not fields and items:
                    fields = list(items[0].keys())
                
                with open(output_path, 'w', newline='', encoding='utf-8-sig') as out_f:
                    writer = csv.DictWriter(out_f, fieldnames=fields)
                    writer.writeheader()
                    
                    # Write only the specified fields for each item
                    for item in items:
                        row = {field: item.get(field, '') for field in fields}
                        writer.writerow(row)
                        
                print(f"Created {output_path} with {len(items)} rows and {len(fields)} columns")
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")