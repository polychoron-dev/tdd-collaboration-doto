# Architecture

project-root/
├── app/
│   ├── __init__.py
│   ├── main.py                # エントリーポイント（ASGIアプリ）
│   ├── config.py              # 環境変数や設定読み込み
│   ├── api/                   # APIルーティング層
│   │   ├── __init__.py
│   │   ├── auth/              # 認証系（Google OAuth等、FastAPIで実装）
│   │   │   ├── __init__.py
│   │   │   └── routes.py      # /auth/google/login, /auth/google/callback
│   │   ├── groups/            # グループ管理エンドポイント
│   │   │   ├── __init__.py
│   │   │   └── routes.py      # /groups, /groups/{group_id} など
│   │   ├── members/           # グループメンバー招待/管理エンドポイント
│   │   │   ├── __init__.py
│   │   │   └── routes.py      # /groups/{group_id}/members など
│   │   └── todos/             # Todo管理エンドポイント（グループ内）
│   │       ├── __init__.py
│   │       └── routes.py      # /groups/{group_id}/todos など
│   ├── core/                  # 共通基盤（セキュリティ、ロギング）
│   │   ├── __init__.py
│   │   ├── security.py        # JWT認証関連
│   │   └── logger.py          # ロギング設定
│   ├── schemas/               # Pydanticスキーマ
│   │   ├── __init__.py
│   │   ├── group.py
│   │   ├── user.py
│   │   └── todo.py
│   ├── services/              # ビジネスロジック層（Supabase API呼び出しラッパー）
│   │   ├── __init__.py
│   │   ├── auth_service.py    # 認証（FastAPI側）
│   │   ├── group_service.py   # グループ管理ロジック
│   │   ├── member_service.py  # メンバー管理ロジック
│   │   └── todo_service.py    # Todo管理ロジック
│   └── utils/                 # 共通ユーティリティ
│       ├── __init__.py
│       └── supabase_client.py # Supabase APIクライアントのラッパー
├── tests/                     # TDD用テストコード
│   ├── __init__.py
│   ├── conftest.py            # 共通フィクスチャ、テスト設定
│   ├── test_auth.py           # 認証系のテスト
│   ├── test_groups.py         # グループ管理機能のテスト
│   ├── test_members.py        # グループメンバー管理のテスト
│   └── test_todos.py          # Todo管理機能のテスト
├── scripts/                   # 補助スクリプト（Supabaseのマイグレーション等、必要なら）
│   └── migrate.py
├── docker-compose.yml         # コンテナ構築用設定（FastAPIとSupabase）
├── Dockerfile                 # アプリケーションDockerイメージビルド設定
├── requirements.txt           # Pythonパッケージ一覧
└── README.md                  # プロジェクト概要、セットアップ手順