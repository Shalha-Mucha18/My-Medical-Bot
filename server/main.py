from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exception_handler

from routes.upload_pdfs import router as upload_router
from routes.ask_qestion import router as ask_router

app = FastAPI(title="MED API", description="API for the MED project", version="1.0.0")

# CORS configuration
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"], # Allow all origins for development
                   allow_credentials=["*"],
                   allow_methods=["*"], # Allow all methods
                   allow_headers=["*"]) # Allow all headers

# middleware exception handler
app.middleware("http")(catch_exception_handler)


# route for the root path

# 1. upload pdf file
app.include_router(upload_router)
# 2. asking query
app.include_router(ask_router)