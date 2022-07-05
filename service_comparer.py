import os
import subprocess

from back.config_manager import get_config

SCRIPT_PATH = "/".join(os.path.realpath(__file__).split("/")[:-1])
CONFIG = get_config(SCRIPT_PATH)
APP_NAME = CONFIG["APP_NAME"]


# cat_service = str(os.system(cat_command))[:-1].strip()
cat_command = f"systemctl --user cat {APP_NAME}.service"
temp_subprocess = subprocess.Popen(cat_command, stdout=subprocess.PIPE, shell=True)
cat_service = "\n".join(temp_subprocess.communicate()[0].decode().split("\n")[1:])
cat_service = cat_service.strip()
print("⚙️ service file in systemctl:\n")
print(cat_service)

with open(f"./service/{APP_NAME}.service", "r") as f:
    text_service = f.read().strip()

if cat_service != text_service:
    print("\n❌ service files NOT match ")
else:
    print("\n✅ service files match")
