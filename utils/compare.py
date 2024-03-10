from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse
from queue import Queue
import json
import csv

class CourseComparator:
    def __init__(self, index):
        self.index = index

    def compare(self, course1_id, course2_id):
        course1_words = set(self.index.get(course1_id, []))
        course2_words = set(self.index.get(course2_id, []))
        common_words = course1_words.intersection(course2_words)
        
        # Verificar si hay palabras comunes
        if not common_words:
            return 0.0
        
        # Calcular la similitud evitando la división por cero
        similarity = len(common_words) / (len(course1_words) + len(course2_words) - len(common_words))
        return similarity