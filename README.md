# 請求書自動生成ツール（Books-to-Scrape風）

このプロジェクトは、Pythonを使って顧客情報から請求書（PDF）を自動生成する業務自動化ツールです。  
CSVファイルで渡された顧客情報を元に、HTMLテンプレートをレンダリングし、PDFで保存します。

---

## 🔧 使用技術

- Python 
- pandas
- Jinja2
- WeasyPrint（PDF生成）
- Google Colab（開発環境）

---


## 📝 機能

- 顧客ごとの請求書を自動作成（PDF形式）
- HTMLテンプレートをJinja2で動的に変換
- 日本語フォント対応（Google Colab上で確認済み）
- 出力先ディレクトリを自動生成

---

## 🚀 使い方（Google Colab）

1. `customers.csv` に顧客情報を入力
2. `invoice_template.html` にテンプレートを記述
3. `generate_invoices.py` を実行
4. `invoices/` フォルダにPDFが自動生成されます

---

## 📌 注意

- WeasyPrint は日本語PDF生成に対応していますが、ローカル環境ではCライブラリが必要です（Colab推奨）
- `.gitignore` によりPDFファイルはGitHubに含まれていません

---

## 📄 ライセンス

MIT License
