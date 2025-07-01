from fastapi import FastAPI
from src.presentation.controllers.hello_world_controller import HelloWorldController

def create_app() -> FastAPI:
    """
    FastAPIアプリケーションを作成する
    
    Returns:
        FastAPI: 設定済みのFastAPIアプリケーション
    """
    app = FastAPI(
        title="Hello World API",
        version="1.0.0",
        description="クリーンアーキテクチャで構築されたHello World API"
    )
    
    # コントローラーのルーターを登録
    hello_world_controller = HelloWorldController()
    app.include_router(hello_world_controller.router)
    
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)