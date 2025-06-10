# 🕸️ Web Scraping
---

## ✅ Day 1–2: Introduction to Web Scraping

### 🔹 Topics:

- What is web scraping?
- Ethical and Legal Considerations
- Static vs. Dynamic Websites
- How to evaluate `robots.txt` file and their content
- How to check for Sitemap URLs
- Tools & Libraries Overview:
  - `requests`
  - `BeautifulSoup (bs4)`
  - `Selenium` (for browser automation)
  - `Scrapy` (intro only for now)

### 🛠️ Hands-on Tasks:

#### 1. Scrape Headings and Links from a sample HTML page:

- Use `requests` to load a static page.
- Use `BeautifulSoup` to extract all `<h1>`, `<h2>`, and `<a href>` links.

#### 2. Parse Structured Data from a simple blog or news site:

Extract:
- Article titles
- URLs
- Descriptions or image URLs
- Date published

---

## ✅ Day 3–4: Dealing with Real Sites

### 🔹 Topics:

- Inspecting HTML using DevTools
- CSS Selectors vs XPath
- HTTP Methods (GET, POST)
- Headers, Cookies, and Sessions
- Learn about user-agents integration
- Intro to Proxies and their importance for bypassing IP restrictions
- Using `CloudScraper` to bypass bot protections

### 🛠️ Hands-on Tasks:

#### 1. Scrape a Paginated Site (e.g. Books to Scrape)

Extract:
- Book Title
- Price
- Rating
- Availability

Follow pagination links across multiple pages.

#### 2. Submit a Search Form and Extract Results

- Use `requests + bs4` or `Selenium`
- Example: Quotes Search
- Save results in `.json` file
