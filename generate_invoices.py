
import pandas as pd
from jinja2 import Template
from weasyprint import HTML
import os

# 顧客データの読み込み
df = pd.read_csv("customers.csv")

# HTMLテンプレートの読み込み
with open("invoice_template.html", "r", encoding="utf-8") as f:
    html_template = f.read()

template = Template(html_template)

# PDF保存先ディレクトリ作成
output_dir = "invoices"
os.makedirs(output_dir, exist_ok=True)

# スタイルシート（日本語フォント）
css = """
@font-face {
    font-family: 'Noto Sans CJK';
    src: url('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc');
}
body {
    font-family: 'Noto Sans CJK', sans-serif;
}
"""

# 顧客ごとにPDFを作成
for index, record in df.iterrows():
    total_price = record["unit_price"] * record["quantity"]
    
    rendered_html = template.render(
        company=record["company"],
        person=record["person"],
        item=record["item"],
        unit_price=record["unit_price"],
        quantity=record["quantity"],
        total_price=total_price
    )

    pdf_filename = f"{output_dir}/{record['person']}_invoice.pdf"
    HTML(string=rendered_html).write_pdf(pdf_filename, stylesheets=[css])
    print(f"{record['person']} さんの請求書を作成しました。")
