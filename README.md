# gpio-valve-monitor

Utility for determining floor heating valve statuses through the GPIO pins on a Raspberry Pi or compatible device

## Usage

```bash
$ python3 gpiovalvemonitor/main.py 
[
  {
    "pin": 17,
    "octocoupler_port": "L8",
    "roth_channel": 1,
    "room_description": "F\u00f6rr\u00e5d",
    "state": 0
  },
  {
    "pin": 27,
    "octocoupler_port": "L7",
    "roth_channel": 2,
    "room_description": "Sovrum",
    "state": 1
  },
  ... SNIP ...
  {
    "pin": 16,
    "octocoupler_port": "R3",
    "roth_channel": 8,
    "room_description": "Hj\u00e4lpk\u00f6k",
    "state": 1
  }
]
```