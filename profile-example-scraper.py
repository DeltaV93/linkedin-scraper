import time
import requests
from bs4 import BeautifulSoup

# Your Linkedin profile
profile_url = "http://www.linkedin.com/in/valerie--sharp/"
# Path to example html file
html_path = "new-linkedin-profile-example.html"
# url = "http://www.linkedin.com/in/feed/"
html_data = open(html_path, encoding="utf8").read()

# Selenium hands the page source to Beautiful Soup
soup = BeautifulSoup(html_data, "lxml")

# SKILLS VARS
skill_div = soup.find_all('div', {'class': ['pv-skill-category-list', 'pv-profile-section__section-info']})
skill_list = soup.find_all('ol', {'class': ['pv-skill-category-list__skills_list', 'list-style-none']})
skills_title = soup.find_all('h3', {'class': 'pb2 t-16 t-black--light t-normal pv-skill-categories-section__secondary-skill-heading'})
skills_name = soup.find_all('span', {'class': 't-16 t-black t-bold'})

# EXPERIENCES DIVS
experiences_div = soup.find_all('div', {'class': 'pv-entity__summary-info pv-entity__summary-info--background-section mb2'})

# PORTFOLIO SUMMARY
summary_p = soup.find('p',{'class': 'pv-top-card-section__summary-text mt4 ember-view'})

# GET PROFILE HEADING
# for job_description_span in job_description:
print("==============================================")
print('====================SUMMARY===================')
print("==============================================")
for summary_spans in summary_p:
    for sentence in summary_spans:
        print(sentence.strip())
print("********************************************************")

# FIND ALL JOB TITLE INFO
print("==============================================")
print('==================Experience==================')
print("==============================================")
for experience_li in experiences_div:

    job_title = experience_li.find_next("h3")
    company_name = experience_li.find_next("span", {"class": "pv-entity__secondary-title"})
    job_date_range = experience_li.find_next("h4", {"class": "pv-entity__date-range"}).find_next("span").find_next("span")
    job_location = experience_li.find_next("h4", {"class": "pv-entity__location"}).find_next("span").find_next("span")
    job_description = experience_li.find_parent("a").find_next_sibling("div", {"class": "pv-entity__extra-details ember-view"}).find("p")
    job_description_msg = ""
    print("----------- COMPANY: ")
    print(company_name.string)
    print("----------- TITLE: ")
    print(job_title.string)
    print("----------- DATE: ")
    print(job_date_range.string)
    print("----------- LOCATION: ")
    print(job_location.string)
    print("----------- DESCRIPTION: ")

    for job_description_span in job_description:
        for word in job_description_span:
            if isinstance(word, str):
                job_description_msg += word
    print(job_description_msg.strip())
    print("********************************************************")

# FIND ALL SKILLS AND SAVE THEM
print("==============================================")
print('====================SKILLS====================')
print("==============================================")
for skill_title in skills_title:
    print(skill_title.text.strip())
    print("=========== ")
    for skill in skills_name:
        print(skill.string.strip())
print("********************************************************")
