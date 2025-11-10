from transformers import BertTokenizer, BertModel

print("Đang tải mô hình BERT (bert-base-uncased)...")
BertTokenizer.from_pretrained("bert-base-uncased")
BertModel.from_pretrained("bert-base-uncased")
print("✅ Đã tải xong và lưu vào cache Hugging Face.")
