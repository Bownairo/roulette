from subprocess import run

run(["roulette/manage.py", "makemigrations"])
run(["roulette/manage.py", "migrate"])
run(["roulette/manage.py", "runserver", "127.0.0.1:8080"])
