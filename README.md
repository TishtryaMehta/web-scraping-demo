# Web Scraping Demo

A beginner-friendly quick demo on web scraping using Python, featuring a practical example that scrapes company data from Wikipedia. This demo aims to help newcomers understand the basics of web scraping through a real-world application.

## Overview

This repository serves as a tutorial for web scraping fundamentals, demonstrating:
- How to fetch HTML content from websites
- Parse HTML tables using BeautifulSoup
- Convert web data into structured formats
- Handle and clean scraped data
- Save results to CSV files


## Prerequisites

- Python 3.7
- Basic understanding of HTML structure
- Required Python packages:
  - numpy
  - pandas
  - beautifulsoup4
  - requests

## Installation

1. Install required packages:
```bash
pip install numpy pandas beautifulsoup4 requests
```

## Project Structure

```
├── wikipedia_test.py     # Example scraping script
└── wikipedia_test.csv    # Sample output data
```

## Understanding the Code

The example script (`wikipedia_test.py`) is thoroughly commented to explain each step of the web scraping process:

1. **Setting up the request:**
   - How to specify the target URL
   - Making HTTP requests safely

2. **Parsing HTML:**
   - Using BeautifulSoup to parse HTML content
   - Locating specific elements in the page structure
   - Understanding HTML tables and their components

3. **Data Extraction:**
   - Finding and selecting specific HTML elements
   - Extracting text from elements
   - Cleaning extracted data

4. **Data Processing:**
   - Converting scraped data to pandas DataFrames
   - Basic data cleaning techniques
   - Saving results to CSV

## Adapting for Your Own Projects

To modify this script for other websites:

1. Change the target URL:
```python
url = "your_target_website_url"
```

2. Identify the correct HTML elements:
   - Use browser developer tools to inspect your target website
   - Modify the BeautifulSoup selectors accordingly
   - Adjust the data processing to match your needs

## Best Practices

- Always check a website's terms of service. Many wesbites prohibit webscraping. 

## Acknowledgments

- This entire demo is heavily based on a tutorial by [Alex The Analyst](https://www.youtube.com/watch?v=8dTpNajxaH0)
- Base code adapted from [Alex's GitHub Repository](https://github.com/AlexTheAnalyst/PythonYouTubeSeries)
