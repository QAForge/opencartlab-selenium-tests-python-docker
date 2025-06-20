# Budowanie obrazu
docker build -t qaforge-projects .


cd C:\Users\tomiz\PycharmProjects\qaforge-projects

docker run --rm -v "${PWD}:/app" qaforge-projects pytest tests/ --html=/app/report.html --self-contained-html
