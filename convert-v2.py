import json

f = open("presets.json")
obj = json.load(f)

d = {}
l = []

categories = obj["categories"]

for preset in obj["presets"]:
  set_name = None
  for category in categories:
    if preset["categoryId"] == category["id"] and category["id"] != "6e102277-814f-47c7-a054-f4a31cae30bf":
      set_name = category["name"]
      break

  if set_name is None:
    print(f"Warning: No category found for preset {preset['name']}")
    continue

  scene_name = preset["name"]
  bri = preset["bri"]
  lights = [[l["x"], l["y"]] for l in preset["lights"]]
  s = {"c": lights, "b": round(bri / 255, 3), "s": set_name}
  d[scene_name] = s
  l.append(set_name + ": " + scene_name)

sorted_json = {k: d[k] for k in sorted(d)}
with open('output.json', 'w') as f:
  # Need to add Colorloop and Random manually
  json.dump(sorted_json, f, separators=(',', ':'), ensure_ascii=False)

l.sort()
l.append("Special: Colorloop")
l.append("Special: Random")

for s in l:
  print(f"- \"{s}\"")
