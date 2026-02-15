
import os

def generate_progress_md():
    files = []
    # Relevant extensions for system prompts
    extensions = ('.md', '.xml', '.txt')
    
    for root, dirs, files_in_dir in os.walk("."):
        if '.git' in root or 'node_modules' in root or 'scripts' in root:
            continue
            
        for file in files_in_dir:
            if file.lower().endswith(extensions):
                rel_path = os.path.relpath(os.path.join(root, file), ".")
                if rel_path in ["PROGRESS.md"] or rel_path.endswith("_zh_TW.md") or rel_path.endswith("_zh_TW.xml") or rel_path.endswith("_zh_TW.txt"):
                    continue
                # We want README to be separate at the top
                if rel_path.lower() == "readme.md":
                    continue
                
                files.append(rel_path)

    files.sort()

    # Track already completed files from current PROGRESS.md
    completed = set()
    if os.path.exists("PROGRESS.md"):
        with open("PROGRESS.md", "r") as f:
            for line in f:
                if "[x]" in line:
                    # Extract path between []
                    start = line.find("[") + 4 # skip "[x] ["
                    end = line.find("]", start)
                    if start > 3 and end > start:
                        path = line[start:end]
                        completed.add(path)

    content = "# Translation Progress\n\n"
    # Special handling for README
    readme_status = "[x]" if "readme.md" in completed else "[ ]"
    content += f"- {readme_status} [readme.md](readme.md)\n"
    
    for file_path in files:
        status = "[x]" if file_path in completed else "[ ]"
        content += f"- {status} [{file_path}]({file_path})\n"

    with open("PROGRESS.md", "w") as f:
        f.write(content)
        
    print(f"Updated PROGRESS.md with {len(files) + 1} files.")

if __name__ == "__main__":
    generate_progress_md()
