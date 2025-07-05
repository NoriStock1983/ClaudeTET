from datetime import datetime


class CreatedDate:
    """作成日時値オブジェクト (created_date)"""
    
    def __init__(self, value: datetime):
        self._validate(value)
        self._value = value
    
    def _validate(self, value: datetime) -> None:
        if value is None:
            raise ValueError("作成日時は必須です")
        
        if not isinstance(value, datetime):
            raise TypeError("作成日時はdatetime型である必要があります")
    
    @property
    def value(self) -> datetime:
        return self._value
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CreatedDate):
            return False
        return self._value == other._value
    
    def __hash__(self) -> int:
        return hash(self._value)
    
    def __str__(self) -> str:
        return self._value.isoformat()