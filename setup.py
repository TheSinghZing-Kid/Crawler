import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "bs4"])