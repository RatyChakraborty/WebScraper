import requests
from bs4 import BeautifulSoup
# url = 'https://www.1mg.com/all-diseases'

def scrape_disease_information(url):
    disease_information = {}
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Scrape disease name
    disease_name = soup.select_one('div.marginTop-16 .flexColumn').text.strip()
    disease_information['Acidity'] = disease_name
    
    # # Scrape Overview
    overview = soup.select_one('#overview').text.strip()
    disease_information['Overview'] = overview
    
    # # Scrape Key facts
    key_facts = soup.select_one('.marginTop-8').text.strip()
    disease_information['Key facts'] = key_facts
    
    # # Scrape Symptoms
    symptoms = soup.select_one('#symptoms').text.strip()
    disease_information['Symptoms'] = symptoms
    
    
    # # Scrape Causes
    causes = soup.select_one('#causes').text.strip()
    disease_information['Causes'] = causes
    
    # # Scrape Types
    # types = soup.select_one('#types').text.strip()
    # disease_information['Types'] = types
    
    # # Scrape Risk Factors
    # risk_factors = soup.select_one('#risk_factors').text.strip()
    # disease_information['Risk Factors'] = risk_factors
    
    # # Scrape Diagnosis
    # diagnosis = soup.select_one('#diagnosis').text.strip()
    # disease_information['Diagnosis'] = diagnosis
    
    # # Scrape Prevention
    # prevention = soup.select_one('#prevention').text.strip()
    # disease_information['Prevention'] = prevention
    
    # # Scrape Specialist to Visit
    specialist_to_visit = soup.select_one('#specialist_to_visit').text.strip()
    disease_information['Specialist to Visit'] = specialist_to_visit
    
    # # Scrape Treatment
    treatment = soup.select_one('#treatment').text.strip()
    disease_information['Treatment'] = treatment
    
    # # Scrape Home-care
    home_care = soup.select_one('#home-care').text.strip()
    disease_information['Home Care'] = home_care

    # # Scrape Complications
    complications = soup.select_one('#complications').text.strip()
    disease_information['Complications'] = complications
    
    # # Scrape Alternatives therapies
    alternative_therapies = soup.select_one('#alternatives_therapies').text.strip()
    disease_information['Alternatives therapies'] = alternative_therapies
    
    # # Scrape Living with
    living_with = soup.select_one('#living_with').text.strip()
    disease_information['Living with'] = living_with

    # # Scrape Living with
    faqs = soup.select_one('#faqs').text.strip()
    disease_information['Frequently Asked Questions'] = faqs
    
    return disease_information

disease_information = scrape_disease_information('https://www.1mg.com/diseases/acidity-42')
print(disease_information)
