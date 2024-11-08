import requests
from bs4 import BeautifulSoup

def scrape_course_data():
    url = "https://www.analyticsvidhya.com/genaipinnacle"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    courses = soup.find_all("div", class_="course-container")  # Adjust based on actual HTML structure

    course_data = []
    for course in courses:
        title = course.find("h2").text.strip()
        description = course.find("p").text.strip()
        course_data.append({"title": title, "description": description})

    return course_data

if __name__ == "__main__":
    courses = scrape_course_data()
    print(courses)  # Verify that the data is scraped correctly
