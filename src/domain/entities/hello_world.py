class HelloWorld:
    """
    Hello Worldメッセージを表現するエンティティ
    """
    
    def __init__(self, message: str = "Hello, World!"):
        self._message = message
    
    @property
    def message(self) -> str:
        """
        メッセージを取得する
        
        Returns:
            str: Hello Worldメッセージ
        """
        return self._message
    
    def customize_message(self, custom_message: str) -> None:
        """
        メッセージをカスタマイズする
        
        Args:
            custom_message: カスタムメッセージ
            
        Raises:
            ValueError: メッセージが空文字列の場合
        """
        if not custom_message.strip():
            raise ValueError("メッセージが空です")
        
        self._message = custom_message