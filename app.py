from subprocess import run

run(["roulette/manage.py", "makemigrations"])
run(["roulette/manage.py", "migrate"])
run(["roulette/manage.py", "runserver", "0.0.0.0:8080"])
