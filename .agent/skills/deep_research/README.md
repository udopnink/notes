# Deep Research & Knowledge Management for AI Agents

> [!NOTE]
> This document serves as a "Knowledge Base" regarding the capabilities required for an AI agent to perform Deep Research. It demonstrates the "extraction of essence" from various web sources, organized into a structured overview.

## 1. Deep Research Workflows

Deep research differs from simple web search by its iterative, multi-step nature. It involves planning, gathering, analyzing, and synthesizing information over time.

### Core Principles
*   **Multi-Agent Systems**: Break down research into specialized roles:
    *   **Planner**: Decomposes the query into sub-questions.
    *   **Fetcher**: Retrieves raw data (Web Search, PDF download).
    *   **Analyst**: Reads and summarizes individual documents.
    *   **Synthesizer**: Combines findings into a cohesive report.
*   **Iterative Refinement**: The "Planner" should revisit the plan based on initial findings. If a search reveals a new concept, the plan is updated to investigate that concept.
*   **Structured Output**: Agents should communicate via structured schemas (JSON) rather than free text to ensure reliability.

### Recommended "Skills" or Tools
*   **Research Frameworks**:
    *   **Storm**: A research system that simulates a conversation between an agent and a persona to deepen the topic.
    *   **AutoGPT/BabyAGI**: Early examples of autonomous task loops.
    *   **LangGraph**: A library for building stateful, multi-actor applications (ideal for research loops).

## 2. Document Analysis & Essence Extraction

To "dive into a topic," an agent must consume more than just search snippets. It needs to ingest full documents (PDFs, Markdown, Papers).

### PDF & Document Parsing
*   **Mistral OCR**: A powerful tool for extracting text *and* semantic structure (tables, math) from PDFs into Markdown.
*   **Docling**: Open-source framework for deep document understanding, preserving layout and reading order.
*   **Parseur / Unstructured.io**: Tools specifically designed to turn "messy" documents into clean data for LLMs.

### Essence Extraction Techniques
*   **Map-Reduce Summarization**:
    1.  **Map**: Summarize each chunk/page independently (extracting key entities, claims, and data).
    2.  **Reduce**: Combine chunk summaries into a master summary.
*   **Claim Extraction**: Instead of summarizing, specifically extract "Claims" and "Evidence" to build an argument graph.
*   **Recursive Summarization**: For very large corpuses, summarize chapters, then summarize the book from chapter summaries.

## 3. Knowledge Management (The "Second Brain")

How to "keep track and store the essence" for future lookup.

### Storage Architectures
*   **Vector Databases (Semantic Memory)**:
    *   Tools: **Chroma**, **Pinecone**, **Weaviate**.
    *   Usage: Store chunks of text as embeddings. Allows "fuzzy" retrieval (e.g., "Find me concepts related to agent memory" returns results even if exact keywords don't match).
*   **Knowledge Graphs (Structured Memory)**:
    *   Tools: **Neo4j**, **CocoIndex**.
    *   Usage: Store entities (nodes) and relationships (edges). E.g., `(Mistral OCR) --[IS_A]--> (PDF Tool)`. Excellent for connecting disparte facts.
*   **File-Based Systems (Markdown/Obsidian)**:
    *   **Zettelkasten Method**:
        *   **Atomic Notes**: One concept per file.
        *   **Links**: Use `[[WikiLinks]]` to connect notes.
        *   **YAML Frontmatter**: Metadata for the agent (tags, source, date).
    *   **Why**: Human-readable *and* machine-parseable. An agent can "read" your Obsidian vault as a dataset.

### Organization Strategy
A recommended folder structure for an Agent's brain:
```text
/brain
  /inbox        # Raw downloads (PDFs, scraped HTML)
  /processing   # Intermediate summaries
  /concepts     # Atomic notes (The "Essence")
  /entities     # People, Tools, Organizations
  /journals     # Chronological logs of research sessions
```

## 4. Example Workflow: "Agent Skills Research"

Applying these concepts to the user's example request ("collect sources regarding agent skills"):

1.  **Ingest**:
    *   Search query: "Best AI agent skills for research 2025" and "AI knowledge management tools".
    *   Download top 5 relevant PDFs/Pages.
2.  **Process**:
    *   Convert all to Markdown (using Mistral OCR or simple text extraction).
    *   Split into chunks.
3.  **Extract**:
    *   For each chunk, ask LLM: "Extract any defined 'Skill', 'Tool', or 'Framework'. Output as JSON."
4.  **Store**:
    *   Create a file `concepts/Deep_Research_Workflow.md` with the definition.
    *   Create a file `tools/Mistral_OCR.md` with the capabilities.
    *   Link them: "Deep Research Workflow uses [[Mistral_OCR]] for PDF parsing."
5.  **Review**:
    *   The user (or agent) can now browse the connected graph of skills.

## 5. Next Steps

To implement this verification workflow, I can create a custom **Skill** for you.
This skill would be a script or prompt chain that creates this folder structure and automates the "Ingest -> Process -> Store" loop.
