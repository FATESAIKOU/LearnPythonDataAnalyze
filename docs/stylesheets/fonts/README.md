# 字體檔案說明

## 問題
完整的 CJK 等寬字體（如 Source Han Mono）檔案大小約 10-20 MB，
會顯著增加網站載入時間。

## 建議方案

### 方案 A：使用系統字體（已在 CSS 中配置）
CSS 已配置 fallback 字體鏈：
- MS Gothic (Windows)
- Osaka-Mono (macOS)
- monospace (系統預設)

### 方案 B：使用輕量級 Web 字體
如需強制統一字體，建議：
1. 下載 Source Han Mono 的子集版本（只包含常用漢字）
2. 或使用 font-subset 工具減小字體檔案

## 下載方式（選用）

如果堅持要用完整字體，可以手動下載：

```bash
# Source Han Mono JP (完整版，約 15MB)
curl -L -o SourceHanMono-Regular.woff2 \
  "https://github.com/adobe-fonts/source-han-mono/releases/download/1.002/SourceHanMono.ttc"
```

建議使用工具將其轉換為 woff2 並子集化。
