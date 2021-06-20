from tqdm import tqdm
import numpy as np
import pandas as pd
import json
import re



if __name__ == "__main__":
	search_poi = json.load(open("rule/poi_rules.json"))

	df = pd.DataFrame()
	for key,value in tqdm(search_poi.items()):
		poi_search, poi = key.split(" -> ")
		df = df.append({"poi_search": poi_search, "poi": poi, "count": value}, ignore_index=True)

	df["sum"] = df["count"].groupby(df["poi_search"]).transform("sum")
	df["perc"] = df["count"]/df["sum"]
	df = df[["poi_search", "poi", "count", "sum", "perc"]]
	df = df.sort_values(["poi_search", "perc"], ascending=False)
	output_d = d[(d["perc"]>=0.4) & (d["sum"]>=3)].sort_values("sum", ascending=False)

	output_dict = {}
	for ind,row in output_d.iterrows():
		pattern = row.poi_search.replace('(', '\(').replace(')', '\)').replace('?', '\?').replace('.', '\.').replace('+', '\+').replace('[', '\[').replace(']', '\]')
		output_dict[f"(?<!\w){pattern}(?!\w)"] = row.poi

	with open('rule/expansion_rule_dict.json', 'w') as json_file:
		json.dump(output_dict, json_file)
