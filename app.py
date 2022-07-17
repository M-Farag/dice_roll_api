from fastapi import FastAPI
from dicy import dicy
from random import choice

app = FastAPI()


@app.get('/')
async def root():
    dice = dicy.Dicy()

    return {
        'data': {
            'result': choice(dice).face
        }
    }
