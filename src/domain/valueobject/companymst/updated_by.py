class UpdatedBy:
    """更新者値オブジェクト (updated_by)"""
    
    def __init__(self, value: str):
        self._validate(value)
        self._value = value
    
    def _validate(self, value: str) -> None:
        if not value:
            raise ValueError("更新者は必須です")
        
        if not isinstance(value, str):
            raise TypeError("更新者は文字列である必要があります")
        
        if len(value) > 8:
            raise ValueError("更新者は8文字以内である必要があります")
    
    @property
    def value(self) -> str:
        return self._value
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UpdatedBy):
            return False
        return self._value == other._value
    
    def __hash__(self) -> int:
        return hash(self._value)
    
    def __str__(self) -> str:
        return self._value