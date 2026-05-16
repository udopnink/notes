import os
import argparse
import datetime
import re
from pathlib import Path

# Configuration
BRAIN_DIR = Path("brain_data")
DIRS = ["inbox", "concepts", "entities", "tools", "journals"]

def slugify(text):
    """Convert text to a filename-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '_', text)
    return text.strip('_')

def init_brain():
    """Initialize the brain directory structure."""
    if not BRAIN_DIR.exists():
        BRAIN_DIR.mkdir()
    
    for d in DIRS:
        (BRAIN_DIR / d).mkdir(exist_ok=True)
    
    print(f"Brain initialized at {BRAIN_DIR.absolute()}")

def create_note(title, category, content, tags=None, source=None):
    """Create a new markdown note with frontmatter."""
    if category not in DIRS:
        print(f"Error: Category '{category}' must be one of {DIRS}")
        return

    filename = f"{slugify(title)}.md"
    filepath = BRAIN_DIR / category / filename
    
    # Avoid overwriting existing notes (unless intentionally updating - simple logic for now)
    if filepath.exists():
        print(f"Warning: Note '{filename}' already exists. Appending timestamp to new filename.")
        filename = f"{slugify(title)}_{datetime.datetime.now().strftime('%H%M%S')}.md"
        filepath = BRAIN_DIR / category / filename

    # Prepare Frontmatter
    frontmatter = "---\n"
    frontmatter += f"title: \"{title}\"\n"
    frontmatter += f"created: {datetime.datetime.now().isoformat()}\n"
    frontmatter += f"type: {category}\n"
    if tags:
        tag_list = [t.strip() for t in tags.split(',')]
        frontmatter += f"tags: {tag_list}\n"
    if source:
        frontmatter += f"source: \"{source}\"\n"
    frontmatter += "---\n\n"

    # Write File
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        f.write(content)
    
    print(f"Note created: {filepath}")

def main():
    parser = argparse.ArgumentParser(description="Knowledge Base Manager")
    subparsers = parser.add_subparsers(dest="command")

    # init command
    subparsers.add_parser("init", help="Initialize the brain directories")

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("--title", required=True, help="Title of the note")
    add_parser.add_argument("--category", required=True, choices=DIRS, help="Category (folder)")
    add_parser.add_argument("--content", required=True, help="Content of the note")
    add_parser.add_argument("--tags", help="Comma-separated tags")
    add_parser.add_argument("--source", help="Source URL or origin")

    args = parser.parse_args()

    if args.command == "init":
        init_brain()
    elif args.command == "add":
        create_note(args.title, args.category, args.content, args.tags, args.source)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
