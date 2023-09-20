# UCPH Finansering 1 Exam Search Tool

A search utility to easily find similar exam questions from previous years for the UCPH course "Finansering 1" (Fin1).

## Introduction

This tool provides an interface to search through past exam documents to find relevant and similar questions. Whether you're preparing for your Fin1 exam or simply want to revisit previous year's content, this tool offers a convenient way to do so.

## Setup

### Prerequisites

Ensure you have `chromadb` installed. You can install it via pip:

```bash
pip install chromadb
```

### Clone the Repository

```bash
git clone https://github.com/yourusername/yourrepositoryname.git
cd yourrepositoryname
```

*Replace `yourusername` and `yourrepositoryname` with your actual GitHub username and the repository's name.*

## Usage

Run the script using the following command:

```bash
python search_tool.py "search_string" --n_results=number_of_results
```

- **search_string**: The string or phrase you want to search for in the exam database.
- **number_of_results** (Optional): The number of search results you want to retrieve. Default is 5.

### Example:

```bash
python search_tool.py "capital structure" --n_results=3
```

This will search for the term "capital structure" and display the top 3 relevant exam questions.

## Output

For each result, the following details will be displayed:

1. **Opgave**: The assignment name.
2. **Delopgave**: The task number within the assignment.
3. **Tekst**: The content/text of the exam question.

## Contribute

Feel free to fork this project, submit pull requests, or report issues.

---

Remember to replace placeholders like `yourusername` and `yourrepositoryname` with your actual GitHub details. Adjust as needed based on your project's structure and features.