import tabula
import glob, os
import os.path
import json

files = glob.glob("pdfs/*.pdf")

#declaring lists
whole_data = []
all_colleges = []
all_categories = []
all_quotas = []
all_seat_pools = []
all_streams = []


for i in files:
    inputf = os.path.join(os.path.dirname(os.path.realpath(__file__)), i)
    output = os.path.join(os.path.dirname(os.path.realpath(__file__)) ,"pdfs-to-jsons" + os.sep + ".".join(i.split(os.sep)[-1].split(".")[:-1]) + ".csv")
    print("Reading {}. ".format(i.split(os.sep)[-1]))
    df = tabula.read_pdf(inputf, pages='all')
    #data = []
    for i in df:
        page = i.dropna().values
        for row in page:
            if str(row[0]) not in ['1','2','3','4','5','6','7']:
                continue
            temp_dict = {
                "round": int(row[0]),
                "college": row[1].replace("\r", " "),
                "stream": row[2].replace("\r", " "),
                "quota": row[3].replace("\r", " "),
                "category": row[4].replace("\r", " "),
                "seat_pool": row[5].replace("\r", " "),
                "opening_rank": int(float(row[6][:-1])) if str(row[6]).endswith("P") else int(float(row[6])),
                "closing_rank": int(float(row[7][:-1])) if str(row[7]).endswith("P") else int(float(row[7])),
                "rank_type": "preparatory" if str(row[7]).endswith("P") else "general" if row[4] == "General" else "category"
            }
            if temp_dict["college"] not in all_colleges:
                all_colleges.append(temp_dict["college"])
            if temp_dict["stream"] not in all_streams:
                all_streams.append(temp_dict["stream"])
            if temp_dict["category"] not in all_categories:
                all_categories.append(temp_dict["category"])
            if temp_dict["quota"] not in all_quotas:
                all_quotas.append(temp_dict["quota"])
            if temp_dict["seat_pool"] not in all_seat_pools:
                all_seat_pools.append(temp_dict["seat_pool"])
            whole_data.append(temp_dict)

print("Writing to data.json")
with open("data.json", "w") as output:
    json.dump({
        "values" : {
            "round": [1,2,3,4,5,6,7],
            "college": all_colleges,
            "stream": all_streams,
            "category": all_categories,
            "quota": all_quotas,
            "seat_pool": all_seat_pools
        },
        "data" : whole_data
    }, output, indent=4)
