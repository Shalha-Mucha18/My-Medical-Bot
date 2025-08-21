from fastapi import APIRouter, File, UploadFile
from typing import List
from modules.vectorstore import load_vectorestore
from fastapi.responses import JSONResponse
from logger import logger

router = APIRouter()

@router.post("/upload_pdfs/")
async def upload_pdfs(files: List[UploadFile] = File(...)):

    try:
        logger.info("Received files for upload.")
        load_vectorestore(files)
        logger.info("PDFs uploaded successfully.")
        return {"message": "files processed and  vectorqtore updated successfully. Please ask your query."}    
    except Exception as e:
        logger.error(f"Error uploading PDFs: {e}")
        return JSONResponse(status_code=500, content={"message": "Failed to upload PDFs."})     

