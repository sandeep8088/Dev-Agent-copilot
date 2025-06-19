Dev Agent Copilot
=================

Dev Agent Copilot is an AI-powered tool designed to streamline software engineering workflows by processing and triaging JIRA tickets. 
It leverages sentence-transformer embeddings for duplicate detection and OpenAI GPT models to rewrite ticket summaries in a more developer-friendly language.

Key Features:
-------------
- Parses and deduplicates JIRA tickets from CSV inputs
- Uses embedding similarity to detect and group redundant issues
- Rewrites and summarizes tickets using GPT
- Outputs a clean, triaged CSV ready for engineering workflows

Ideal For:
----------
- Engineering teams dealing with large volumes of unstructured tickets
- DevOps teams seeking smarter async triage
- Product teams needing better insight into ticket structure

How it Works:
-------------
1. Input: Raw JIRA tickets in CSV format
2. Process:
   - Generate embeddings for all ticket summaries
   - Identify and flag similar or duplicate tickets
   - Rewrite ticket summaries using GPT for clarity and conciseness
3. Output: A clean CSV of triaged, rewritten tickets
