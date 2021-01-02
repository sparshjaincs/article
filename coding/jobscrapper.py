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
    def extract_company_indeed(self,job_elem,loca):
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
            location=loca.capitalize()
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
        link = 'https://www.indeed.co.in' + link
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
    
    
    def extract_salary(self,element):
        try:
            salary = element.find('span',class_="salaryText")
            salary = salary.text.strip()
        except:
            salary = ""
        return salary
    def get_indeed_job_data(self,instance,jobs,location):
        db = list()
        data = instance.find_all('div', class_='jobsearch-SerpJobCard')
        for x in data:
            sol = dict()
            title = self.indeed_title(x)
            company = self.extract_company_indeed(x,location)
            link = self.extract_link_indeed(x)
            date = self.extract_date_indeed(x)
            summary = self.indeed_summary(x)
            req = self.extract_requirement(x)
            salary = self.extract_salary(x)
            sol['title'] = title
            sol['company'] = company
            sol['link'] = link
            sol['date'] = date
            sol['summary'] = summary
            sol['requirement'] = req
            sol['salary'] = salary
            sol['jobs'] = 'Full Time'
            db.append(sol)
        return db
            

        
        
    def find_jobs(self,website,jobs="",location=""):
        if website  == 'Indeed':
            try:
                soup = self.load_indeed(jobs,location)
                information = self.get_indeed_job_data(soup,jobs,location)
            except:
                information = "Data Not Found !!"

            return information


class Company:
    def __init__(self):
        pass
    def load_info(self,company):
        url = f"https://www.indeed.co.in/companies/search?from=discovery-cmp-search&q={company}"
        data = requests.get(url)
        data = data.content
        soup = bs(data,"html.parser")
        job_soup = soup.find(id="cmp-curated")
        return job_soup
    def extract_name(self,ins,company):
        try:
            soup = ins.find('div',class_='cmp-company-tile-blue-name')
            soup = soup.text.strip()
        except:
            soup = company
        return soup
    def extract_logo(self,ins):
        try:
            image = ins.find('div',class_='cmp-company-tile-logo')
            source = [True,image.find('img')['src']]
        except:
            source = [False,'<i class="fa fa-building-o" aria-hidden="true"></i>']
        return source
    def extract_title_info(self,ins):
        db = {}
        try:
            info = ins.find('div',class_="cmp-company-tile-content")
            rating = info.find('span',class_='cmp-value-title')['title']
            addition = info.find('p',class_='cmp-rating-description').text.strip()
            information = info.find_all('div')
            data = ""
            for i in information:
                data+=i.text.strip()+'\n'
            information = data.split("reviews")[-1]
            sd = ""
            for i in range(1,6):
                if i<=round(float(rating)):
                    sd+='<span class="fa fa-star checked"></span>'
                else:
                    sd+='<span class="fa fa-star"></span>'
            stars = sd
                
            
            
            
        except:
            rating = "Not Available"
            addition = "Not Available"
            stars = ""
            information = ""
        db['rating'] = rating
        db['addition'] = addition
        db['stars'] = stars
        db['information'] = information
        return db
        
    def information(self,ins):
        try:
            data = ins.find('div',class_='cmp-company-featured-description').text.strip()
        except:
            data = ""
        return data
    def extract(self,instance,company):
        db = {}
        db['name'] = self.extract_name(instance,company)
        db['logo'] = self.extract_logo(instance)
        db['rating'] = self.extract_title_info(instance)
        db['information'] = self.information(instance)
        
        
        return db
    
        
        
    
        
    def find_information(self,company):
        soup = self.load_info(company)
        info = self.extract(soup,company)
        
        return info
        

class Hiring:
    def __init__(self):
        pass
    
    def instance(self):
        url = "https://www.indeed.co.in/companies?from=gnav-homepage"
        data = requests.get(url)
        content = data.content
        soup = bs(content,'html.parser')
        return soup
    def get_data(self,instance):
        df ={}
        soup = instance.find('div',class_="cmp-PopularCompaniesWidget-companyName")
        img = instance.find('img')
        link = instance.find('a')
        if soup and img:
            df['name'] = soup.text.strip()
            df['logo'] = img['src']
            df['link'] = "https://in.indeed.com"+link['href']+'/jobs'
            
        return df
            
    def getinfo(self):
        soup = self.instance()
        soup = soup.find_all('div',class_="icl-Grid-col")
        
        df = []
        for ins in soup:
            name = self.get_data(ins)
            if name:
                df.append(name)
            
            
        return df
        
    
    def extract(self):
        data = self.getinfo()
        return data
        
            
    
    
        