## Getting started

* To download and install `pytest`, run this command from the terminal : `py -m pip install pytest`
* To download and install `requests`, run this command from the terminal : `py -m pip install requests`

To ensure all dependencies are resolved, run the following command:
`py -m pip install -r requirements.txt`

## Running tests

To run the tests use the command: `py -m pytest -q`

Additional arguments may be provided my using the `--persons num` flag; which will generate `num` number of persons to test. If not provided, will result in a default value of 5.

# Using Docker

To build the Docker container use the following command in the working dir of the project: `docker build -t {image_name}`

To run the Docker container use the following command: `docker run -dp 80:80 {image_name}`