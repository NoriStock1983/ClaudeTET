class SubcontractClass:
    """外注区分値オブジェクト (subcontract_class)"""
    
    ALLOWED_VALUES = ["00", "01", "02"]  # 00:自社, 01:外注, 02:協力会社
    
    def __init__(self, value: str):
        self._validate(value)
        self._value = value
    
    def _validate(self, value: str) -> None:
        if not value:
            raise ValueError("外注区分は必須です")
        
        if not isinstance(value, str):
            raise TypeError("外注区分は文字列である必要があります")
        
        if value not in self.ALLOWED_VALUES:
            raise ValueError("外注区分は00, 01, 02のいずれかである必要があります")
    
    @property
    def value(self) -> str:
        return self._value
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SubcontractClass):
            return False
        return self._value == other._value
    
    def __hash__(self) -> int:
        return hash(self._value)
    
    def __str__(self) -> str:
        return self._value