from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse
from queue import Queue
import json
import csv

class CourseSearcher:
    def __init__(self, index):
        self.index = index

    def search(self, keywords):
        relevant_courses = {}
        for keyword in keywords:
            for course_id in self.index.get(keyword.lower(), []):
                relevant_courses[course_id] = relevant_courses.get(course_id, 0) + 1
        sorted_courses = sorted(relevant_courses.items(), key=lambda x: x[1], reverse=True)
        return [course_id for course_id, relevance in sorted_courses]
