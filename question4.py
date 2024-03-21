import re

text = '<div><span class="actionBar__text"> Showing 18 of 101 products.</span></div>'
total_products_match = re.search(r'Showing \d+ of (\d+)', text)
if total_products_match:
    total_products = total_products_match.group(1)
    print(total_products)
else:
    print("Total number of products not found.")
