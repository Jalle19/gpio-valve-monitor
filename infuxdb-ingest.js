const fs = require('fs')
const Influx = require('influx')

getSchemaDefinition = function () {
    return [
        {
            measurement: 'valves',
            fields: {
                'pin': Influx.FieldType.INTEGER,
                'octocoupler_port': Influx.FieldType.STRING,
                'roth_channel': Influx.FieldType.INTEGER,
                'zone': Influx.FieldType.STRING,
                'state': Influx.FieldType.INTEGER, // Grafana doesn't like booleans
            },
            tags: [
                'pin',
                'octocoupler_port',
                'roth_channel',
                'zone',
            ]
        }
    ]
}

createPoint = function (valve) {
    return {
        measurement: 'valves',
        fields: {
            'pin': valve.pin,
            'octocoupler_port': valve.octocoupler_port,
            'roth_channel': valve.roth_channel,
            'zone': valve.zone,
            'state': valve.state,
        },
        tags: {
            'pin': valve.pin,
            'octocoupler_port': valve.octocoupler_port,
            'roth_channel': valve.roth_channel,
            'zone': valve.zone,
        }
    }
}

const requiredEnvVars = [
    'INFLUX_HOST',
    'INFLUX_DATABASE',
    'INFLUX_USERNAME',
    'INFLUX_PASSWORD',
]

for (const envVar of requiredEnvVars) {
    if (!process.env[envVar]) {
        throw new Error(`${requiredEnvVars.join(', ')} must be specified`)
    }
}

const influx = new Influx.InfluxDB({
    host: process.env.INFLUX_HOST,
    database: process.env.INFLUX_DATABASE,
    username: process.env.INFLUX_USERNAME,
    password: process.env.INFLUX_PASSWORD,
    schema: getSchemaDefinition(),
})

influx.getDatabaseNames().then((names) => {
    if (!names.includes(process.env.INFLUX_DATABASE)) {
        throw new Error(`The specified database "${process.env.INFLUX_DATABASE}" does not exist`)
    }

    const jsonData = fs.readFileSync(0, 'utf-8')
    const valves = JSON.parse(jsonData)

    // Create points for each valve, then write them all in one go
    const points = []

    for (const valve of valves) {
        points.push(createPoint(valve))
    }

    influx.writePoints(points)
})
