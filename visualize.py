import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    Generates a bar chart showing the frequency of each sentiment 
    (positive, neutral, negative, irrelevant) from the input list and saves it 
    as an image in the 'images/' folder.

    Args:
    sentiments (list): A list of sentiment labels (positive, neutral, negative, irrelevant).

    Returns:
    None
    """
     # Count the occurrences of each sentiment
    positive_count = sentiments.count("positive")
    neutral_count = sentiments.count("neutral")
    negative_count = sentiments.count("negative")
    irrelevant_count = sentiments.count("irrelevant")

    # Prepare the data for plotting
    labels = ["Positive", "Neutral", "Negative", "Irrelevant"]
    counts = [positive_count, neutral_count, negative_count, irrelevant_count]

    # Create the bar plot
    plt.bar(labels, counts, color=['green', 'blue', 'red', 'gray'])

    # Add titles and labels
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiments")
    plt.ylabel("Frequency")

    # Save the plot to the images/ folder
    plt.savefig('images/sentiment_distribution.png')

    # Optionally, display the plot
    plt.show()
