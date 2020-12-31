# gpio-valve-monitor

> This is for personal use, you'll need to adapt it to your environment if you want to use it

Utility for determining floor heating valve statuses through the GPIO pins on a Raspberry Pi or compatible device. The 
valve outputs (24 VAC) should be connected via an octocoupler to the GPIO pins. The pin state can then be sampled to 
determine whether there's a line or not (i.e. if the valve is open or not).

Assumes valve motors are NC (normally closed).

![Wiring](https://github.com/Jalle19/gpio-valve-monitor/raw/master/wiring.jpg)

The boards used here are AL-ZARD DST-1R8P-P and DST-1R4P-P. They can be powered from the 3V3 pins on a Raspberry Pi 
Zero W. 

## Usage

There's a Python script that reads the state of all valves and prints a JSON summary:

```bash
$ python3 gpiovalvemonitor/main.py | jq
[
  {
    "pin": 17,
    "octocoupler_port": "L8",
    "pull_up": false,
    "roth_channel": 1,
    "zone": "Förråd",
    "state": 0
  },
  {
    "pin": 27,
    "octocoupler_port": "L7",
    "pull_up": false,
    "roth_channel": 2,
    "zone": "Sovrum",
    "state": 1
  },
  ... SNIP ...
  {
    "pin": 16,
    "octocoupler_port": "R3",
    "pull_up": true,
    "roth_channel": 9,
    "zone": "Hjälpkök",
    "state": 0
  }
]
```

There's a Node.js script for ingesting the JSON from the previous command into InfluxDB:

```bash
cat example.json | node infuxdb-ingest.js
```

The script requiress the `INFLUX_HOST`, `INFLUX_DATABASE`, `INFLUX_USERNAME` and `INFLUX_PASSWORD` environment 
variables to be defined.

Combined, the two scripts can be run from cron every minute or so:

```bash
*/10 * * * * python3 gpiovalvemonitor/main.py | node infuxdb-ingest.js
```

## License

GNU GENERAL PUBLIC LICENSE Version 3