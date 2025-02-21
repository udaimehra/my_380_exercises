project_ids = ['02134', '24253']
project_id = '02135'
present = False
for i in project_ids:
    if i == project_id:
        print(i)
        present = True
if not present:  
    project_ids.append(project_id)
print(project_ids)
