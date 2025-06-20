# Budowanie obrazu
docker build -t opencartlab-selenium-tests-python-docker .

docker run --rm -v "${PWD}:/app" opencartlab-selenium-tests-python-docker pytest tests/ --html=/app/report.html --self-contained-html
