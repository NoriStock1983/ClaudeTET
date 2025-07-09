from datetime import datetime
from typing import Dict, Any
from src.domain.valueobject.companymst import (
    CompanyCode,
    CompanyName,
    CompanyShortName,
    SubcontractClass,
    CreatedBy,
    CreatedDate,
    UpdatedBy,
    UpdatedDate,
    UpdateCounter
)


class CompanymstMaintenance:
    """会社マスタメンテナンスエンティティ"""
    
    def __init__(
        self,
        company_code: CompanyCode,
        company_name: CompanyName,
        company_short_name: CompanyShortName,
        subcontract_class: SubcontractClass,
        created_by: CreatedBy,
        created_date: CreatedDate,
        updated_by: UpdatedBy,
        updated_date: UpdatedDate,
        update_counter: UpdateCounter
    ):
        """
        会社マスタメンテナンスエンティティのコンストラクタ
        
        Args:
            company_code: 会社コード
            company_name: 会社名
            company_short_name: 会社名略称
            subcontract_class: 外注区分
            created_by: 作成者
            created_date: 作成日時
            updated_by: 更新者
            updated_date: 更新日時
            update_counter: 更新カウンタ
        """
        self._company_code = company_code
        self._company_name = company_name
        self._company_short_name = company_short_name
        self._subcontract_class = subcontract_class
        self._created_by = created_by
        self._created_date = created_date
        self._updated_by = updated_by
        self._updated_date = updated_date
        self._update_counter = update_counter
    
    @classmethod
    def create(cls, data: Dict[str, Any]) -> 'CompanymstMaintenance':
        """
        プリミティブ値の辞書からエンティティを生成するファクトリメソッド
        
        Args:
            data: プリミティブ値の辞書
        
        Returns:
            CompanymstMaintenanceインスタンス
        """
        return cls(
            company_code=CompanyCode(data['company_code']),
            company_name=CompanyName(data['company_name']),
            company_short_name=CompanyShortName(data['company_short_name']),
            subcontract_class=SubcontractClass(data['subcontract_class']),
            created_by=CreatedBy(data['created_by']),
            created_date=CreatedDate(data['created_date']),
            updated_by=UpdatedBy(data['updated_by']),
            updated_date=UpdatedDate(data['updated_date']),
            update_counter=UpdateCounter(data['update_counter'])
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        エンティティをプリミティブ値の辞書に変換
        
        Returns:
            プリミティブ値の辞書
        """
        return {
            'company_code': self._company_code.value,
            'company_name': self._company_name.value,
            'company_short_name': self._company_short_name.value,
            'subcontract_class': self._subcontract_class.value,
            'created_by': self._created_by.value,
            'created_date': self._created_date.value,
            'updated_by': self._updated_by.value,
            'updated_date': self._updated_date.value,
            'update_counter': self._update_counter.value
        }
    
    def update(
        self,
        company_name: str,
        company_short_name: str,
        subcontract_class: str,
        updated_by: str,
        updated_date: datetime
    ) -> 'CompanymstMaintenance':
        """
        エンティティを更新した新しいインスタンスを返す
        
        Args:
            company_name: 新しい会社名
            company_short_name: 新しい会社名略称
            subcontract_class: 新しい外注区分
            updated_by: 更新者
            updated_date: 更新日時
        
        Returns:
            更新された新しいCompanymstMaintenanceインスタンス
        """
        return CompanymstMaintenance(
            company_code=self._company_code,  # 会社コードは変更不可
            company_name=CompanyName(company_name),
            company_short_name=CompanyShortName(company_short_name),
            subcontract_class=SubcontractClass(subcontract_class),
            created_by=self._created_by,  # 作成者は変更不可
            created_date=self._created_date,  # 作成日時は変更不可
            updated_by=UpdatedBy(updated_by),
            updated_date=UpdatedDate(updated_date),
            update_counter=self._update_counter.increment()  # カウンタをインクリメント
        )
    
    def __eq__(self, other: object) -> bool:
        """
        等価性判定（会社コードで判定）
        
        Args:
            other: 比較対象
        
        Returns:
            同じ会社コードを持つ場合True
        """
        if not isinstance(other, CompanymstMaintenance):
            return False
        return self._company_code == other._company_code
    
    # プロパティ
    @property
    def company_code(self) -> CompanyCode:
        return self._company_code
    
    @property
    def company_name(self) -> CompanyName:
        return self._company_name
    
    @property
    def company_short_name(self) -> CompanyShortName:
        return self._company_short_name
    
    @property
    def subcontract_class(self) -> SubcontractClass:
        return self._subcontract_class
    
    @property
    def created_by(self) -> CreatedBy:
        return self._created_by
    
    @property
    def created_date(self) -> CreatedDate:
        return self._created_date
    
    @property
    def updated_by(self) -> UpdatedBy:
        return self._updated_by
    
    @property
    def updated_date(self) -> UpdatedDate:
        return self._updated_date
    
    @property
    def update_counter(self) -> UpdateCounter:
        return self._update_counter