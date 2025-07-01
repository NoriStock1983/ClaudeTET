# データモデル仕様

## テーブル構成
## companymstテーブル
| 項目名                   | 型           | 主キー      | NOT NULL |
| ----------------------- | ------------ | ---------- | -------- |
| companycd               | nvarchar(3)  | PRIMARYKEY | NOT NULL |
| companynm               | nvarchar(50) |            | NOT NULL |
| companynm_short         | nvarchar(10) |            | NOT NULL |
| subcontract_class       | nvarchar(2)  |            | NOT NULL |
| created_by              | nvarchar(8)  |            | NOT NULL |
| created_date            | datetime     |            | NOT NULL |
| updated_by              | nvarchar(8)  |            | NOT NULL |
| updated_date            | datetime     |            | NOT NULL |
| updatecounter           | number       |            | NOT NULL |

