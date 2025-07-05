class UpdateCounter:
    """更新カウンター値オブジェクト (updatecounter)"""
    
    def __init__(self, value: int):
        self._validate(value)
        self._value = value
    
    def _validate(self, value: int) -> None:
        if value is None:
            raise ValueError("更新カウンターは必須です")
        
        if not isinstance(value, int):
            raise TypeError("更新カウンターは整数である必要があります")
        
        if value < 0:
            raise ValueError("更新カウンターは0以上である必要があります")
    
    @property
    def value(self) -> int:
        return self._value
    
    def increment(self) -> 'UpdateCounter':
        """カウンターをインクリメントした新しいインスタンスを返す"""
        return UpdateCounter(self._value + 1)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UpdateCounter):
            return False
        return self._value == other._value
    
    def __hash__(self) -> int:
        return hash(self._value)
    
    def __str__(self) -> str:
        return str(self._value)