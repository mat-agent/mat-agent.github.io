import json

# Load data from the JSON file
with open('public/data/demo.json', 'r') as f:
    data = json.load(f)

# Filter the data using list comprehensions
fire_100k = [i for i in data if i["split"] == "fire_100k"]
fire_1m = [i for i in data if i["split"] == "fire_1m"]
fire_bench = [i for i in data if i["split"] == "fire_test" and i["source"]!= "mathverse"]

# Print the lengths of the filtered lists
print(len(fire_100k), len(fire_1m), len(fire_bench))

# Save the filtered data to separate JSON files
with open('public/data/demo-100k.json', 'w') as f:
    json.dump(fire_100k, f)

with open('public/data/demo-1m.json', 'w') as f:
    json.dump(fire_1m, f)

with open('public/data/demo-bench.json', 'w') as f:
    json.dump(fire_bench, f)