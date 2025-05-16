from mcrcon import MCRcon
import time
from config import get_kit_command

HOST = "localhost"
PORT = 25575
PASSWORD = "robocode"

given_kits = {}
last_line = ""

with MCRcon(HOST, PASSWORD, port=PORT) as mcr:
    print("Подключено к серверу")

    while True:
        try:
            with open("Server/logs/latest.log", "r", encoding="utf-8", errors="ignore") as log_file:
                lines = log_file.readlines()
                if not lines:
                    continue

                new_line = lines[-1]

                if new_line != last_line and "<" in new_line and ">" in new_line:
                    last_line = new_line
                    parts = new_line.split("> ")
                    player = parts[0].split("<")[1].strip()
                    message = parts[1].strip()

                    print(f"{player}: {message}")

                    if message.startswith("!kit"):
                        kit_name = message.split(" ")[1] if len(message.split(" ")) > 1 else ""

                        if (player, kit_name) in given_kits:
                            mcr.command(f"tell {player} Ты уже получал набор {kit_name}")
                        else:
                            command_list = get_kit_command(player, kit_name)
                            if command_list:
                                for cmd in command_list:
                                    mcr.command(cmd)
                                mcr.command(f"tell {player} Ты получил набор {kit_name}!")
                                given_kits[(player, kit_name)] = True
                            else:
                                mcr.command(f"tell {player} Набор '{kit_name}' не найден.")

                    if "give" in message.lower():
                        mcr.command(f"kick {player} Подозрение на читы (команда 'give')")

                    if message == "!heal":
                        mcr.command(f"effect give {player} minecraft:instant_health 1 2 true")
                        mcr.command(f"effect give {player} minecraft:saturation 1 1 true")
                        mcr.command(f"tell {player} Ты исцелен!")

                    if message == "!fireball":
                        mcr.command(f"summon minecraft:fireball ~ ~2 ~ {{direction:[0.0,0.0,0.0],power:[0.0,0.5,0.0],ExplosionPower:1,owner:{{UUID:[I;0,0,0,0]}}}}")
                        mcr.command(f"tell {player} БУМ! 🔥")

        except Exception as e:
            print(f"Ошибка: {e}")

        time.sleep(1)
