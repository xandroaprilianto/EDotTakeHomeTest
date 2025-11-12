import time

from web.common.config.conftest import driver
from web.common.fixtures.authFixture import do_login
from web.pages.companiesLocator.companiesLocator import CompaniesPage
from web.common.fixtures.generalFunction import scroll_to_bottom, scroll_once

def test_success_add_company(driver, do_login):
    company = CompaniesPage(driver)

    do_login()
    company.click_CompaniesMenu()
    company.click_AddCompany()
    company.verify_PageRegisterCompany()
    company.input_CompanyName("Avenger Seven")
    company.input_Email("qatest@mail.com")
    company.input_Phone("81210002000")
    company.select_IndustryType("hospitality")
    company.select_CompanyType("retailer")
    company.select_Language("indonesia")
    company.input_StreetAddress("Jalan jalan keliling indonesia")
    company.select_detail_country(
        country="id",
        province="DI YOGYAKARTA",
        city="KAB BANTUL",
        district="BANGUNTAPAN",
        sub_district="BATURETNO"
    )
    # company.select_detail_country(
    #     country="my",
    #     state="Perak",
    #     city="Batu Gajah",
    #     location="Peti Surat",
    #     postal_code="31007"
    # )
    # company.select_detail_country(
    #     country="ph",
    #     region="Mimaropa Region",
    #     province="Romblon",
    #     city="San Jose",
    #     barangay="Lanas"
    # )
    company.click_Next()
    company.click_Next()
    company.input_BranchName("QA Test Malaysia")
    company.input_StreetAddress("Jalan jalan ke Malaysia")
    company.select_detail_country(
        country="my",
        state="Perak",
        city="Batu Gajah",
        location="Peti Surat",
        postal_code="31007"
    )
    company.click_AgreePolicyAndTNC()
    assert company.isRegisterBTN_Disabled() is True
    company.click_Register()
    time.sleep(20)

def test_verify_success_add_company(driver, do_login, scroll_to_bottom):
    company = CompaniesPage(driver)

    do_login()
    company.click_CompaniesMenu()
    scroll_to_bottom()
    company.click_Manage_Company(company_name="Avenger Seven")
    company.verify_success_open_page_detail_company()
    company.verify_company_details(
        company_name="Avenger Seven",
        industry_type ="Hospitality",
        company_type = "Retailer",
        country = "Indonesia",
        province = "DI YOGYAKARTA",
        city = "KAB BANTUL",
        district = "BANGUNTAPAN",
        sub_district = "BATURETNO",
        email = "qatest@mail.com",
        phone = "81210002000",
        address = "Jalan jalan keliling indonesia"
    )
