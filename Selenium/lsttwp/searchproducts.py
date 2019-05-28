# PRE: pip install selenium
# In your virtualenv.
from selenium import webdriver

# The above is just the WebDriver API.
# PRE: You also need the specific driver for Firefox.  It's the Gecko driver.
# Make sure you use the 64-bit driver for 64-bit Firefox.
# PRE: You need to add the location of that driver to your PATH.
# If using virtualenv, set this up in <env>/bin/activate.bat.

# Create a new Firefox session.
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# Go to the webapp home page.
driver.get("http://demo-store.seleniumacademy.com/")

# Find the search field (by HTML name attribute).
search_field = driver.find_element_by_name("q")

# Enter a search query and submit.
search_field.clear()
search_field.send_keys("phones")
search_field.submit()

# Get all the anchor elements.
products = driver.find_elements_by_xpath("//h2[@class='product-name']/a")

# List the products we found.
print("Found " + str(len(products)) + " products: ")
for product in products:
    print(product.text)

# Quit Firefox.
driver.quit()

