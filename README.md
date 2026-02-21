# AURA--AI-based-Universal-Retrieval-Assistant
AI-powered web scraper using Python
This project is an AI-powered web scraper written in Python that combines traditional scraping tools with modern large-language-model (LLM) capabilities to extract structured information from webpages.

🧠 Core Purpose

The main goal of the project is to let a user enter a URL, fetch the page’s content, and then use an AI model to intelligently interpret and extract the information you want from that content — instead of manually writing scraping rules for every website.

🧰 Key Technologies Used

Selenium – Automates a browser to load web pages (including JavaScript-rendered content).

BrightData (optional) – A data proxy/API service to help avoid blocking and gather large amounts of data.

Ollama (or other LLM backends via LangChain) – A local or cloud-based LLM to parse and reason about the scraped page text.

Streamlit (often used in the tutorial) – Creates a simple web UI where users can input URLs and prompts for what data to extract.

📜 How It Works

User Input: The user enters a URL (and optionally some instructions on what data to extract).

Page Fetching: Selenium opens and loads the page so that any dynamic content is fully rendered.

DOM Extraction: HTML content is collected and cleaned up for analysis.

AI Processing: The text content is sent to the LLM with a prompt to extract, summarize, or structure the data (e.g., list prices, titles, specific fields, etc.).

Output: Results are shown back to the user through the UI or saved to files/JSON.

🚀 Project Use Cases

Extract product info (names, prices, descriptions).

Summarize article content.

Turn scraped text into structured data like CSV or JSON.

Build datasets for machine learning.

📌 Why It’s Useful

Unlike a regular scraper that requires you to write CSS/XPath rules manually for each site, this AI scraper lets the model interpret page content in natural language, making it more flexible across varying layouts and designs