from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exception_handler

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
# 2. asking query