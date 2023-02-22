import asyncio
import threading
from fastapi import FastAPI
import uvicorn,gunicorn
from src import inference_ouput, ingression
from src.core.appconfig import app_port,amqp_url
from src.core.amqp import AmqpConfig
app = FastAPI()

amqpConfig=AmqpConfig(amqp_url)


@app.on_event("startup")
async def startup():
    print("⚡️🚀 RadioAdSpread Analytics Engine Started")
    chn = await asyncio.to_thread(amqpConfig.start)
    inference_thread = threading.Thread(target=inference_ouput.push_audio_inference, args=(chn,))
    inference_thread.start()
    ingression_thread=threading.Thread(target=ingression.LoadStationData, args=())
    ingression_thread.start()



@app.on_event("shutdown")
async def shutdown():
    print("⚡️🚀 RadioAdSpread Analytics Engine::SHUTDOWN")

@app.get("/")
async def root():
    return {"message": "Hello--World"}


if __name__ == "__main__":
    gunicorn.run(app, host="0.0.0.0")