import pytest
from datetime import datetime
from src.domain.entities.companymst_maintenance import CompanymstMaintenance
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


class TestCompanymstMaintenance:
    """会社マスタメンテナンスエンティティのテスト"""
    
    def test_正常なインスタンス生成(self):
        """すべてのValueObjectを使用してインスタンスを生成できること"""
        # Arrange
        company_code = CompanyCode("001")
        company_name = CompanyName("テスト株式会社")
        company_short_name = CompanyShortName("テスト")
        subcontract_class = SubcontractClass("00")
        created_by = CreatedBy("user001")
        created_date = CreatedDate(datetime(2024, 1, 1, 10, 0, 0))
        updated_by = UpdatedBy("user001")
        updated_date = UpdatedDate(datetime(2024, 1, 1, 10, 0, 0))
        update_counter = UpdateCounter(0)
        
        # Act
        entity = CompanymstMaintenance(
            company_code=company_code,
            company_name=company_name,
            company_short_name=company_short_name,
            subcontract_class=subcontract_class,
            created_by=created_by,
            created_date=created_date,
            updated_by=updated_by,
            updated_date=updated_date,
            update_counter=update_counter
        )
        
        # Assert
        assert entity.company_code == company_code
        assert entity.company_name == company_name
        assert entity.company_short_name == company_short_name
        assert entity.subcontract_class == subcontract_class
        assert entity.created_by == created_by
        assert entity.created_date == created_date
        assert entity.updated_by == updated_by
        assert entity.updated_date == updated_date
        assert entity.update_counter == update_counter
    
    def test_createメソッドでインスタンス生成(self):
        """プリミティブ値の辞書からインスタンスを生成できること"""
        # Arrange
        data = {
            "company_code": "002",
            "company_name": "サンプル会社",
            "company_short_name": "サンプル",
            "subcontract_class": "01",
            "created_by": "admin",
            "created_date": datetime(2024, 1, 1, 9, 0, 0),
            "updated_by": "admin",
            "updated_date": datetime(2024, 1, 1, 9, 0, 0),
            "update_counter": 1
        }
        
        # Act
        entity = CompanymstMaintenance.create(data)
        
        # Assert
        assert entity.company_code.value == "002"
        assert entity.company_name.value == "サンプル会社"
        assert entity.company_short_name.value == "サンプル"
        assert entity.subcontract_class.value == "01"
        assert entity.created_by.value == "admin"
        assert entity.created_date.value == datetime(2024, 1, 1, 9, 0, 0)
        assert entity.updated_by.value == "admin"
        assert entity.updated_date.value == datetime(2024, 1, 1, 9, 0, 0)
        assert entity.update_counter.value == 1
    
    def test_to_dictメソッド(self):
        """エンティティをプリミティブ値の辞書に変換できること"""
        # Arrange
        entity = CompanymstMaintenance(
            company_code=CompanyCode("003"),
            company_name=CompanyName("変換テスト会社"),
            company_short_name=CompanyShortName("変換テスト"),
            subcontract_class=SubcontractClass("02"),
            created_by=CreatedBy("user002"),
            created_date=CreatedDate(datetime(2024, 1, 2, 10, 0, 0)),
            updated_by=UpdatedBy("user003"),
            updated_date=UpdatedDate(datetime(2024, 1, 3, 10, 0, 0)),
            update_counter=UpdateCounter(5)
        )
        
        # Act
        result = entity.to_dict()
        
        # Assert
        assert result == {
            "company_code": "003",
            "company_name": "変換テスト会社",
            "company_short_name": "変換テスト",
            "subcontract_class": "02",
            "created_by": "user002",
            "created_date": datetime(2024, 1, 2, 10, 0, 0),
            "updated_by": "user003",
            "updated_date": datetime(2024, 1, 3, 10, 0, 0),
            "update_counter": 5
        }
    
    def test_等価性判定(self):
        """同じ値を持つエンティティが等しいと判定されること"""
        # Arrange
        data = {
            "company_code": "004",
            "company_name": "等価テスト会社",
            "company_short_name": "等価テスト",
            "subcontract_class": "00",
            "created_by": "testuser",
            "created_date": datetime(2024, 1, 1, 12, 0, 0),
            "updated_by": "testuser",
            "updated_date": datetime(2024, 1, 1, 12, 0, 0),
            "update_counter": 0
        }
        
        # Act
        entity1 = CompanymstMaintenance.create(data)
        entity2 = CompanymstMaintenance.create(data)
        
        # Assert
        assert entity1 == entity2
    
    def test_異なる会社コードのエンティティは等しくない(self):
        """異なる会社コードを持つエンティティが等しくないと判定されること"""
        # Arrange
        entity1 = CompanymstMaintenance.create({
            "company_code": "005",
            "company_name": "会社A",
            "company_short_name": "A社",
            "subcontract_class": "00",
            "created_by": "user",
            "created_date": datetime(2024, 1, 1),
            "updated_by": "user",
            "updated_date": datetime(2024, 1, 1),
            "update_counter": 0
        })
        
        entity2 = CompanymstMaintenance.create({
            "company_code": "006",
            "company_name": "会社A",
            "company_short_name": "A社",
            "subcontract_class": "00",
            "created_by": "user",
            "created_date": datetime(2024, 1, 1),
            "updated_by": "user",
            "updated_date": datetime(2024, 1, 1),
            "update_counter": 0
        })
        
        # Act & Assert
        assert entity1 != entity2
    
    def test_updateメソッドで更新情報を反映(self):
        """updateメソッドで更新者、更新日時、カウンタが更新されること"""
        # Arrange
        entity = CompanymstMaintenance.create({
            "company_code": "007",
            "company_name": "更新テスト会社",
            "company_short_name": "更新テスト",
            "subcontract_class": "00",
            "created_by": "creator",
            "created_date": datetime(2024, 1, 1, 10, 0, 0),
            "updated_by": "creator",
            "updated_date": datetime(2024, 1, 1, 10, 0, 0),
            "update_counter": 0
        })
        
        # Act
        updated_entity = entity.update(
            company_name="更新後会社名",
            company_short_name="更新後",
            subcontract_class="01",
            updated_by="updater",
            updated_date=datetime(2024, 1, 2, 15, 0, 0)
        )
        
        # Assert
        assert updated_entity.company_code.value == "007"  # 変更されない
        assert updated_entity.company_name.value == "更新後会社名"
        assert updated_entity.company_short_name.value == "更新後"
        assert updated_entity.subcontract_class.value == "01"
        assert updated_entity.created_by.value == "creator"  # 変更されない
        assert updated_entity.created_date.value == datetime(2024, 1, 1, 10, 0, 0)  # 変更されない
        assert updated_entity.updated_by.value == "updater"
        assert updated_entity.updated_date.value == datetime(2024, 1, 2, 15, 0, 0)
        assert updated_entity.update_counter.value == 1  # インクリメントされる