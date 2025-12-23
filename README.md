# Python データ分析入門

プログラミング未経験者向けの Python データ分析教材です。

📖 **オンラインドキュメント**: https://fatesaikou.github.io/LearnPythonDataAnalyze/

---

## 📚 目次

- [学習者向け：教材の使い方](#学習者向け教材の使い方)
- [開発者向け：ドキュメント発行方法](#開発者向けドキュメント発行方法)

---

## 学習者向け：教材の使い方

### 1. 学習環境の起動

Docker を使って JupyterLab 環境を起動します。

```bash
# 方法1: スクリプトを使用（推奨）
./testenv-launch.sh

# 方法2: 手動で Docker を起動
docker build -t python-data-analysis-learn .
docker run -p 8888:8888 -v $(pwd):/workspace python-data-analysis-learn
```

起動後、ブラウザで以下にアクセス：

```
http://localhost:8888
```

### 2. 学習の進め方

各章（CH1〜CH8）は以下の構成になっています：

```
CHx-章タイトル/
├── ch-overview.md      # 章の概要
├── introduction.md     # 導入説明
└── Section1-セクション名/
    ├── 技術説明.md      # ① まず読む：概念と基本的な使い方
    ├── 演習.md          # ② 次に挑戦：手を動かして学ぶ練習問題
    └── 応用問題.md      # ③ 最後に挑戦：実践的な課題
```

#### Step 1: 技術説明を読む 📖

各セクションの `技術説明.md` を読んで、概念と基本的な使い方を理解します。

#### Step 2: 演習に挑戦 ✏️

`演習.md` の問題を JupyterLab で実際にコードを書いて解きます。

```python
# JupyterLab で新しいノートブックを作成
# 演習の指示に従ってコードを入力・実行
```

#### Step 3: 応用問題に挑戦 🚀

`応用問題.md` で実践的な課題に取り組みます。
自分でコードを設計・実装してみましょう。

#### Step 4: AI に質問 🤖

分からないことがあれば、いつでも AI アシスタントに質問できます：

- コードの解説を依頼
- エラーの原因を調査
- ヒントをもらう
- 解答例を確認

### 3. 推奨学習順序

| 順序 | 章 | 内容 | 想定時間 |
|------|-----|------|----------|
| 1 | CH1 | Python 基礎 | 2-3時間 |
| 2 | CH2 | 制御構文 | 2-3時間 |
| 3 | CH3 | 関数とモジュール | 2-3時間 |
| 4 | CH4 | NumPy 入門 | 2-3時間 |
| 5 | CH5 | Pandas 入門 | 3-4時間 |
| 6 | CH6 | Pandas 応用 | 3-4時間 |
| 7 | CH7 | Matplotlib 入門 | 2-3時間 |
| 8 | CH8 | 総合演習 | 4-5時間 |

---

## 開発者向け：ドキュメント発行方法

本教材は [MkDocs](https://www.mkdocs.org/) + [Material Theme](https://squidfunk.github.io/mkdocs-material/) を使用してドキュメントサイトを生成しています。

### 1. 環境準備

```bash
# MkDocs と Material テーマをインストール
pip install mkdocs mkdocs-material
```

### 2. ローカルでテスト編集

```bash
# ドキュメントをビルド（エラーチェック）
mkdocs build

# 成功すると site/ フォルダに静的サイトが生成される
```

### 3. ローカルでプレビュー

```bash
# 開発サーバーを起動
mkdocs serve

# ブラウザで確認
# http://127.0.0.1:8000
```

ファイルを編集すると自動的にリロードされます。

### 4. 正式発行フロー

本番サイトへの発行は **GitHub Actions** で自動化されています。

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ドキュメント発行フロー                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ローカル環境                                                      │
│   ┌────────────────┐                                                │
│   │  ファイル編集  │.                                               │
│   │  (docs/*.md)   │                                                │
│   └──────┬─────────┘                                                │
│          │                                                          │
│          ▼                                                          │
│   ┌──────────────┐                                                  │
│   │  git commit  │                                                  │
│   │  git push    │───────────┐                                      │
│   └──────────────┘           │                                      │
│                              │                                      │
│   ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   │
│                              │                                      │
│   GitHub                     ▼                                      │
│   ┌─────────────────────────────────────────────────────────┐       │
│   │                      main ブランチ                      │       │
│   └──────────────────────────┬──────────────────────────────┘       │
│                              │                                      │
│                              │ push をトリガー                      │
│                              ▼                                      │
│   ┌─────────────────────────────────────────────────────────┐       │
│   │                   GitHub Actions                        │       │
│   │  ┌─────────────────────────────────────────────────┐    │       │
│   │  │  1. actions/checkout      - コード取得          │    │       │
│   │  │  2. actions/setup-python  - Python セットアップ │    │       │
│   │  │  3. pip install           - MkDocs インストール │    │       │
│   │  │  4. mkdocs build          - サイトビルド        │    │       │
│   │  │  5. actions/upload-pages-artifact               │    │       │
│   │  │  6. actions/deploy-pages  - デプロイ            │    │       │
│   │  └─────────────────────────────────────────────────┘    │       │
│   └──────────────────────────┬──────────────────────────────┘       │
│                              │                                      │
│                              ▼                                      │
│   ┌──────────────────────────────────────────────────────────┐      │
│   │                    GitHub Pages                          │      │
│   │                                                          │      │
│   │     https://fatesaikou.github.io/LearnPythonDataAnalyze/ │      │
│   │                                                          │      │
│   └──────────────────────────────────────────────────────────┘      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

#### 発行手順

```bash
# 1. 変更をコミット
git add -A
git commit -m "docs: Update documentation"

# 2. main ブランチにプッシュ
git push origin main

# 3. GitHub Actions が自動実行される
#    （進捗は GitHub の Actions タブで確認可能）

# 4. 数分後、サイトが更新される
#    https://fatesaikou.github.io/LearnPythonDataAnalyze/
```

### 5. ファイル構成

```
LearnPythonDataAnalyze/
├── mkdocs.yml                    # MkDocs 設定ファイル
├── docs/                         # ドキュメントソース
│   ├── index.md                  # トップページ
│   ├── stylesheets/
│   │   └── custom.css            # カスタムスタイル
│   ├── CH1-Python基礎/           # 各章のコンテンツ
│   ├── CH2-Python制御構文/
│   └── ...
├── .github/workflows/
│   └── deploy-mkdocs.yml         # GitHub Actions 設定
├── Dockerfile                    # 学習環境用
└── testenv-launch.sh             # 環境起動スクリプト
```

---

## ライセンス

This project is for educational purposes.

---

## 貢献

Issue や Pull Request を歓迎します！
