from fastapi import FastAPI
from pydantic import BaseModel
from sentiments import get_sentiment


class Message(BaseModel):
    text: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Sentimental Analysis Api"}


@app.post("/sentiment")
async def check_sentiment(message: Message):
    score, sentiment = get_sentiment(message.text)
    return {"sentiment": sentiment, "score": score}
