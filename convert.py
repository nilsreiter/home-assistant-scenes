import json

f = open("scenes.json")
obj = json.load(f)

d = {}
l = []

for scene_set in obj["sets"]:
  set_name = scene_set["name"]
  for scene in scene_set["scenes"]:
    scene_name = scene["name"]
    bri = scene["bri"]
    lights = [[l["x"], l["y"]] for l in scene["lights"]]
    s = {"c": lights, "b": round(bri / 255, 3), "s": set_name}
    d[scene_name] = s
    l.append(set_name + ": " + scene_name)

print(json.dumps(d, separators=(',', ':'), sort_keys=True))

l.sort()

for s in l:
  print(f"- \"{s}\"")
