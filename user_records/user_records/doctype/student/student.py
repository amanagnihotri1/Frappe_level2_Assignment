# Copyright (c) 2024, Aman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime
def create_user_if_not_exists(email):

    if not frappe.db.exists("User", email):
        # Fetch student details
        student = frappe.get_doc("Student", email_address)
        
        # Create a new user document
        new_user = frappe.new_doc("User")
        new_user.first_name = student.first_name
        new_user.last_name = student.last_name
        new_user.email = student.email_address,
        new_user.append("roles", {
            "role": "student"  
        })
        
        # Save the user
        new_user.insert(ignore_permissions=True)  
        
        frappe.msgprint("User created successfully.")
    else:
        frappe.msgprint("User already exists.")
class Student(Document):
    def get_full_name(self):
        full_name_parts = [self.first_name, self.middle_name, self.last_name]
        full_name = " ".join(part for part in full_name_parts if part)
        return full_name
    
    def validate(self):
           birth_date = datetime.datetime.strptime(self.date_of_birth, '%Y-%m-%d')
        if birth_date >= datetime.datetime.now():
            frappe.throw("Date of birth cannot be greater than the current date")
	    if self.start_date and self.end_date:
            # Calculate duration
            duration = self.calculate_duration(self.start_date,self.end_date)
            # Set the duration in the DocType
            self.duration = duration
	def calculate_duration(self, start_date, end_date):
        # Convert string dates to datetime objects
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        # Calculate duration
        duration = end_date - start_date

        # Extract days from the duration
    return duration.days
    def before_save(self):
        self.full_name =f'{self.first_name} {self.middle_name} {self.last_name}'