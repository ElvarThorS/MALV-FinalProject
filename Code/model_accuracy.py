import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import os

# Define directories
root_dir = "."  # Assuming the script is run from the root directory
predictions_dir = os.path.join(root_dir, "Model and Predictions")

# Function to load CSV file
def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

# Function to calculate metrics
def calculate_metrics(data):
    # Ensure labels are numeric
    data['ner'] = pd.to_numeric(data['ner'])
    data['human'] = pd.to_numeric(data['human'])
    
    # Map numeric labels to IOB tags
    iob_mapping = {0: 'B', 1: 'I', 2: 'O'}
    data['ner_iob'] = data['ner'].map(iob_mapping)
    data['human_iob'] = data['human'].map(iob_mapping)
    
    # Calculate accuracy
    accuracy = accuracy_score(data['human_iob'], data['ner_iob'])
    
    # Classification report
    report = classification_report(data['human_iob'], data['ner_iob'], labels=['B', 'I', 'O'])
    
    # Confusion matrix
    matrix = confusion_matrix(data['human_iob'], data['ner_iob'], labels=['B', 'I', 'O'])
    
    return accuracy, report, matrix

# Function to combine results
def combine_results(file_paths):
    combined_data = pd.DataFrame()
    accuracies = []
    reports = []
    matrices = []
    
    for file_path in file_paths:
        data = load_csv(file_path)
        if data is not None and 'human' in data.columns:
            combined_data = pd.concat([combined_data, data[['ner', 'human']]])
            accuracy, report, matrix = calculate_metrics(data)
            accuracies.append(accuracy)
            reports.append(report)
            matrices.append(matrix)
    
    # Calculate overall accuracy
    if not combined_data.empty:
        overall_accuracy, overall_report, overall_matrix = calculate_metrics(combined_data)
    else:
        overall_accuracy, overall_report, overall_matrix = None, None, None
    
    return {
        'accuracies': accuracies,
        'eports': reports,
        'atrices': matrices,
        'overall_accuracy': overall_accuracy,
        'overall_report': overall_report,
        'overall_matrix': overall_matrix
    }

# Function to plot confusion matrix
def plot_confusion_matrix(matrix, title):
    plt.figure(figsize=(10, 8))
    sns.heatmap(matrix, annot=True, cmap='Blues', fmt='g', xticklabels=['B', 'I', 'O'], yticklabels=['B', 'I', 'O'])
    plt.xlabel('Predicted Labels')
    plt.ylabel('Actual Labels')
    plt.title(title)
    plt.show()

# Main execution
if __name__ == "__main__":
    file_paths = [os.path.join(predictions_dir, file_name) 
                  for file_name in os.listdir(predictions_dir) 
                  if file_name.startswith("historical-event-ner_") and file_name.endswith("_labeled.csv")]
    
    results = combine_results(file_paths)
    
    if results['overall_accuracy']:
        print("Overall Accuracy:", results['overall_accuracy'])
        print("Overall Classification Report:")
        print(results['overall_report'])
        
        # Plot overall confusion matrix
        plot_confusion_matrix(results['overall_matrix'], "Overall Confusion Matrix")
    else:
        print("No files processed.")