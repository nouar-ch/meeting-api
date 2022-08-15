# Meeting API

This an API that returns the best meeting slot if any given a list of availability times.

## Installation
Requires python 3.7.3
Use pipenv to setup the project

```bash
pip install pipenv
cd <project directory>
pipenv install
pipenv shell
```

## Usage

```bash
python ./main.py
```

in a seperate terminal window

```bash
curl --location --request POST 'http://127.0.0.1:5000/api/v1/calculate-best-dates' \
--header 'Content-Type: text/plain' \
--data-raw '[{
"from": "2022-05-02T09:00:00.0+08:00",
"to": "2022-05-02T17:00:00.0+08:00",
"CC": "SG"
},
{
"from": "2022-05-02T09:00:00.0+01:00",
"to": "2022-05-02T17:00:00.0+01:00",
"CC": "NG"
},
{
"from": "2022-05-02T09:00:00.0+05:30",
"to": "2022-05-02T17:00:00.0+05:30",
"CC": "IN"
}]'
```

## Run Unit Tests

```bash
python ./test.py
```
