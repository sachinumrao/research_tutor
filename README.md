# Research Tutor

A LLM powered tutor to ask questions from research papers

## Document Processing Flow:

- Pdf -> Pdf parser -> Chunks -> Embedding

### Query Processing Flow:

- Query -> Embedding -> Retrieved Chunks -> Context building for LLM -> LLM -> Response

## Tools:

- Embedding: nomic using sentence transformers
- Vector DB: voyager in memory DB
- LLM: Mistral-instruct v1 / Gemma-2 instruct
- UI: streamlit
- Pdf Parser: pdfplumber
