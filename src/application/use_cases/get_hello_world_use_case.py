from src.domain.entities.hello_world import HelloWorld
from src.application.dtos.hello_world_response import HelloWorldResponse

class GetHelloWorldUseCase:
    """
    Hello Worldメッセージを取得するユースケース
    """
    
    def execute(self) -> HelloWorldResponse:
        """
        Hello Worldメッセージを取得する
        
        Returns:
            HelloWorldResponse: Hello Worldメッセージのレスポンス
        """
        hello_world = HelloWorld()
        return HelloWorldResponse(message=hello_world.message)