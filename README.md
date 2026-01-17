# Eaglercraft Server Setup

This is a complete Eaglercraft server setup using BungeeCord as a proxy and Paper 1.12.2 as the backend server.

## Structure
```
eaglercraft-server/
├── bungee/           # BungeeCord proxy
│   ├── BungeeCord.jar
│   ├── config.yml
│   ├── plugins/
│   │   └── EaglerXServer.jar
│   └── start.sh
└── paper/            # Paper 1.12.2 server
    ├── paper-1.12.2.jar
    ├── server.properties
    ├── spigot.yml
    ├── eula.txt
    └── start.sh
```

## EaglerXServer Plugin

✅ **Already installed!** The EaglerXServer v1.0.8 plugin has been downloaded and placed in the BungeeCord plugins folder.

This plugin provides Eaglercraft support for:
- EaglercraftX 1.8
- Eaglercraft 1.12.2
- Eaglercraft 1.5.2 clients

## How to Start

### Step 1: Start the Paper Server
```bash
cd ~/Desktop/eaglercraft-server/paper
./start.sh
```
Wait for the server to fully start (you'll see "Done" message).

### Step 2: Start BungeeCord
In a new terminal:
```bash
cd ~/Desktop/eaglercraft-server/bungee
./start.sh
```

## Connecting

### For Eaglercraft Clients:
- Connect to: `ws://localhost:25565` or your server IP
- Make sure to use the correct Eaglercraft client version that matches your plugin

### For Regular Minecraft 1.12.2:
- Connect to: `localhost:25565`

## Configuration

### BungeeCord (port 25565)
- Edit `bungee/config.yml` to configure the proxy
- online-mode is set to false for Eaglercraft compatibility

### Paper Server (port 25566)
- Edit `paper/server.properties` for server settings
- `spigot.yml` has bungeecord mode enabled for IP forwarding

## Stopping the Server

Press `Ctrl+C` in each terminal or type `end` in the BungeeCord console.

## Troubleshooting

1. If ports are in use, edit the port numbers:
   - BungeeCord: `bungee/config.yml` (host: 0.0.0.0:25565)
   - Paper: `paper/server.properties` (server-port=25566)

2. Make sure Java is installed: `java -version`

3. Adjust memory allocation in start.sh files if needed
