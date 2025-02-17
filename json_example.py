import json

with open('data.json') as file:
    data = json.load(file)
    
    
# show the content of the file
print(data['students'])


with open("data_new.json", "w") as file:
    #saves a  dict (data) in a file (file) on JSON fromat
    json.dump(data, file, indent=3)
    
    
    


