import os, json
from prompt import inst, example
from llm_api import llm_query

data = json.load(open('train.json', 'r'))
N = len(data)
print(data[0])

#把raw_data根据id排序
# code

for i in range(N):
    print(data[i]["documents"])
    print("-" * 30)
    #输出到文件
    with open('output.txt', 'w') as f:
        #把data[i]["documents"]转成json格式输出到文件
        text = json.dumps(data[i]["documents"], ensure_ascii=False, indent=4)
        print(text, file=f)
        prpt = example + inst + text
        # json.dump(data[i]["documents"], f, ensure_ascii=False, indent=4)
        # print(data[i]["documents"], file=f)
    # for j in range(len(data[i]['documents'])):
    #     print(data[i]["documents"][j])
    break

print("-" * 30)
