import json
with open("payload_telemetry.txt") as f:
    data = json.loads(f.read())

for row in data["rows"]:
    print str(row["doc"]["data"]["altitude"]) + "," + \
    str(row["doc"]["data"]["temperature_internal"])
