/!\ THIS README IS STILL UNDER CONSTRUCTION /!\

# Menestrel

Ménestrel is a Discord Python bot used to perform live sound mixing, and to play the result on a Discord voice channel.
It is mainly developed for TTRPG games, allowing Game Master to set an more immersive ambiance for their players, when remote playing.

# Installation

Clone the git repo, install the requirements.
FYI, it uses mainly:
```
- Flask
- DiscordPy
- Asyncio
```

## How does it works

User interface files are set in `interface/` folder.
Create a `conf.ini` file in the `conf/` folder, following this pattern:
```ini
[DISCORD]
TOKEN=<Your Discord Token Goes Here>
```

Run  `python3 run.py` to start the bot.

# Technical Informations

As the DiscordPy bot is blocking, it has to be running in an Asyncio Event Loop.
But the Flask API is also, somehow, blocking. So, it has to be run in a separate thread. 
That's what is done here, in Menestrel.

You can imagine the project working as follow:
```
+-----+            +-------+                               +---------+
| UI  |            | Flask |                               | Backend |
+-----+            +-------+                               +---------+
   |                   |                                        |
   |   HTTP Request    |                                        |
   |------------------>|                                        |
   |                   |                                        |
   |                   |                Tasks Queue             |
   |                   |--------------------------------------->|
   |                   |                                        | --------------------\
   |                   |                                        |-| Reads Tasks Queue |
   |                   |                                        | |-------------------|
   |                   |                                        | ------------------\
   |                   |                                        |-| Perform actions |
   |                   |                                        | |-----------------|
   |                   |                                        | -----------------------------------\
   |                   |                                        |-| Puts computed data in Data Queue |
   |                   |                                        | |----------------------------------|
   |                   |                                        |
   |                   |                 Data Queue             |
   |                   |<---------------------------------------|
   |                   | ------------------\                    |
   |                   |-| Read Data Queue |                    |
   |                   | |-----------------|                    |
   |                   | ----------------------------------\    |
   |                   |-| Sends back data to UI if needed |    |
   |                   | |---------------------------------|    |
   |                   |                                        |
   |   HTTP Response   |                                        |
   |<------------------|                                        |
   |                   |                                        |
   ```