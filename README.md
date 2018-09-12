# Windows 10 Install

- Download AnacondaPython
- Install with optional ✓ path
- "Anaconda Navigator" → new environment → "ScrapyEnv"
- Save
- Open Anaconda Command Prompt
- `activate ScrapyEnv`
- `"cd [project_path]/[project]/spiders"`
- `scrapy crawl toscrape-css -o quotes.csv`

# QuotesBot
This is a Scrapy project to scrape quotes from famous people from http://quotes.toscrape.com ([github repo](https://github.com/scrapinghub/spidyquotes)).

This project is only meant for educational purposes.

Quotes does not drill into additional pages


## Extracted data

This project extracts quotes, combined with the respective author names and tags.
The extracted data looks like this sample:

    {
        'author': 'Douglas Adams',
        'text': '“I may not have gone where I intended to go, but I think I ...”',
        'tags': ['life', 'navigation']
    }


## Spiders

This project contains two spiders and you can list them using the `list`
command:

    $ scrapy list
    toscrape-css
    toscrape-xpath

Both spiders extract the same data from the same website, but `toscrape-css`
employs CSS selectors, while `toscrape-xpath` employs XPath expressions.

You can learn more about the spiders by going through the
[Scrapy Tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html).


## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl toscrape-css

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl toscrape-css -o quotes.json

If you want to save scraped data to a csv file, use the following:
    
    $ scrapy crawl toscrape-css -o quotes.csv