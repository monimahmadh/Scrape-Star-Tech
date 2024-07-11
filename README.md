# Scrape Star Tech

This project contains a Python script to scrape product information from the Star Tech Ltd website and store the data in a CSV file. The script scrapes product names, images (in base64 format), features, and prices from the Star Tech website, handling pagination to ensure all products are captured.

## Star Tech Ltd

Star Tech Ltd is a leading technology retailer in Bangladesh, providing a wide range of tech products, including laptops, desktops, processors, accessories, and more. They are known for their extensive product selection, competitive pricing, and excellent customer service. The website offers detailed product descriptions, specifications, and prices, making it a valuable resource for tech enthusiasts and consumers looking for the latest technology.

## Features

- Scrapes product names, images, features, and prices from Star Tech Ltd's website.
- Handles pagination to scrape all product pages.
- Saves the scraped data into a CSV file.
- Encodes product images in base64 format.
- Provides an executable version of the script for easy use without requiring Python.

## Prerequisites

- Python 3.x (for running the script directly)
- `requests` library
- `beautifulsoup4` library
- `pandas` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/monimahmadh/Start-Tech-Scrap
    cd scrape_startech
    ```

2. Install the required libraries (if running the script directly):
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Python Script

1. Run the script:
    ```bash
    python scrape_startech.py
    ```

2. Follow the prompts to enter the URL of the Star Tech page you want to scrape and the desired filename for the output CSV file.

### Using the Executable File

1. Download the `scrape_startech.exe` file from the repository.
2. Double-click the executable file to run the script.
3. Follow the prompts to enter the URL of the Star Tech page you want to scrape and the desired filename for the output CSV file.

## Important Notes

- Ensure you have an active internet connection while running the script, as it fetches data from the web.
- The base64 encoding of images can result in large character strings, which might exceed the character limits in some spreadsheet software. Consider alternative methods for storing large base64 strings if necessary.

## Example

```python
Paste URL from Star Tech: https://www.startech.com.bd/laptop-notebook
File name (e.g., laptop_data, intel_processor, etc.): laptop_data
```

The script will save the scraped data in `laptop_data.csv`.
