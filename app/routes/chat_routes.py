from fastapi import APIRouter,WebSocket
from gpt_index import GPTSimpleVectorIndex

chat_router = APIRouter()

@chat_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        input_text = await websocket.receive_text()
        index = GPTSimpleVectorIndex.load_from_disk('resource/index.json')
        response = index.query(input_text, response_mode="compact")
        await websocket.send_text(f"Me: {input_text}")
        await websocket.send_text(f"ChatBot: {response.response}")