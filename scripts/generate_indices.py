import os

def generate_sub_readmes():
    directories = [
        'Anthropic', 'Anthropic/old',
        'Google',
        'Misc',
        'OpenAI', 'OpenAI/API', 'OpenAI/Old',
        'Perplexity',
        'xAI'
    ]
    
    category_links = []

    for dir_path in directories:
        if not os.path.exists(dir_path):
            continue
            
        files = os.listdir(dir_path)
        # 篩選出有翻譯對應的原始檔案
        pairs = []
        for f in sorted(files):
            if f.endswith('_zh_TW.md') or f.endswith('_zh_TW.xml') or f.endswith('_zh_TW.txt'):
                original_f = f.replace('_zh_TW.', '.')
                if original_f in files:
                    pairs.append((original_f, f))
        
        if not pairs:
            continue
            
        # 生成子目錄 README.md
        title = dir_path.replace('/', ' > ')
        readme_content = f"# {title} 提示詞索引\n\n"
        readme_content += "| 提示詞名稱 | 原文 (English) | 繁體中文 (Chinese) |\n"
        readme_content += "| :--- | :--- | :--- |\n"
        
        for orig, trans in pairs:
            name = orig.rsplit('.', 1)[0]
            readme_content += f"| {name} | [Original](./{orig}) | [繁體中文](./{trans}) |\n"
            
        with open(os.path.join(dir_path, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(readme_content)
            
        category_links.append((dir_path, os.path.join(dir_path, 'README.md')))

    # 更新根目錄 README_zh_TW.md
    root_readme = """# System Prompts Leaks (繁體中文版)

[English](readme.md)

本專案收集了各大 AI 模型的系統提示詞、系統訊息與開發者訊息，並提供高品質的繁體中文（台灣用語）翻譯。

## 目錄索引

"""
    for cat_name, cat_path in category_links:
        root_readme += f"- [{cat_name}]({cat_path})\n"
        
    root_readme += """
## 參與貢獻

歡迎提交 Pull Requests (PR) 以更新或增加新的提示詞。

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=asgeirtj/system_prompts_leaks&type=Date)](https://www.star-history.com/#asgeirtj/system_prompts_leaks&Date)
"""
    
    with open('README_zh_TW.md', 'w', encoding='utf-8') as f:
        f.write(root_readme)

if __name__ == "__main__":
    generate_sub_readmes()
    print("成功生成子目錄 README.md 並更新根目錄索引。")
