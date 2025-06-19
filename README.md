# opencartlab-selenium-tests

Project created by [qaforge.tech](https://qaforge.tech)

End-to-end UI automation tests for https://oc3032std.opencartlab.pl using Selenium & Python.

## Project Structure

```
opencartlab-selenium-tests-python
├── docker
│   ├── selenium
│   │   └── Dockerfile
│   └── docker-compose.yml
├── .env
├── src
│   ├── pages
│   │   ├── base_page.py
│   │   └── home_page.py
│   ├── utilities
│   │   ├── driver_factory.py
│   │   └── config_reader.py
│   └── conftest.py
├── tests
│   ├── TestSelenium.py
│   └── conftest.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── README.md
├── LICENSE
└── .gitignore
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/QAForge/opencartlab-selenium-tests-python.git
   cd opencartlab-selenium-tests-python
   ```

2. **Build the Docker image:**
   ```
   docker-compose build
   ```

3. **Run the tests:**
   ```
   docker-compose up
   ```

## Usage

- The Selenium tests are located in the `tests` directory. You can modify the `TestSelenium.py` file to add more test cases as needed.
- The project uses `pytest` for running tests. Ensure that you have the necessary dependencies listed in `requirements.txt`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.