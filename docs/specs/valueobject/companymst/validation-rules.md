  #### バリデーションルール

  ##### companycd（会社コード）
  - **データ型**: 文字列
  - **最大長**: 3文字
  - **必須**: Yes
  - **許可文字**: 半角数字のみ（0-9）
  - **パターン**: `^\d{1,3}$`
  - **例**: "001", "999", "12"
  - **エラーメッセージ**:
    - 必須エラー: "会社コードは必須です"
    - 型エラー: "会社コードは文字列である必要があります"
    - 長さエラー: "会社コードは3文字以内である必要があります"
    - フォーマットエラー: "会社コードは半角数字のみ使用できます"

  ##### companynm（会社名）
  - **データ型**: 文字列
  - **最大長**: 50文字
  - **必須**: Yes
  - **許可文字**: 全角・半角文字
  - **禁止文字**: 特殊記号（<, >, &, ", '）
  - **エラーメッセージ**:
    - 必須エラー: "会社名は必須です"
    - 長さエラー: "会社名は50文字以内である必要があります"
    - 禁止文字エラー: "会社名に使用できない文字が含まれています"

  ##### companynm_short（会社名略称）
  - **データ型**: 文字列
  - **最大長**: 10文字
  - **必須**: Yes
  - **許可文字**: 全角・半角文字
  - **エラーメッセージ**:
    - 必須エラー: "会社名（略称）は必須です"
    - 長さエラー: "会社名（略称）は10文字以内である必要があります"

  ##### subcontract_class（外注区分）
  - **データ型**: 文字列
  - **最大長**: 2文字
  - **必須**: Yes
  - **許可値**: "00"（自社）, "01"（外注）, "02"（協力会社）
  - **エラーメッセージ**:
    - 必須エラー: "外注区分は必須です"
    - 許可値エラー: "外注区分は00, 01, 02のいずれかである必要があります"

  ##### created_by / updated_by（作成者・更新者）
  - **データ型**: 文字列
  - **最大長**: 8文字
  - **必須**: Yes
  - **許可文字**: 半角英数字のみ
  - **パターン**: `^[A-Za-z0-9]{1,8}$`
  - **エラーメッセージ**:
    - 必須エラー: "作成者/更新者は必須です"
    - フォーマットエラー: "作成者/更新者は半角英数字8文字以内である必要があります"

  ##### updatecounter（更新カウンタ）
  - **データ型**: 整数
  - **範囲**: 0以上
  - **初期値**: 0
  - **更新時**: +1
  - **エラーメッセージ**:
    - 型エラー: "更新カウンタは整数である必要があります"
    - 範囲エラー: "更新カウンタは0以上である必要があります"
