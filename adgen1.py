import os
import sys

from api import GPT, Example, UIConfig
from api import demo_web_app

question_prefix = "Input: "
answer_prefix = "Output: "

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
temperature=0.6,
max_tokens=300,
input_prefix=question_prefix,
output_prefix=answer_prefix,
append_output_prefix_to_query=False)

gpt.add_example(Example("Input: Watch countless movies and TV shows online with Netflix. Subscribe now and get 20% off.", "Output: There are many services available to watch your favorite movies and TV shows, but no other services is as easy to use or smooth as Netflix. Currently, they offer a 20% off discount for new users. Come and enjoy your favorite movies with Netflix!"))
gpt.add_example(Example("Input: Buy our classic Coca-Cola non-alcoholic drinks.", "Output: Spend summer with your favorite Coca-Cola! Enjoy the summer with your family and friends while drinking delicious non-alcoholic beverages from Coca-Cola. Now comes in different flavors. Choose yours!"))
gpt.add_example(Example("Input: Our shop on sale for sneakers.", "Output: For men and women who want the latest trends and hottest fashion sneaker collection has never been easier to shop with. Find the hottest trends in sneakers including the latest releases from famous brands like Nike, Adidas, Converse, and more."))

# Define UI configuration
config = UIConfig(
    description="Use GPT-3 to generate your advertisement quote.",
    button_text="Generate",
    placeholder="Input something about your advertisement or company.",
    show_example_form=True,
)

demo_web_app(gpt, config)
