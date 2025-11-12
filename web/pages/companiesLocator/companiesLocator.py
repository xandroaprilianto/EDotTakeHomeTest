from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ..base_page import BasePage

class CompaniesPage(BasePage):
    CompaniesMenu_BTN = (By.XPATH, "//a[normalize-space()='Companies' or normalize-space()='Perusahaan']")
    AddCompany_BTN =(By.XPATH, "//button[normalize-space()='+ Add Company' or normalize-space()='+ Tambahkan Perusahaan']")
    GreetingsRegisterCompany_TXTTitle = (By.XPATH, "//span[contains(.,'Register Company') or contains(.,'Daftarkan Perusahaan')]")
    CompanyName_TXTField = (By.XPATH, "//input[@placeholder='Input Company Name' or @placeholder='Masukkan Nama perusahaan']")
    Email_TXTField = (By.XPATH, "//input[@placeholder='Input Email' or @placeholder='Masukkan Email']")
    Phone_TXTField = (By.XPATH, "//input[@placeholder='Input Phone' or @placeholder='Masukkan Telepon' or @placeholder='Masukkan Ponsel']")
    IndustryType_ComboBox = (By.XPATH, "//button[normalize-space()='Choose Industry Type' or normalize-space()='Pilih Jenis Industri']")
    CompanyType_ComboBox = (By.XPATH, "//button[normalize-space()='Choose Company Type' or normalize-space()='Pilih Jenis Perusahaan']")
    Language_ComboBox = (By.XPATH, "//button[normalize-space()='Choose Language' or normalize-space()='Pilih Bahasa']")
    StreetAddress_TXTField = (By.XPATH, "//input[@placeholder='Input Address' or @placeholder='Masukkan Alamat' or @placeholder='Masukkan Alamat Perusahaan']")
    Country_ComboBox = (By.XPATH, "//button[normalize-space()='Choose Country' or normalize-space()='Pilih Negara']")

    # General Combobox When Select Country
    Province_ComboBox = (By.XPATH, "//button[normalize-space()='Choose Province' or normalize-space()='Pilih Propinsi']")
    City_ComboBox = (By.XPATH, "//button[normalize-space()='Choose City' or normalize-space()='Pilih Kota']")
    District_ComboBox = (By.XPATH, "//button[normalize-space()='Choose District' or normalize-space()='Pilih Kecamatan']")
    SubDistrict_ComboBox = (By.XPATH, "//button[normalize-space()='Choose Sub District' or normalize-space()='Pilih Sub Diskrit']")
    PostalCode_ComboBox = (By.XPATH, "//button[normalize-space()='Choose Postal Code' or normalize-space()='Pilih Kode Pos']")

    # Special Combobox When Select Country Philippines
    Region_ComboBox = (By.XPATH, "//button[normalize-space()='Choose Region' or normalize-space()='Pilih Wilayah']")
    Barangay_ComboBox = (By.XPATH, "//button[normalize-space()='Choose Barangay' or normalize-space()='Pilih Barangay']")

    # Special Combobox When Select Country Malaysia
    State_ComboBox = (By.XPATH, "//button[normalize-space()='Choose State' or normalize-space()='Pilih State']")
    Location_ComboBox = (By.XPATH, "//button[normalize-space()='Choose Location' or normalize-space()='Pilih Lokasi']")

    SearchComboBox = (By.XPATH, "//input[@placeholder='Search' or @placeholder='Cari']")

    Next_BTN = (By.XPATH, "//button[normalize-space()='Next' or normalize-space()='Selanjutnya']")
    Back_BTN = (By.XPATH, "//button[normalize-space()='Back' or normalize-space()='Kembali']")

    AddDocumentHukum_BTN = (By.XPATH, "//button[normalize-space()='+ Add Document']")

    BranchName_TXTField = (By.XPATH, "//input[@placeholder='Enter Branch Name' or @placeholder='Masukkan Nama Cabang']")
    InputSameDataFromCompanyNote_BTN = (By.XPATH, "//button[contains(text(),'Isikan dengan data yang sama dari catatan Perusahaan' or contains(text(),'Fill data same as company note')]")

    AgreePolicyAndTNC_CHECKBox = (By.XPATH, "//button[@id='select-all']")

    Register_BTN = (By.XPATH, "//button[normalize-space()='Daftar' or normalize-space()='Register']")

    # Company Detail
    Page_Detail_GetTXT = (By.XPATH, "//h3[normalize-space()='Detail Perusahaan']")
    CompanyName_Detail_GetTXT = (By.XPATH, "//span[normalize-space(text())='Nama perusahaan' or normalize-space(text())='Company Name']/following-sibling::div//input")
    IndustryType_Detail_GetTXT = (By.XPATH, "//span[normalize-space(text())='Jenis Industri' or normalize-space(text())='Industry Type']/following-sibling::button/span")
    CompanyType_Detail_GetTXT = (By.XPATH, "//span[normalize-space(text())='Jenis Perusahaan' or normalize-space(text())='Company Type']/following-sibling::button/span")
    Country_Detail_GetTXT = (By.XPATH, "//span[normalize-space(text())='Negara' or normalize-space(text())='Country']/following-sibling::button/span")
    Province_Detail_GetTXT = (By.XPATH, "//span[normalize-space(text())='Propinsi' or normalize-space(text())='Province']/following-sibling::div/button/span")
    City_Detail_GetTXT = (By.XPATH, "//span[normalize-space(text())='Kota' or normalize-space(text())='City']/following-sibling::div/button/span")
    District_Detail_GetTXT = (By.XPATH, "//span[normalize-space(text())='Kecamatan' or normalize-space(text())='District']/following-sibling::div/button/span")
    SubDistrict_Detail_GetTXT = (By.XPATH, "//span[normalize-space(text())='Kelurahan' or normalize-space(text())='Sub-District']/following-sibling::div/button/span")
    Email_Detail_GetTXT = (By.XPATH, "//span[normalize-space(text())='Email']/following-sibling::div//input")
    NoPonsel_Detail_GetTXT = (By.XPATH, "//span[normalize-space(text())='Nomor Ponsel' or normalize-space(text())='Phone Number']/following-sibling::div//input")
    CompanyAdress_Detail_GetTXT = (By.XPATH, "//span[normalize-space(text())='Alamat Perusahaan' or normalize-space(text())='Company Address']/following-sibling::textarea")

    def combo_value_general(self, value):
        self.find((By.XPATH, f"//div[@id='list-combobox']//div[@data-value='{value}']")).click()

    def combo_value_country_detail(self, value):
        self.find((By.XPATH, f"//div[@cmdk-item and normalize-space(text())='{value}']")).click()

    def click_CompaniesMenu(self):
        self.find(self.CompaniesMenu_BTN).click()

    def click_AddCompany(self):
        self.find(self.AddCompany_BTN).click()

    def verify_PageRegisterCompany(self):
        return self.find(self.GreetingsRegisterCompany_TXTTitle).is_displayed()

    def input_CompanyName(self, text):
        self.type(self.CompanyName_TXTField, text)

    def input_Email(self, text):
        self.type(self.Email_TXTField, text)

    def input_Phone(self, text):
        self.type(self.Phone_TXTField, text)

    def select_IndustryType(self, text):
        self.find(self.IndustryType_ComboBox).click()
        self.combo_value_general(text)

    def select_CompanyType(self, text):
        self.find(self.CompanyType_ComboBox).click()
        self.combo_value_general(text)

    def select_Language(self, text):
        self.find(self.Language_ComboBox).click()
        self.combo_value_general(text)

    def input_StreetAddress(self, text):
        self.type(self.StreetAddress_TXTField, text)

    def select_Country(self, text):
        self.find(self.Country_ComboBox).click()
        self.combo_value_general(text)

    def select_detail_country(self, country, **kwargs):
        country = country.lower()

        self.select_Country(country)

        # Mapping struktur administrasi tiap negara
        country_fields = {
            "id": ["province", "city", "district", "sub_district"],
            "my": ["state", "city", "location", "postal_code"],
            "ph": ["region", "province", "city", "barangay", "sub_district"]
        }

        # Validasi jika negara tidak dikenal
        if country not in country_fields:
            raise ValueError(f"Country '{country}' is not supported.")

        # Mapping combo box locator berdasarkan field
        field_locators = {
            "province": self.Province_ComboBox,
            "city": self.City_ComboBox,
            "district": self.District_ComboBox,
            "sub_district": self.SubDistrict_ComboBox,
            "state": self.State_ComboBox,
            "location": self.Location_ComboBox,
            "postal_code": self.PostalCode_ComboBox,
            "region": self.Region_ComboBox,
            "barangay": self.Barangay_ComboBox
        }

        # Ambil daftar field yang sesuai negara
        fields = country_fields[country]

        # Klik setiap combo box berdasarkan field yang tersedia di kwargs
        for field in fields:
            value = kwargs.get(field)
            if not value:
                print(f"Skipping {field}, not provided in kwargs")
                continue

            print(f"Selecting {field}: {value}")

            # Klik combo box sesuai field
            if field in field_locators:
                self.find(field_locators[field]).click()
                self.type(self.SearchComboBox, value)
                self.combo_value_country_detail(value)
            else:
                print(f"Warning: No locator defined for field '{field}'")

    def click_Next(self):
        self.find(self.Next_BTN).click()

    def input_BranchName(self, text):
        self.type(self.BranchName_TXTField, text)

    def click_AgreePolicyAndTNC(self):
        self.find(self.AgreePolicyAndTNC_CHECKBox).click()

    def isRegisterBTN_Disabled(self):
        return self.find(self.Register_BTN).is_enabled()

    def click_Register(self):
        self.find(self.Register_BTN).click()

    def get_manage_button_locator(self, company_name):
        return (
            By.XPATH,
            f"//div[contains(@class,'bg-card')]"
            f"[.//div[contains(@class,'font-bold') and normalize-space(text())='{company_name}']]"
            f"//button[normalize-space()='Mengelola' or normalize-space()='Manage']"
        )

    def click_Manage_Company(self, company_name):
        locator = self.get_manage_button_locator(company_name)
        self.find(locator).click()

    def verify_success_open_page_detail_company(self):
        return self.find(self.Page_Detail_GetTXT).is_displayed()

    def get_element_text(self, locator):
        elem = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        return elem.text.strip()

    def get_input_value(self, locator):
        try:
            elem = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
            # Ambil value menggunakan JS langsung untuk input disabled
            value = self.driver.execute_script("return arguments[0].value;", elem)
            return value.strip() if value else ""
        except Exception as e:
            print(f"⚠️ Gagal ambil input value: {locator} - {e}")
            return ""

    def get_detail_company(self):
        return {
            "company_name": self.get_input_value(self.CompanyName_Detail_GetTXT),
            "industry_type": self.get_element_text(self.IndustryType_Detail_GetTXT),
            "company_type": self.get_element_text(self.CompanyType_Detail_GetTXT),
            "country": self.get_element_text(self.Country_Detail_GetTXT),
            "province": self.get_element_text(self.Province_Detail_GetTXT),
            "city": self.get_element_text(self.City_Detail_GetTXT),
            "district": self.get_element_text(self.District_Detail_GetTXT),
            "sub_district": self.get_element_text(self.SubDistrict_Detail_GetTXT),
            "email": self.get_input_value(self.Email_Detail_GetTXT),
            "phone": self.get_input_value(self.NoPonsel_Detail_GetTXT),
            "address": self.get_input_value(self.CompanyAdress_Detail_GetTXT),
        }

    def verify_company_details(
            self,
            company_name,
            industry_type,
            company_type,
            country,
            province,
            city,
            district,
            sub_district,
            email,
            phone,
            address
    ):
        actual = self.get_detail_company()

        expected = {
            "company_name": company_name,
            "industry_type": industry_type,
            "company_type": company_type,
            "country": country,
            "province": province,
            "city": city,
            "district": district,
            "sub_district": sub_district,
            "email": email,
            "phone": phone,
            "address": address,
        }

        # Loop untuk verifikasi detail satu per satu
        for i, (key, expected_value) in enumerate(expected.items(), start=1):
            # Scroll sekali di tengah proses untuk memastikan elemen bawah terlihat
            if i == len(expected) // 2:
                self.driver.execute_script("window.scrollBy(0, 200);")  # scroll kecil ke bawah

            actual_value = actual.get(key)
            assert actual_value == expected_value, (
                f"❌ Mismatch pada '{key}': "
                f"Expected '{expected_value}', Got '{actual_value}'"
            )

        print("✅ Semua detail perusahaan sesuai!")




