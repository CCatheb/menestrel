# Ménestrel

Ménestrel is a Discord bot used to stream audio when playing RPG on VTTs.

## Features

Actual features:
- Self-Hosted
- Answers "Pong!" when typing "!ping"
- Logs API calls on Discord channel

Features in progress:
- Audio mixing and streaming
- Getting audio files from a network storage (my personal NAS)

## Install

This is somehow a personnal project. You can try to download it and setup it. Shouldn't be too hard.

Put a file `config.ini` in the `config` directory, with the following elements:
```
[Discord]
Token=<YourToken>

[API]
VERSION=1
Authorized_Hosts=<YourAPIAuthorizedHosts>
Port=<YourPort>

[Database]
File=database.json
```

Under the `data` folder, set your database (you can change the name of the file in the ``config.ini``)

Database example:
```json
{
    "_default": {
        "1": {
            "type": "music",
            "tags": {
                "scene": "Ville",
                "phase": "Exploration"
            },
            "path": "/path/to/music"
        },
        "2": {
            "type": "music",
            "tags": {
                "scene": "Ville",
                "phase": "Exploration"
            },
            "path": "/path/to/second/music"
        }
    }
}
```