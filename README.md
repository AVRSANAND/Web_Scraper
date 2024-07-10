# Web Scraper

This Python project scrapes event data from a specified URL and stores the data in a file. If new events are found, it sends an email notification.

## Files

- `main.py`: Main script to scrape data, process it, and send notifications.
- `data.txt`: Stores the extracted event data.

## Requirements

- `requests`
- `selectorlib`
- `smtplib`
- `ssl`

You can install the required packages using:

```bash
pip install requests selectorlib
```

## Usage

1. **Configuration**: Ensure your `extract.yaml` file is properly configured to extract the necessary data from the scraped page.
2. **Email Setup**: Update the email settings in the `send_email` function in `main.py` with your own email credentials.

## Running the Script

To run the script, execute:

```bash
python main.py
```

The script will:

1. Scrape the webpage specified by the URL.
2. Extract event data.
3. Store the extracted data in `data.txt`.
4. Send an email notification if new events are found.

The script runs in an infinite loop, checking for new events every 2 seconds.

## Sample Data

Example entries in `data.txt`:

```
Lions of the IDE, Clone City, 6.5.2088
Feng Suave, Minimalia City, 5.5.2089
```

