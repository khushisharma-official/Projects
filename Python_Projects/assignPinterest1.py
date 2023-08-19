from pinscrape import pinscrape
import csv

def remove(string):
    return string.replace(" ", "")

def save_to_csv(image_urls, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Image URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for url in image_urls:
            writer.writerow({'Image URL': url})

input_tags = input("Enter Pinterest tags (comma-separated): ").split(',')

for tag in input_tags:
        tag = remove(tag)
        print(tag)
        details = pinscrape.scraper.scrape(tag, "/images", {}, 10)

print(details)
save_to_csv(details['url_list'], 'pinterest.csv')

# if details["isDownloaded"]:
#     print("\nDownloading completed !!")
#     print(f"\nTotal urls found: {len(details['extracted_urls'])}")
#     print(f"\nTotal images downloaded (including duplicate images): {len(details['url_list'])}")
#     print(details)
# else:
#     print("\nNothing to download !!")