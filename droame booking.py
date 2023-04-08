from selenium import webdriver

# Open the browser and navigate to the webpage
driver = webdriver.Chrome()
driver.get("C:\Users\yuvak\OneDrive\Desktop\drome bookings.html")

# Find the add booking button and click it
addBookingBtn = driver.find_element_by_css_selector('#bookings button')
addBookingBtn.click()

# Find all the edit buttons and add event listeners to them
editBtns = driver.find_elements_by_css_selector('button[type="edit"]')
for btn in editBtns:
    btn.click()

# Find all the delete buttons and add event listeners to them
deleteBtns = driver.find_elements_by_css_selector('button[type="delete"]')
for btn in deleteBtns:
    btn.click()

# Find all the navigation links and sections and add event listeners to them
navLinks = driver.find_elements_by_css_selector('nav a')
sections = driver.find_elements_by_css_selector('main section')

for link in navLinks:
    link.click()
    sectionId = link.get_attribute('href')
    sectionToShow = driver.find_element_by_css_selector(sectionId)
    sections = driver.find_elements_by_css_selector('main section')
    for section in sections:
        section.style.display = 'none'
    sectionToShow.style.display = 'block'
