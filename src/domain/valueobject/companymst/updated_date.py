from datetime import datetime


class UpdatedDate:
    """更新日時値オブジェクト (updated_date)"""
    
    def __init__(self, value: datetime):
        self._validate(value)
        self._value = value
    
    def _validate(self, value: datetime) -> None:
        if value is None:
            raise ValueError("更新日時は必須です")
        
        if not isinstance(value, datetime):
            raise TypeError("更新日時はdatetime型である必要があります")
    
    @property
    def value(self) -> datetime:
        return self._value
    
    @classmethod
    def now(cls) -> 'UpdatedDate':
        """現在時刻で新しいインスタンスを作成"""
        return cls(datetime.now())
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UpdatedDate):
            return False
        return self._value == other._value
    
    def __hash__(self) -> int:
        return hash(self._value)
    
    def __str__(self) -> str:
        return self._value.isoformat()