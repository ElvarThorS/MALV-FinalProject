import wikipedia
import pandas as pd
import spacy

nlnlp = spacy.load("en_core_web_trf")
import en_core_web_trf
nlp = en_core_web_trf.load()

def fetch_random_articles(n):
    print("Starting to fetch random articles...")
    article_data = []
    count = 0
    attempts = 0
    max_attempts = n * 10  # To prevent infinite loops in case of persistent errors

    while count < n and attempts < max_attempts:
        try:
            pages = wikipedia.random(10)
            for page in pages:
                try:
                    wiki_page = wikipedia.page(page)

                    # Filter out articles that contain people in the summary
                    doc = nlp(wiki_page.summary)
                    entities = [(ent.text, ent.label_) for ent in doc.ents]
                    if any(entity[1] == "PERSON" for entity in entities):
                        continue  # Skip if the summary mentions a person

                    article_data.append({
                        'title': page,
                        'summary': wiki_page.summary,
                        'url': wiki_page.url
                    })
                    count += 1
                    print(f"{page} ({count}/{n}) Type: {wiki_page.categories}")
                except wikipedia.exceptions.DisambiguationError:
                    continue  # Skip to the next page on disambiguation error
                except wikipedia.exceptions.PageError:
                    continue  # Skip to the next page on page not found error
        except wikipedia.exceptions.DisambiguationError:
            continue  # Skip to the next batch on disambiguation error
        except wikipedia.exceptions.PageError:
            continue  # Skip to the next batch on page not found error
        attempts += 1

    if count < n:
        print(f"Warning: Could not fetch {n} valid articles. Only {count} articles were fetched due to persistent errors.")

    print("Finished Fetching articles")
    return article_data

def save_articles_to_file(article_data, filename):
    df = pd.DataFrame(article_data)
    df.to_csv(f"{filename}.csv", index=False)
    print(f"Article data saved to {filename}")

if __name__ == "__main__":
    num_articles = 100
    filename = "random_wikipedia_articles"
    article_data = fetch_random_articles(num_articles)
    save_articles_to_file(article_data, filename)
    print("Done!")
    