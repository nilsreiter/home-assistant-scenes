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
  preset_id = preset["id"]
  bri = preset["bri"]
  lights = [[l["x"], l["y"]] for l in preset["lights"]]
  s = {"c": lights, "b": round(bri / 255, 3), "s": set_name, "n": scene_name}
  d[preset_id] = s
  l.append(set_name + ": " + scene_name)

sorted_json = {k: d[k] for k in sorted(d)}
with open('output.json', 'w') as f:
  for key, value in sorted_json.items():
    f.write(f'{ json.dumps(value, separators=(",", ":"), ensure_ascii=False) },\n')
  f.write("""{"colors":[
  [ range(hue_min|default(0),hue_max|default(360))|random,range(sat_min|default(99),sat_max|default(101))|random ],
  [ range(hue_min|default(0),hue_max|default(360))|random,range(sat_min|default(99),sat_max|default(101))|random ],
  [ range(hue_min|default(0),hue_max|default(360))|random,range(sat_min|default(99),sat_max|default(101))|random ],
  [ range(hue_min|default(0),hue_max|default(360))|random,range(sat_min|default(99),sat_max|default(101))|random ],
  [ range(hue_min|default(0),hue_max|default(360))|random,range(sat_min|default(99),sat_max|default(101))|random ],
],"s":"Special","n":"Random"},
""")
  f.write('{"colors":[],"s":"Special","n":"Colorloop"}')

l.sort()
l.append("Special: Colorloop")
l.append("Special: Random")

for s in l:
  print(f"- \"{s}\"")
