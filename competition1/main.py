import pandas as pd
import json


df = json.load(open("contacts.json"))


parent_dict = {}
parentID_record = [x for x in range(len(df))]


def findParent(curID):
    if parentID_record[curID] == curID:
        return curID
    parentID_record[curID] = findParent(parentID_record[curID])
    return parentID_record[curID]


for row in df:
    id = row["Id"]
    mail = row["Email"]
    phone = row["Phone"]
    orderId = row["OrderId"]
    if mail != "":
        if mail not in parent_dict:
            parent_dict[mail] = id
        parentID_record[findParent(parent_dict[mail])] = findParent(id)
    if phone != "":
        if phone not in parent_dict:
            parent_dict[phone] = id
        parentID_record[findParent(parent_dict[phone])] = findParent(id)
    if orderId != "":
        if orderId not in parent_dict:
            parent_dict[orderId] = id
        parentID_record[findParent(parent_dict[orderId])] = findParent(id)


record = pd.DataFrame(
    data={
        "child":range(len(df))
    }
)
record["parent"] = record["child"].map(lambda x : findParent(x))
output = {}
for row in df:
    id = row["Id"]
    contact = row["Contacts"]
    parentID = parentID_record[id]
    if parentID not in output:
        tmp = {}
        tmp["ticket_trace"] = str(id)
        tmp["contact"] = contact
        output[parentID] = tmp
    else:
        output[parentID]["ticket_trace"] += ("-" + str(id))
        output[parentID]["contact"] += contact
output_trace = [output[parentID_record[x]]["ticket_trace"] for x in range(len(df))]
output_contact = [output[parentID_record[x]]["contact"] for x in range(len(df))]
output_merge = [output_trace[i]+", "+str(output_contact[i]) for i in range(len(df))]


output_df = pd.DataFrame(
    {
        "ticket_id": range(len(df)),
        "ticket_trace/contact" : output_merge
    }
)
output_df.to_csv("output1.csv", index=False)