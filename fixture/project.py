from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_manage_tab()
        self.open_manage_projects_tab()
        # init project creation
        wd.find_element_by_xpath("//*[@value='Create New Project']").click()
        self.fill_project_info(project)
        # submit project creation
        wd.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[7]/td/input").click()


    def fill_project_info(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        wd.find_element_by_name("view_state").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.view_state)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)

    def open_manage_tab(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[1]/a[7]").click()

    def open_manage_projects_tab(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div[2]/p/span[2]/a").click()
