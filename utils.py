import platform
from subprocess import run, PIPE

def is_linux():
    if platform.system() == "Linux":
        return True
    else:
        print(f"Este sistema no es Linux, es {platform.system()}")
        return False

def know_path_ffmpeg(search_path: str = "ffmpeg"):
    if is_linux():
        result = run(["which", search_path], stdout=PIPE, text=True)
        path = result.stdout.strip()
        print(path)
        return path
    else:
        result = run(["where", search_path], stdout=PIPE, text=True)
        path = result.stdout.strip()
        print(path)
        return path


