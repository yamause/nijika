# 概要

伊地知さんがあなたのDiscordを彩ります。
具体的には伊地知さんが参加しているDiscordでコマンドの実行やリアクションをすると伊地知さんが素晴らしい体験をあなたに届けます。
# 利用方法

## インストール

### ローカルにclone

```
# ssh接続
git clone git@nev-yo-sv-gitlab-01.asaasahi.com:neverneband/nijika.git

# https接続
git clone https://nev-yo-sv-gitlab-01.asaasahi.com/neverneband/nijika.git
```

### 環境変数の設定

envファイルもしくはexportで環境変数を定義してください。

```
export DEEPL_AUTHKEY="your deepl authkey"  # 翻訳機能利用時は設定必須
export DISCORD_BOT_TOKEN="your discord token"
```

### 起動

```
cd nijika
docker-compose build
docker-compose up -d
```

# 開発

開発時はルールに従って適切にIssueの発行及びMerge Requestを行ってください。

[Git運用](https://www.notion.so/Git-791ac03195ec43cebbbcc7bee5d58b56?pvs=4) を参照してね

## Cog

機能追加は `cogs` ディレクトリにPythonファイルを作成し `commands.Cog` を継承したCogクラスを新たに作成してください。
詳細は [Discord.py 公式リファレンス](https://discordpy.readthedocs.io/ja/latest/ext/commands/cogs.html) を参照してください。
