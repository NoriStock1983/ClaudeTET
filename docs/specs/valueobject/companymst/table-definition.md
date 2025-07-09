  #### テーブル定義
  | 項目名 | 型 | 主キー | NOT NULL | 説明 |
  | --- | --- | --- | --- | --- |
  | companycd | nvarchar(3) | PRIMARY KEY | NOT NULL | 会社コード |
  | companynm | nvarchar(50) | | NOT NULL | 会社名 |
  | companynm_short | nvarchar(10) | | NOT NULL | 会社名（略称） |
  | subcontract_class | nvarchar(2) | | NOT NULL | 外注区分 |
  | created_by | nvarchar(8) | | NOT NULL | 作成者 |
  | created_date | datetime | | NOT NULL | 作成日時 |
  | updated_by | nvarchar(8) | | NOT NULL | 更新者 |
  | updated_date | datetime | | NOT NULL | 更新日時 |
  | updatecounter | number | | NOT NULL | 更新カウンタ |
