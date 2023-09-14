from fastapi import File, UploadFile,APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

upload_file_router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Đường dẫn đến thư mục chứa các tệp đã tải lên
upload_folder = "docs"

# Tạo thư mục tải lên nếu nó không tồn tại
# os.makedirs(upload_folder, exist_ok=True)
@upload_file_router.post("/upload")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    # Đường dẫn lưu trữ tệp đã tải lên
    file_path = os.path.join(upload_folder, pdf_file.filename)
    # Mở tệp để ghi dữ liệu đã tải lên
    with open(file_path, "wb") as f:
        f.write(pdf_file.file.read())  
    return {"Successfully upload file :": pdf_file.filename}

@upload_file_router.get("/response", response_class=HTMLResponse)
async def get_upload_form():
    return templates.TemplateResponse("app/templates/admin.html", {"request": "request"})