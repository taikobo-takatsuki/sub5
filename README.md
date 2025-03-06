# 日本語翻訳・カタカナ変換アプリケーション

このアプリケーションは外国語を日本語に翻訳し、その発音をカタカナで表示するウェブアプリケーションです。

## 機能

- 複数の言語から日本語への翻訳
- 翻訳結果の発音をカタカナで表示
- シンプルで使いやすいユーザーインターフェース

## 技術スタック

### バックエンド
- Python 3.10
- FastAPI
- Pykakasi (日本語のカタカナ変換)
- Googletrans (Google翻訳APIラッパー)

### フロントエンド
- Vue.js 3
- Vuetify 3
- Axios (HTTPクライアント)

### デプロイ
- Docker & Docker Compose
- GitHub Actions

## 開発環境のセットアップ

### 必要条件
- Docker と Docker Compose
- Git

### インストール手順

1. リポジトリをクローンする
```bash
git clone https://github.com/yourusername/translation-app.git
cd translation-app
```

2. Docker Composeでアプリケーションを起動する
```bash
docker-compose up
```

3. ブラウザで以下のURLにアクセスする
   - フロントエンド: http://localhost:8080
   - バックエンドAPI: http://localhost:8000
   - API ドキュメント: http://localhost:8000/docs

## 使用方法

1. トップページで翻訳したいテキストを入力します
2. 元の言語を選択します（自動検出も可能）
3. 「翻訳する」ボタンをクリックします
4. 翻訳結果と共にカタカナ発音が表示されます

## デプロイ

このアプリケーションはGitHub Actionsを使用して自動デプロイが可能です。設定方法については`.github/workflows/deploy.yml`を参照してください。

## ライセンス

[MIT](LICENSE)

## 謝辞

- このプロジェクトは[Pykakasi](https://github.com/miurahr/pykakasi)と[Googletrans](https://github.com/ssut/py-googletrans)のライブラリを使用しています。
- UIデザインには[Vuetify](https://vuetifyjs.com/)を使用しています。 