
# Eaglercraft Server Setup

This repository contains a portable Eaglercraft + Paper 1.12.2 server setup using BungeeCord as a proxy.

## Workspace Structure

```text
eaglercraft-portable/
├── bungee/
│   ├── config.yml
│   ├── start.sh
│   └── plugins/
│       └── EaglercraftXServer/
│           ├── ice_servers.yml
│           ├── listeners.yml
│           └── ...
├── paper/
│   ├── eula.txt
│   ├── server.properties
│   ├── spigot.yml
│   └── start.sh
└── web-serve/
    ├── http-serve.py
    └── index.html
```

## EaglerXServer Plugin

The EaglerXServer plugin is already present under `eaglercraft-portable/bungee/plugins/EaglercraftXServer` and provides Eaglercraft compatibility for multiple client versions.

## How to Start

Start the servers from the repository root or from your home directory. Example commands (adjust paths as needed):

1. Start the Paper backend (wait until you see the server "Done" message):

```bash
cd ~/Desktop/Eaglercraft-Paper_1.12-Server/eaglercraft-portable/paper
./start.sh
```

1. In a new terminal, start the BungeeCord proxy:

```bash
cd ~/Desktop/Eaglercraft-Paper_1.12-Server/eaglercraft-portable/bungee
./start.sh
```

## Connecting

- For Eaglercraft clients: connect to `ws://<server-ip>:25565` (use WebSocket URL if required by your client).
- For standard Minecraft 1.12.2 clients: connect to `<server-ip>:25565`.

Default ports used by this setup:

- BungeeCord proxy: `25565`
- Paper backend: `25566` (the Paper server is typically configured to run on a different port)

## Configuration

- Edit `eaglercraft-portable/bungee/config.yml` to change proxy settings (host, ports, online-mode).
- Edit `eaglercraft-portable/paper/server.properties` and `spigot.yml` for backend settings; ensure BungeeCord/IP forwarding settings match your network.

## Stopping the Servers

Press `Ctrl+C` in each terminal running the servers, or use the BungeeCord console command `end` to stop the proxy.

## Troubleshooting

1. If ports are in use, change them in `bungee/config.yml` (proxy) and `paper/server.properties` (backend).
2. Ensure Java is installed: run `java -version`.
3. If you need more memory, edit the `start.sh` scripts to adjust JVM flags.

If you'd like, I can also:

- update the start scripts with explicit `java -Xmx` settings
- add a small `README` section showing how to install Java on Linux
