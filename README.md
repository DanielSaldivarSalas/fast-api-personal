# fast-api-personal
This is for my personal understand of fast api


## Running application
```
pipenv run uvicorn app.main:app --reload
```

### Interactive API while Application is running
http://localhost:8000/docs

### Alternative Documentation provided by redoc
```
http://localhost:8000/redoc
```
## Running the test suite
```
pipenv run pytest
```

## Running code coverage
```
pipenv run pytest --cov-config=.coveragerc --cov .
```

## Running Static Type Checker
```
pipenv run mypy --strict src/
```