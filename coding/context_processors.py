
from coding.models import Company
def data(request):
    companies = Company.objects.all().order_by('company_name')
    return {"company":companies}