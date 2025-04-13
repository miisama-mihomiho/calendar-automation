from pdf2image import convert_from_path
from datetime import datetime
import os

# PDFファイルのパス（リポジトリ内またはダウンロード）
pdf_path = 'カレンダー.pdf'  # Google Driveからダウンロード済みと仮定

# 出力フォルダ
output_folder = 'output_images'
os.makedirs(output_folder, exist_ok=True)

images = convert_from_path(pdf_path)
for i, image in enumerate(images):
    image.save(f"{output_folder}/calendar_page_{i + 1}.png", "PNG")
  
