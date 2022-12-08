clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

migrate:
	flask --app manage:app  db migrate

upgrade:
	flask --app manage:app  db upgrade

run:
	flask --app manage:app run

init:
	flask --app manage:app init


run-prod:
	gunicorn -b 0.0.0.0:5000 manage:app

test:
	pytest
