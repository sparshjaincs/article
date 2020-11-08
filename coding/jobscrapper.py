import requests
from bs4 import BeautifulSoup as bs


class Scrapper:
    def __init__(self):
        pass
    
    def load_indeed(self,jobs,location):
        url = f"https://www.indeed.co.in/jobs?q={jobs}&l={location}"
        data = requests.get(url)
        data = data.content
        soup = bs(data,"html.parser")
        job_soup = soup.find(id="resultsCol")
        return job_soup
    def indeed_title(self,element):
        try:
            title_elem = element.find('h2', class_='title')
            title = title_elem.text.strip()
        except:
            title = ""
        return title
    def indeed_summary(self,element):
        try:
            summary = element.find('div',class_ = 'summary')
            summary = summary.text
        except:
            summary = ""
        return summary
    def extract_company_indeed(self,job_elem):
        db = {}
        try:
            company_elem = job_elem.find('div', class_='sjcl')
            company_data = company_elem.find('span',class_ = 'company')
            company = company_data.text.strip()
        except:
            company = ""
            
        try:
            location_data = company_elem.find('span',class_ = 'location')
            location = location_data.text.strip()
        except:
            location=""
        #remote_data = company_elem.find('span',class_ = 'remote')
        #remote = remote_data.text.strip()
        #req_data = company_elem.find('div',class_='summary')
        #req = req_data.text.strip()
        
        
        db['company'] = company
        db['location'] = location
        #db['requirement'] = req_data
        #db['method'] = remote
        return db

    def extract_link_indeed(self,job_elem):
        link = job_elem.find('a')['href']
        link = 'https://www.Indeed.co.uk/' + link
        return link
    def extract_requirement(self,element):
        #req_elem = element.find('div', class_='jobCardReqContainer')
        try:
            data = element.find('div',class_ = 'jobCardReqList')
            sol = ""
            for i in data.find_all('div',class_='jobCardReqItem'):
                sol += i.text.strip() + '\n'
            
        except:
            sol = ""
        #req = req_elem.text.strip()
        return sol
    def extract_date_indeed(self,job_elem):
        try:
            date_elem = job_elem.find('span', class_='date')
            date = date_elem.text.strip()
        except:
            date=""
        return date
    
        
    def get_indeed_job_data(self,instance):
        db = list()
        data = instance.find_all('div', class_='jobsearch-SerpJobCard')
        for x in data:
            sol = dict()
        
            title = self.indeed_title(x)
            company = self.extract_company_indeed(x)
            link = self.extract_link_indeed(x)
            date = self.extract_date_indeed(x)
            summary = self.indeed_summary(x)
            req = self.extract_requirement(x)
            
            sol['title'] = title
            sol['company'] = company
            sol['link'] = link
            sol['date'] = date
            sol['summary'] = summary
            sol['requirement'] = req
            db.append(sol)
        return db
            

        
        
    def find_jobs(self,website,jobs,location):
        if website  == 'Indeed':
            soup = self.load_indeed(jobs,location)
            information = self.get_indeed_job_data(soup)
            return information
            
    
    
        