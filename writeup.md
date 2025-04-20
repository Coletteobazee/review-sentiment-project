## Question 1

What is the most common sentiment observed in your sample of 50 reviews according to your OpenAI labeled data?

[Based on the bar chart, the most common sentiment is Negative, with approximately 27 reviews in this run.
This suggests that a significant portion of customers are dissatisfied with the current version of Zico Coconut Water, citing issues such as a plastic or odd taste, with an unpleasant aftertaste, or concerns about quality and packaging.]

## Question 2

How reliable do you believe these labels are? Look at the respective labels OpenAI has generated for specific reviews, does it seem like the large language model accurately described the user's review? What risk do model hallucinations introduce into this analysis?

[The model is generally reliable and often captures sentiment well, but it’s not perfect. It might misinterpret mixed or nuanced reviews. Also, the model may return slightly different label counts each time it's run.
    
Although the reviews.json file contains 50 reviews, the model returns about 57 sentiment labels. This may be due to how it processes HTML tags like <br /> or line breaks, which could cause it to treat parts of one review as separate entries. Since the output is a list of sentiments with no direct link to each review, it’s difficult to assess label accuracy without checking them line by line.

Model hallucinations can distort the analysis by incorrectly categorizing reviews, leading to flawed conclusions. This can affect decision-making and risk misdirecting efforts to improve the product. For critical use cases, it's best to manually verify a sample of the labels.]

## Question 3

Using the most common sentiment, what would you recommend to this Coconut Water producer to improve customer satisfaction? Should they continue to pursue current market/product outcomes, or does there exist an opportunity for this business to improve its product?

[The most common sentiment in this sample is "Negative", highlighting key issues with Zico Coconut Water’s current product. Many reviews mention a decline in taste and quality, with complaints about the switch to plastic bottles (e.g., “it makes the drink taste like plastic”) and the product now being “from concentrate”. Some customers even suggest Zico should “go back to using fresh juice”.

To improve customer satisfaction, Zico coconut water producer should consider returning to its original Tetra Pak packaging, revising the formula to taste more natural, and being transparent about product changes. These updates could help regain trust and win back disappointed loyal customers and improve overall customer perception. A deeper dive into the individual reviews would likely uncover additional actionable insights to guide their product and customer experience improvements.]
