This script replicates Hue scenes for Home Assistant. Each scene has five different colors represented by XY values. These colors are distributed randomly on the participating lights (must support XY or RGB color modes) -- each light gets a different color.

The script can run in two modes, selectable *at runtime*, corresponding to  setting lights once or repeatedly. If `repeat_delay` is specified at the start of the script, it runs continuously, with the specified delay in between rounds. In this case, the end of the script is determined by the `stop_when_lights_turn_off` parameter: If set to true, the script turns off when one of the participating lights is turned off. If set to false, the script runs until it is turned off.

If `repeat_delay` is left empty or set to 0:00:00, lights are set once and the script ends.

The script has various configuration options, described below. 

## Usage

The intended setup is to instantiate the blueprint for each area in which it will be run. To facilitate daily use, you can define buttons as pre-defined action call. To launch the scene "Savanna sunset" as a dynamic scene, you can define a mushroom card like this:

```
type: custom:mushroom-template-card
primary: Savanna sunset
picture: /local/hue/Savanna sunset.jpg
tap_action:
  action: call-service
  service: script.hue_like_scenes
  target: {}
  data:
    scene: Savanna sunset
```

If called as part of another script, make sure to use the action `script.turn_on`, so that it runs in the background ([see here](https://www.home-assistant.io/integrations/script/#waiting-for-script-to-complete)):

```
action: script.turn_on
data:
  variables:
    scene: Savanna sunset
metadata: {}
target:
  entity_id: script.hue_like_scenes
```



## Changelog 

### 3.0

- Added default Hue scenes (Bright, Concentrate, Cool bright, Dimmed, Energize, Nightlight, Read, Relax, Rest). 
- Scene selection dropdown now shows scene set (Cozy, Defaults, Dreamy, Futuristic, Lush, Luxurious, Party vibes, Peaceful, Pure, Refreshing, Serenity, Sunrise). When launching the script (e.g. as an action), users can use the simple name as before, or a combination of set and scene name (e.g., `Cozy: Savanna sunset`).
- The script now includes pre-defined brightness settings. When starting, one now has three options: a) Define a brightness value, b) use the scene-defined value, and c) leave the brightness as it is.
- As part of the blueprint input settings, it is now possible to also set default values for the script. All script fields can be specified, and the script can then be run without any arguments (e.g., if you're mostly using one scene, you can set it as default).
- Fixed a bug for non-dynamic scenes

### 2.5.1

- Fixed a bug in assigning first colors for colorloop.

### 2.5

- Added input `stop_when_lights_turn_off` to allow running the script continuously.
- Added scene "Colorloop", which iterates over the entire color wheel. Colorloop uses hs color scheme, and only changes the hue value without touch the saturation.
- Re-added a scene consisting of random colors. Note that random colors are selected once when the script starts and then distributed over the lights.
- Added input `debug` to generate debug messages in the log.

### 2.4

- It is now possible to also specify devices. If a device has multiple entities from the light domain, all will be added individually.

### 2.3

- Selecting the lights is now done via proper lists, and no longer relies on parsing json
- New scene: Malibu pink
- Description of the scene field is shorter
- Added a report entity field. This can be a `input_text` entity and whenever a scene is set, the scene name is written into the entity.

### 2.2

- Transition time is now a blueprint field.
- Repeat delay now has a default value of two minutes.
- Fixed bug in duration format.

### 2.1

- The blueprint now contains all the Hue color scenes that are listed [here](https://gist.github.com/Hypfer/a0a8b5b9429831a7306ec4300077eaaa).

### 2.0

- Made into a blueprint. Intended use case: Instantiate blueprint for each area (then they can run independently in parallel).
- Supports loop mode, a.k.a. dynamic scenes
- Can exclude lights by manufacturer
- Select lights by labels

## Scene images

The images used in the Hue app to represent a scene use creative commons 
licenses. The following is a list of (some) scenes and image sources:

- Savanna Sunset: https://www.flickr.com/photos/ladydragonflyherworld/6293722846
- Majestic Morning: https://unsplash.com/photos/aerial-photo-of-foggy-trees-and-mountains-dbu1zrkZZuo
- Horizon: https://www.pexels.com/photo/rocks-on-water-2261500/
- Tropical Twilight: https://www.flickr.com/photos/130079987@N02/16342014082
- Crocus: https://unsplash.com/photos/close-up-photo-of-purple-petaled-flower-hB_xgEXucQs