from fastapi import FastAPI
from ontology_agent.config import get_settings

settings = get_settings()

def create_app() -> FastAPI:
    app = FastAPI(title="OntologyAgent", version="0.1.0")

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app

app = create_app()
