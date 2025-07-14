from src.auth.factory import authenticate_system
from selenium import webdriver
from src.pages.gsolution.gsolution_data import GsolutionData

driver = webdriver.Chrome()
config = authenticate_system("gsolution", driver)
gsolution = GsolutionData(config=config, driver=driver)
data = gsolution.extrair_dados_GS()
print(data)
input('==FIM==')