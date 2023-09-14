from fastapi import APIRouter
from fastapi.responses import HTMLResponse

UI_router = APIRouter()

# Đường dẫn đến thư mục chứa tệp templates
templates_dir = "app/templates"

@UI_router.get("/chat", response_class=HTMLResponse)
async def get():
    # Đọc nội dung từ tệp HTML và trả nó dưới dạng phản hồi HTML
    with open(f"{templates_dir}/chat.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@UI_router.get("/admin", response_class=HTMLResponse)
async def get():
    # Đọc nội dung từ tệp HTML và trả nó dưới dạng phản hồi HTML
    with open(f"{templates_dir}/admin.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)