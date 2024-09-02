import os
import random
import zipfile

# Define the directory to store mock files
mock_dir = 'mock_files'
os.makedirs(mock_dir, exist_ok=True)

# Define file categories and their extensions
fileCategories = {
    "PDFs": [".pdf"],
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".ico"],
    "Documents": [".doc", ".docx", ".odt", ".txt", ".rtf", ".md", ".tex", ".pdf"],
    "Data": [".csv", ".json", ".xml", ".xls", ".xlsx", ".sql", ".db", ".dbf", ".mdb", ".accdb"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz", ".iso"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".bin", ".cmd", ".com", ".jar"],
    "Music": [".mp3", ".wav", ".wma", ".aac", ".flac", ".ogg", ".m4a", ".aiff"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".webm", ".mpeg", ".mpg", ".m4v"],
    "Presentations": [".ppt", ".pptx", ".odp", ".key"],
    "Spreadsheets": [".xls", ".xlsx", ".ods", ".csv"],
    "Code": [".js", ".jsx", ".ts", ".tsx", ".html", ".css", ".scss", ".py", ".java", ".c", ".cpp", ".cs", ".rb", ".php", ".go", ".rs", ".swift", ".kt", ".sh", ".bat", ".pl", ".r", ".m", ".vb", ".vbs"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    "System": [".dll", ".sys", ".ini", ".log", ".cfg", ".conf"],
    "DiskImages": [".iso", ".img", ".dmg", ".vhd", ".vmdk"],
    "Web": [".html", ".htm", ".css", ".scss", ".js", ".jsx", ".ts", ".tsx", ".json", ".xml", ".yml", ".yaml"],
    "Scripts": [".sh", ".bat", ".cmd", ".ps1", ".pl", ".py", ".rb", ".php", ".js", ".ts"],
    "Backup": [".bak", ".tmp", ".old"],
    "Config": [".ini", ".cfg", ".conf", ".json", ".xml", ".yaml", ".yml"],
    "Text": [".txt", ".md", ".rtf", ".tex"],
}

# Flatten the list of extensions
all_extensions = [ext for exts in fileCategories.values() for ext in exts]

amount = 1000

# Generate 100 mock files
for i in range(amount):
    ext = random.choice(all_extensions)
    file_name = f'file_{i+1}{ext}'
    file_path = os.path.join(mock_dir, file_name)
    with open(file_path, 'w') as f:
        f.write(f'This is a mock file for {file_name}')

# Compress the files into a zip archive
zip_file_name = 'mock_files.zip'
with zipfile.ZipFile(zip_file_name, 'w') as zipf:
    for root, _, files in os.walk(mock_dir):
        for file in files:
            zipf.write(os.path.join(root, file), arcname=file)

print(f'Created {zip_file_name} with {amount} mock files.')