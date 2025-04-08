# Architecture

project-root/
├── backend/                   # ← ここだけ追加されました（内容はそのまま）
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                # エントリーポイント（ASGIアプリ）
│   │   ├── config.py              # 環境変数や設定読み込み
│   │   ├── api/                   # APIルーティング層
│   │   │   ├── __init__.py
│   │   │   ├── auth/              # 認証系（Google OAuth等、FastAPIで実装）
│   │   │   │   ├── __init__.py
│   │   │   │   └── routes.py      # /auth/google/login, /auth/google/callback
│   │   │   ├── groups/            # グループ管理エンドポイント
│   │   │   │   ├── __init__.py
│   │   │   │   └── routes.py      # /groups, /groups/{group_id} など
│   │   │   ├── members/           # グループメンバー招待/管理エンドポイント
│   │   │   │   ├── __init__.py
│   │   │   │   └── routes.py      # /groups/{group_id}/members など
│   │   │   └── todos/             # Todo管理エンドポイント（グループ内）
│   │   │       ├── __init__.py
│   │   │       └── routes.py      # /groups/{group_id}/todos など
│   │   ├── core/                  # 共通基盤（セキュリティ、ロギング）
│   │   │   ├── __init__.py
│   │   │   ├── security.py        # JWT認証関連
│   │   │   └── logger.py          # ロギング設定
│   │   ├── schemas/               # Pydanticスキーマ
│   │   │   ├── __init__.py
│   │   │   ├── group.py
│   │   │   ├── user.py
│   │   │   └── todo.py
│   │   ├── services/              # ビジネスロジック層（Supabase API呼び出しラッパー）
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py    # 認証（FastAPI側）
│   │   │   ├── group_service.py   # グループ管理ロジック
│   │   │   ├── member_service.py  # メンバー管理ロジック
│   │   │   └── todo_service.py    # Todo管理ロジック
│   │   └── utils/                 # 共通ユーティリティ
│   │       ├── __init__.py
│   │       └── supabase_client.py # Supabase APIクライアントのラッパー
│   ├── tests/                       # テストコード全体のルートディレクトリ
│   │   ├── __init__.py              # testsパッケージとして認識させるためのファイル
│   │   ├── conftest.py              # 共通フィクスチャや設定を定義（例：TestClient、モックのSupabaseClient、JWTトークン生成など）
│   │   ├── unit/                    # ユニットテスト用のディレクトリ（各サービスやユーティリティのテスト）
│   │   │   ├── __init__.py
│   │   │   ├── test_auth_service.py    # auth_service.py の関数単位のテスト
│   │   │   ├── test_group_service.py   # group_service.py のテスト
│   │   │   ├── test_member_service.py  # member_service.py のテスト
│   │   │   ├── test_todo_service.py    # todo_service.py のテスト
│   │   │   └── test_supabase_client.py # supabase_client.py のユニットテスト（外部APIモック化）
│   │   ├── integration/             # 統合テスト用のディレクトリ（APIルーティング層や、サービスとutilsの連携テスト）
│   │   │   ├── __init__.py
│   │   │   ├── test_auth_routes.py     # /auth/google/～ のルーティングおよび認証処理の統合テスト
│   │   │   ├── test_group_routes.py    # /groups ルート関連のテスト（正常系・異常系を含む）
│   │   │   ├── test_member_routes.py   # /groups/{group_id}/members のテスト
│   │   │   └── test_todo_routes.py     # /groups/{group_id}/todos のテスト
│   │   └── e2e/                     # エンドツーエンドテスト用ディレクトリ（必要に応じてブラウザ操作やAPI全体のテスト）
│   │       ├── __init__.py
│   │       └── test_end_to_end.py   # アプリ全体のフロー（ログインからグループ作成、Todo登録までなど）のテスト
│   ├── docker-compose.yml         # コンテナ構築用設定（FastAPIとSupabase）
│   ├── Dockerfile                 # アプリケーションDockerイメージビルド設定
│   ├── requirements.txt           # Pythonパッケージ一覧
