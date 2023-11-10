# import pandas as pd
# import json

# # Read data from the Excel file
# excel_file_path = r'E:\Bhagy\Projects\Tothiq\tothiq-python-api\Translated Under Review-Tothiq-Web-Individual-Business-Users-panel-Labels-Tothiq-Team-10-08-2023 (1) (1).xlsx'
# df = pd.read_excel(excel_file_path)

# fixture_data = []

# for idx, row in df.iterrows():
#     fixture_entry = {
#         "model": "masterapp.languages_label",
#         "pk": idx + 1,
#         "fields": {
#             "code": row["Label Name"],
#             "english": row["English Label"],
#             "arabic": row["Arbic Label"]
#         }
#     }
#     fixture_data.append(fixture_entry)

# fixture_file_path = "languages_label_fixture.json"

# with open(fixture_file_path, "w", encoding="utf-8") as f:  # Specify utf-8 encoding
#     json.dump(fixture_data, f, indent=4, ensure_ascii=False)  # Set ensure_ascii to False

# print(f"Fixture file generated at {fixture_file_path}")





##################################################################################################################################################




# import pandas as pd
# from masterapp.models import languages_label  # Replace 'myapp' with your app name

# # Load the Excel file into a DataFrame
# excel_file_path = 'C:\Users\HP\Downloads\Final label v1.xlsx'  # Replace with the path to your Excel file
# df = pd.read_excel(excel_file_path)

# # Set the primary key starting value
# next_id = 748

# # Iterate over rows in the DataFrame and create model instances
# for index, row in df.iterrows():
#     code = row['Code']
#     english = row['English']
#     arabic = row['Arabic']

#     # Create a new languages_label instance and set the primary key
#     label = languages_label(code=code, english=english, arabic=arabic, id=next_id)
    
#     # Save the instance to the database
#     label.save()

#     # Increment the primary key value
#     next_id += 1

# print("Data imported into languages_label model.")





import pandas as pd
import json

# Load the Excel file into a DataFrame
excel_file_path = 'C:/Users/HP/Downloads/Final label v1.xlsx'
df = pd.read_excel(excel_file_path)

# Create a list to hold the fixture data
fixture_data = []

# Iterate over rows in the DataFrame and create fixture entries
for index, row in df.iterrows():
    entry = {
        'model': 'masterapp.languages_label',  # Replace 'myapp' with your app name
        'pk': index + 747,  # Set the primary key value based on your requirement
        'fields': {
            'code': row['Code'],
            'english': row['English'],
            'arabic': row['Arabic']  # Set the 'arabic' field to null as per your requirement
        }
    }
    fixture_data.append(entry)

# Write the fixture data to a JSON file
fixture_file_path = 'E:/Bhagy/Projects/Tothiq/tothiq-python-api/fixturev1.json'  # Replace with the desired output path
with open(fixture_file_path, 'w') as fixture_file:
    json.dump(fixture_data, fixture_file, indent=4)

print(f"Fixture data saved to {fixture_file_path}")