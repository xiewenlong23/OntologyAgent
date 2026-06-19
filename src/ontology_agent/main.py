from fastapi import FastAPI
from ontology_agent.config import get_settings
from ontology_agent.api.chat import router as chat_router
from ontology_agent.api.ontology import router as ontology_router

settings = get_settings()

def create_app() -> FastAPI:
    app = FastAPI(title="OntologyAgent", version="0.1.0")
    app.include_router(chat_router)
    app.include_router(ontology_router)

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app

app = create_app()
