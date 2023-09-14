from fastapi import APIRouter
from gpt_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI

update_KB_router = APIRouter()

@update_KB_router.post('/update')
def update():
    """Input"""
    directory_path = 'docs'
    max_input_size = 4096 #Số lượng input tối đa nhập vào cho một request (đơn vị token)
    max_chunk_overlap = 20 #Số token lặp mỗi phần (tối đa)
    chunk_size_limit = 600 #Số token mỗi phần (tối đa)
    """Output"""
    num_outputs = 512 #Số lượng token output tối đa 
    
    """Trả về object PromptHelper cấu hình các tham số của nó để sử dụng cho việc tạo đoạn gợi (prompt) và quản lý đầu vào cho mô hình chat."""
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs)) #temparature là mức độ "sáng tạo/đa dạng" của mô hình
    
    documents = SimpleDirectoryReader(directory_path).load_data() #Output: text

    index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper) #Output: vector

    index.save_to_disk('resource/index.json')

    return 'Successfully Update Knowledgebase'  