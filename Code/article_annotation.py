import tkinter as tk
from tkinter import messagebox
import pandas as pd

def load_article_data(filename):
    try:
        df = pd.read_csv(filename)
        return df.to_dict('records')
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except pd.errors.EmptyDataError:
        print(f"File {filename} is empty.")
        return []

def save_annotated_data(annotated_data, output_filename):
    df = pd.DataFrame(annotated_data)
    df.to_csv(output_filename, index=False)
    print(f"Annotated data saved to {output_filename}")

def annotate_articles(article_data, output_filename):
    current_index = 0  # Define current_index here
    current_article = article_data[current_index]
    annotated_data = []

    def save_annotation():
        annotation = label_var.get()
        annotated_data.append({
            'title': current_article['title'],
            'ummary': current_article['summary'],
            'url': current_article['url'],
            'annotation': annotation
        })
        display_next_article()

    def display_next_article():
        nonlocal current_index, current_article, annotated_data  # Declare all nonlocal variables
        if current_index < len(article_data):
            current_index += 1
            current_article = article_data[current_index]
            article_text.delete('1.0', tk.END)
            article_text.insert(tk.END, f"**Title:** {current_article['title']}\n\n**Summary:** {current_article['summary']}\n\n**URL:** {current_article['url']}")
            label_var.set("Not an Event")  # Reset label to default
        else:
            messagebox.showinfo("Completed", "All articles have been annotated.")
            root.destroy()
            save_annotated_data(annotated_data, output_filename)

    root = tk.Tk()
    root.title("Article Annotation Tool")

    current_index = 0
    current_article = article_data[current_index]
    annotated_data = []

    article_text = tk.Text(root, height=20, width=80)
    article_text.pack()
    article_text.insert(tk.END, f"**Title:** {current_article['title']}\n\n**Summary:** {current_article['summary']}\n\n**URL:** {current_article['url']}")

    label_var = tk.StringVar(root)
    label_var.set("Not an Event")
    label_option = tk.OptionMenu(root, label_var, "Event", "Not an Event")
    label_option.pack()

    submit_button = tk.Button(root, text="Submit Annotation", command=save_annotation)
    submit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    filename = input("Enter the CSV file to annotate (e.g., random_wikipedia_articles.csv): ")
    output_filename = f"{filename}_annotated.csv"
    article_data = load_article_data(filename)
    annotate_articles(article_data, output_filename)