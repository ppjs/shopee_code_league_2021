from tqdm import tqdm
import argparse
import json
import csv
import re


human_rule_dict = json.load(open("human_rule_dict.json"))
expansion_rule_dict = json.load(open("expanstion_rule_dict.json"))
poi_dict = dict(**human_rule_dict["poi"], **expansion_rule_dict)
street_dict = human_rule_dict["street"]
rule_dict = {"poi": poi_dict, "street": street_dict}


raw_out = []
diff = []

def match_rule(row, field):
    d = {}
    search_dict = rule_dict[field]
    if row[field] != '':
        for key, value in search_dict.items():
            try:
                regex = re.compile(rf"{key}")
            except:
                print(key)
                break
            match = regex.search(row[field])
            if match is not None:
                ans = match.group(0)
                if ans != value:
                    d['id'] = row['id']
                    d[f'old_{field}'] = row[field]
                    d[f'new_{field}'] = row[field].replace(ans, value)
                    raw_out[row['id']][field] = row[field].replace(ans, value)

    return d


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=True)
    parser.add_argument('--output', type=str, default="out.csv")
    parser.add_argument('--diff', type=str, default='diff_rule.csv')
    args = parser.parse_args()

    with open(args.input, newline='', encoding="utf-8") as csvfile:
        rows = csv.reader(csvfile)
        next(rows, None)
        for row in rows:
            raw_out.append({ 'id': int(row[0]), 'poi': row[1].split('/')[0], 'street': row[1].split('/')[1] })

    for i in tqdm(range(len(raw_out))):
        d_poi = match_rule(raw_out[i], 'poi')
        d_street = match_rule(raw_out[i], 'street')
        d_row = {**d_poi, **d_street}
        if 'id' in d_row:
            diff.append(d_row)

    with open(args.output, 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'POI/street'])
        for i in range(len(raw_out)):
            writer.writerow([i, f'{raw_out[i]["poi"]}/{raw_out[i]["street"]}'])

    with open(args.diff, 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(diff)):
            old = diff[i].get('old_poi', '') + '/' + diff[i].get('old_street', '')
            new = diff[i].get('new_poi', '') + '/' + diff[i].get('new_street', '')
            writer.writerow([diff[i]['id'], f'{old} -> {new}'])

if __name__ == "__main__":
	main()