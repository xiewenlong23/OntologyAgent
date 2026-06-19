from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from ontology_agent.config import get_settings
from ontology_agent.api.chat import router as chat_router
from ontology_agent.api.ontology import router as ontology_router
from ontology_agent.tools import register_all_tools
from pathlib import Path

settings = get_settings()

def create_app() -> FastAPI:
    register_all_tools()
    app = FastAPI(title="OntologyAgent", version="0.1.0")
    app.include_router(chat_router)
    app.include_router(ontology_router)

    # Serve frontend static files
    frontend_path = Path(__file__).parent.parent.parent / "frontend"
    if frontend_path.exists():
        app.mount("/static", StaticFiles(directory=str(frontend_path)), name="static")
        @app.get("/")
        async def root():
            return RedirectResponse(url="/static/index.html")

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app

app = create_app()
