from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


# Grab user data to login
user_email = input("What's your email")
user_password = input("What's your password")
# Your Linkedin profile
# url = "http://www.linkedin.com/in/valerie--sharp/"
url = "http://www.linkedin.com/in/feed/"

# Create a new session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)


# View log in form
login_link = driver.find_element_by_link_text("Sign in")
login_link.click()
driver.implicitly_wait(35)
# Login
# email_input = driver.find_element_by_class_name("login-email")
email_input = driver.find_element_by_class_name("login-email")
password_input = driver.find_element_by_class_name("login-password")
login_btn = driver.find_element_by_id("login-submit")

email_input.send_keys(user_email)
password_input.send_keys(user_password)
driver.implicitly_wait(35)
login_btn.click()

# Create CSV files

# skillsFile = open('work_skills.csv', 'wb')
# jobsFile = open('work_jobs.csv', 'wb')
# educationFile = open('work_education.csv', 'wb')

# ON PROFILE PAGE (SCROLL DOWN TO GET FULL VIEW)

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, 2524);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Selenium hands the page source to Beautiful Soup
soup_level = BeautifulSoup(driver.page_source, "lxml")

# find all skills
#   Industry Knowledge
#   Tools & Technologies
#   Interpersonal Skills
#   Other Skills

driver.implicitly_wait(30)

# View all skills
show_more_skills = driver.find_element_by_class_name("pv-skills-section__additional-skills")
show_more_skills.click()

driver.implicitly_wait(30)
skills_div = driver.find_elements_by_class_name("pv-skill-category-list")
# skills_div = soup_level.find_all("div", class_="pv-skill-category-list")
skills = []
print("hey")
#Beautiful Soup finds all Job Title links on the agency page and the loop begins
# for link in soup_level1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):
print(skills_div)
for skill_div in skills_div:
    print(skill_div)
    print("==============")
    # for skill in soup_level1.find_all('ol'):
    #     print(skill)
print(soup_level.title)
driver.quit()
# find all job data
#    company pic
#    job title
#    company
#    start date
#    end date
#    time at job
#    city
#    job description

# education
