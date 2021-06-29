import requests
import json
def course_name():
    a = requests.get("https://join.navgurukul.org/api/partners")
    a1 = a.text
    # print(a1)
    with open("task.json","w") as f:
        python_dict=json.loads(a1)
        json.dump(python_dict,f,indent=4)
    with open("task.json","r") as f:
        data = json.load(f)
        # print(data)
    list_of_name=[]
    i=0
    while i<len(data["data"]):
        # print(i,"..",data["data"][i]["name"])
        list_of_name.append(data["data"][i]["name"])
        i+=1
    print(list_of_name)
course_name()