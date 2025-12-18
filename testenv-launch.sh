#!/bin/bash

# ============================================
# Python データ分析学習環境 起動スクリプト
# ============================================

# 色の定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# スクリプトのディレクトリを取得
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# イメージ名とコンテナ名
IMAGE_NAME="python-data-analysis-learn"
CONTAINER_NAME="python-data-analysis-learn-container"

echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}  Python データ分析学習環境${NC}"
echo -e "${BLUE}============================================${NC}"
echo ""

# Docker がインストールされているか確認
if ! command -v docker &> /dev/null; then
    echo -e "${RED}エラー: Docker がインストールされていません。${NC}"
    echo "Docker をインストールしてから再度実行してください。"
    echo "https://docs.docker.com/get-docker/"
    exit 1
fi

# Docker が起動しているか確認
if ! docker info &> /dev/null; then
    echo -e "${RED}エラー: Docker が起動していません。${NC}"
    echo "Docker Desktop を起動してから再度実行してください。"
    exit 1
fi

# 既存のコンテナを停止・削除
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo -e "${YELLOW}既存のコンテナを停止・削除しています...${NC}"
    docker stop "$CONTAINER_NAME" &> /dev/null
    docker rm "$CONTAINER_NAME" &> /dev/null
fi

# イメージをビルド
echo -e "${GREEN}Docker イメージをビルドしています...${NC}"
echo "（初回は数分かかることがあります）"
echo ""

docker build -t "$IMAGE_NAME" "$SCRIPT_DIR"

if [ $? -ne 0 ]; then
    echo -e "${RED}エラー: Docker イメージのビルドに失敗しました。${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}コンテナを起動しています...${NC}"
echo ""

# コンテナを起動
docker run -d \
    --name "$CONTAINER_NAME" \
    -p 8888:8888 \
    -v "$SCRIPT_DIR:/workspace" \
    "$IMAGE_NAME"

if [ $? -ne 0 ]; then
    echo -e "${RED}エラー: コンテナの起動に失敗しました。${NC}"
    exit 1
fi

# 起動完了メッセージ
echo -e "${GREEN}============================================${NC}"
echo -e "${GREEN}  🎉 学習環境の起動が完了しました！${NC}"
echo -e "${GREEN}============================================${NC}"
echo ""
echo -e "ブラウザで以下の URL にアクセスしてください："
echo ""
echo -e "  ${BLUE}http://localhost:8888${NC}"
echo ""
echo -e "${YELLOW}【操作方法】${NC}"
echo "  - 新しいノートブック: File → New → Notebook"
echo "  - Python 3 を選択してコードを書き始めましょう"
echo ""
echo -e "${YELLOW}【終了方法】${NC}"
echo "  以下のコマンドを実行してください："
echo "  docker stop $CONTAINER_NAME"
echo ""
echo -e "${YELLOW}【再起動方法】${NC}"
echo "  このスクリプトを再度実行してください"
echo ""

# macOS の場合、自動でブラウザを開く
if [[ "$OSTYPE" == "darwin"* ]]; then
    sleep 2
    open "http://localhost:8888"
fi
