from fastapi import APIRouter
from src.application.use_cases.get_hello_world_use_case import GetHelloWorldUseCase
from src.application.dtos.hello_world_response import HelloWorldResponse

class HelloWorldController:
    """
    Hello World APIのコントローラー
    """
    
    def __init__(self):
        self.router = APIRouter()
        self.get_hello_world_use_case = GetHelloWorldUseCase()
        self._setup_routes()
    
    def _setup_routes(self):
        """
        ルートを設定する
        """
        self.router.add_api_route(
            "/",
            self.get_hello_world,
            methods=["GET"],
            response_model=HelloWorldResponse,
            summary="Hello World取得",
            description="Hello Worldメッセージを取得します"
        )
    
    def get_hello_world(self) -> HelloWorldResponse:
        """
        Hello Worldメッセージを取得するエンドポイント
        
        Returns:
            HelloWorldResponse: Hello Worldメッセージ
        """
        return self.get_hello_world_use_case.execute()