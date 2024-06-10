#!/usr/bin/env python
from fastapi import FastAPI
from typing import Optional
import dotenv
import os
from langserve import add_routes
from langchain.chat_models import ChatOpenAI
from main import *


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)


@app.get("/chat")
async def chat(query: Optional[str] = None):
    # Process the query in some way. Here, we just echo it back.
    if query is not None:
        final_response = jiraAgent(query)
        json = {
            "query": query,
            "aiResponse": final_response,
        }
        return json
    else:
        return {"message": "No query provided."}


add_routes(
    app,
    ChatOpenAI(),
    path="/openai",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
