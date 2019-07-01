class Customer():

    def __init__(self, fname = "", lname = "", address = "", mobile_phone = "", work_phone = "", home_phone = "", home_fax = "", work_fax = "", email = "", house_land_budget = 0, house_only_budget = 0, is_selling_existing = False, land_details = "", notes = ""):
        '''constructor'''
        self.fname = fname
        self.lname = lname
        self.address = address
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.home_phone = home_phone
        self.home_fax = home_fax
        self.work_fax = work_fax
        self.email = email
        self.house_land_budget = house_land_budget
        self.house_only_budget = house_only_budget
        self.is_selling_existing = is_selling_existing
        self.land_details = land_details
        self.notes = notes


    def __str__(self):
        return "Name: {} {} Address: {} Ph(M): {}, Ph(W): {} Ph(H): {} Fax(H): {} Fax(W): {} Email: {} House/Land budget: {} House only budget: {} Selling existing: {} Land details: {} Notes: {}".format(self.fname, self.lname, self.address, self.mobile_phone, self.work_phone, self.home_phone, self.home_fax, self.work_fax, self.email, self.house_land_budget, self.house_only_budget, self.is_selling_existing, self.land_details, self.notes)


    def edit_fname(self, detail):
        self.fname = detail

    def edit_lname(self, detail):
        self.lname = detail

    def edit_address(self, detail):
        self.address = detail

    def edit_mobile_phone(self, detail):
        self.mobile_phone = detail

    def edit_work_phone(self, detail):
        self.work_phone = detail

    def edit_home_phone(self, detail):
        self.home_phone = detail

    def edit_home_fax(self, detail):
        self.home_fax = detail

    def edit_work_fax(self, detail):
        self.work_fax = detail

    def edit_email(self, detail):
        self.email = detail

    def edit_house_land_budget(self, detail):
        self.house_land_budget = detail

    def edit_house_only_budget(self, detail):
        self.house_only_budget = detail

    def edit_is_selling_existing(self, detail):
        self.is_selling_existing = detail

    def edit_land_details(self, detail):
        self.land_details = detail

    def edit_notes(self, detail):
        self.notes = detail