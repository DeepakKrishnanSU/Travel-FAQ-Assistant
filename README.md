# Travel FAQ Assistant

## Overview
The Travel FAQ Assistant is a lightweight, text-based question answering system designed to provide quick and reliable answers to common travel-related questions. The project focuses on simplicity, clarity, and extensibility, making it suitable as an MVP for a tourism information assistant.

Instead of relying on large external datasets or APIs, the system uses a curated FAQ knowledge base and matches user queries to the most relevant stored questions.

---

## Problem Statement
Travelers often have recurring questions about visas, flights, baggage, accommodation, safety, and general travel practices. Searching for these answers manually can be time-consuming and inconsistent.

This project aims to:
- Provide instant answers to common travel FAQs
- Avoid overengineering for a small-to-medium knowledge base
- Ensure deterministic and reliable responses without hallucinations

---

## Solution Approach
- A text-based FAQ file (`faq.txt`) is used as the knowledge base.
- Each FAQ entry consists of a clear question and answer pair.
- User input is compared against stored questions using similarity matching.
- The most relevant answer is returned to the user.

This approach demonstrates how a simple FAQ assistant can be built without complex infrastructure while remaining effective and easy to maintain.

---

## Project Structure
travel-faq-assistant/
│
├── app.py # Main application logic
├── matcher.py # Question similarity matching logic
├── faq.txt # Travel questions and answers
├── requirements.txt # Dependencies (standard Python only)
└── README.md

---

## How It Works
1. The application loads all questions and answers from `faq.txt`.
2. The user enters a travel-related question.
3. The system compares the input question with stored FAQ questions.
4. The closest matching question is identified.
5. The corresponding answer is displayed to the user.

---

## Features
- Supports a large FAQ knowledge base (500+ questions)
- Easy to extend by adding new Q&A entries
- No external APIs or paid services required
- Deterministic responses (no hallucinations)
- Simple command-line interface

---

## How to Run
1. Clone the repository:
   git clone https://github.com/DeepakKrishnanSU/Travel-FAQ-Assistant.git

2. Navigate to the project directory:
   cd Travel-FAQ-Assistant

3. Run the application:
   python app.py

4. Ask travel-related questions in the terminal.
   Type exit to quit.

## Extensibility
New questions and answers can be added by simply editing faq.txt. No code changes are required, making the system easy to maintain and scale.

## Limitations
- The system relies on text similarity and does not perform deep semantic understanding.
- Answers are limited to the information available in the FAQ file.

## Future Enhancements
- Semantic search using embeddings
- Multilingual question support
- Categorized FAQs (visa, flights, accommodation, etc.)
- Web or mobile interface
- Integration with real-time travel data sources

## Conclusion
This project demonstrates a practical and efficient approach to building a travel FAQ assistant using fundamental programming concepts. It serves as a strong foundation that can be enhanced with advanced techniques in future iterations.

---

### Why this README is good for your internship submission
- Honest about scope
- No overclaiming
- Clean engineering explanation
- Shows you understand **trade-offs**
- Evaluators can clearly see what you built and why

If you want, next I can:
- shorten it (if they prefer concise READMEs)
- tailor it specifically to the **Intel challenge wording**
- add a small **architecture diagram (ASCII)**
