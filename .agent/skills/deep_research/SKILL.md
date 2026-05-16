---
name: Deep Research & Knowledge Extraction
description: A workflow for conducting deep research on a topic and storing the "essence" into a structured Knowledge Base (Second Brain).
---

# Deep Research & Knowledge Extraction Skill

This skill enables the agent to systematically research a topic, extract key insights, and store them in a permanent "Second Brain" using the `knowledge_manager.py` tool.

## Prerequisites
- `knowledge_manager.py` must be present in the `.agent/skills/deep_research/` directory.
- Python installed.

## Workflow

### Phase 1: Ingest (Gathering Information)
1.  **Search**: Use `search_web` to find high-quality sources (PDFs, Documentation, Articles).
2.  **Read**: Use `read_url_content` (or `browser` tool for complex sites) to get the raw text.
    *   *Tip*: For PDFs, if a direct extraction tool isn't available, rely on text-based web versions or summaries found in search.

### Phase 2: Essence Extraction (Processing)
The goal is to convert raw text into "Atomic Notes".
For each relevant document or section:
1.  **Analyze**: "What is the core concept here? specific tools? definitions?"
2.  **Synthesize**: Write a summary that captures the "essence".
    *   **Format**: Github-flavored Markdown.
    *   **Structure**:
        *   Definition
        *   Key Features
        *   Use Cases
        *   Relationships (Connections to other links).

### Phase 3: Storage (Second Brain)
Use the `knowledge_manager.py` script to save the extracted essence.

**Command:**
```bash
python .agent/skills/deep_research/knowledge_manager.py add --title "Concept Name" --category "concepts" --tags "tag1,tag2" --content "The content of the note..."
```

**Categories Guidelines:**
- `concepts`: Abstract ideas, workflows, theories (e.g., "Deep Research", "Zettelkasten").
- `entities`: People, Organizations, Companies.
- `tools`: Specific software, libraries, models (e.g., "Mistral OCR", "LangChain").
- `journals`: Logs of what you researched and when.

## Example Usage

**User Request**: "Research 'GraphRAG' and save the key points."

**Agent Action 1 (Research)**:
`search_web(query="GraphRAG explained")` -> Returns details about combining Knowledge Graphs with RAG.

**Agent Action 2 (Extract)**:
(Internal Thought): "GraphRAG is a technique that uses knowledge graphs to improve RAG... created by Microsoft..."

**Agent Action 3 (Store)**:
```bash
python .agent/skills/deep_research/knowledge_manager.py add --title "GraphRAG" --category "concepts" --tags "RAG,Knowledge Graph,Microsoft" --content "GraphRAG is a structured approach to Retrieval Augmented Generation..."
```

## Maintenance
- Occasionally run `python .agent/skills/deep_research/knowledge_manager.py init` to ensure the directory structure exists.
