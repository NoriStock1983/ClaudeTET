from dataclasses import dataclass

@dataclass
class HelloWorldResponse:
    """
    Hello World APIのレスポンスDTO
    """
    message: str