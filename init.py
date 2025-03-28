from utils import (is_linux)
from subprocess import run
from os import system

if is_linux():
    run(["touch", ".env"])
else:
    system("echo 'contenido' > .env")