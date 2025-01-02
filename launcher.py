import subprocess
import os

def launch_game():
    game_script = os.path.join(os.path.dirname(__file__), "main.py")

    subprocess.Popen(["start", "cmd", "/k", f"python {game_script}"], shell=True)

if __name__ == "__main__":
    launch_game()