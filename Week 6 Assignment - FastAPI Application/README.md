# Rest Api for sentimental analysis using Fast Api and Textblob


## Install requirements
```shell
pip install -r requirements.txt
```

## Start the application
```shell
uvicorn main:app --reload
```

## Example usage
```shell
curl --location --request POST 'http://127.0.0.1:8000/sentiment' \
--header 'Content-Type: application/json' \
--data-raw '{
  "text": "haha"
}'
```

## Example response
```json
{
    "sentiment": "positive",
    "score": 0.2
}
```
