from fastapi import FastAPI
from app.routes.knowledgebase_routes import update_KB_router
from app.routes.chat_routes import chat_router
from app.routes.UI_routes import UI_router
from app.routes.file_routes import upload_file_router
import os

os.environ["OPENAI_API_KEY"] = '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'

app = FastAPI()

app.include_router(UI_router)
app.include_router(chat_router)
app.include_router(update_KB_router)
app.include_router(upload_file_router)
