# Copyright (c) 2024, Aman and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
import re
@frappe.whitelist()
def total_credits(courses):

	# Get all course names
	courses = re.findall(r'"courses":"([^"]+)"', courses)
	credits = 0
	for course in courses:
		doc = frappe.get_doc('Course', course_name)
		credits += doc.credits
		"""
		Calculate and return total credits
		"""
	return str(credits)
def fetch_student_image(student_name):
         = frappe.get_doc("Student", student_name)
return student_doc.student_image
class Programme(Document):
    pass
