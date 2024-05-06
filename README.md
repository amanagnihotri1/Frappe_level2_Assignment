[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# **Frappe Doctype Assignment Level-2**

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [License](#license)
## Introduction 
The Course Doctype is intended to store information about individual courses, including their name, code, credits, academic year, and topics covered.
## Doctype: Programme

The Program doctype stores information about educational programs. It includes the following fields:
- **program_name**: A field to store the name of the program.
- **description**: A text field providing a description of the program.
- **start_date** and **end_date**: Date fields to store the start and end dates of the program.
- **duration**: A field to specify the duration of the program in months.
- **total_credits**: A field to store the total credits associated with the program. It sums up all the credits inside the courses linked to the program.
- **status**: A select field to indicate the status of the program (Planned, Ongoing, Completed).
- **instructor**: A MultiTable link field linking the program to an employee who coordinates it. It filters only those employees with "Instructor" as their type.
- **participants**: A table field to list participants in the program. It includes a subfield "participant" which links to the "Student" doctype. It also includes a button named "preview" to show the participant's profile picture from the user doctype.
- **courses**: A table field to associate courses with the program. Inside this table, there's a subfield "course" which is a link field to the "Course" doctype.

## Doctype: Course

The Course doctype stores information about individual courses. It includes the following fields:
- **Course Name**: A field to store the name of the course.
- **Course Code**: A field to store the unique code assigned to the course.
- **Credits**: A field to store the number of credits associated with the course.
- **Academic Year**: A link field linking to the Academic Year doctype.
- **Topics**: A child table to add topics covered in the course.

## Doctype: Topics

The Topics doctype stores information about topics covered within courses. It includes the following fields:
- **Topic Name**: A field to store the name of the topic.
- **Topic Description**: A text field providing a description of the topic.
## Technologies Used

- Frappe
- Docker


## Prerequisites

Before running this project, ensure you have the following installed:

- #### Docker Desktop (Docker)
    Docker Desktop is a one-click-install application for your Mac, Linux, or Windows environment that lets you build, share, and run containerized applications and microservices.It provides a straightforward GUI (Graphical User Interface) that lets you manage your containers, applications, and images directly from your machine. Docker Desktop reduces the time spent on complex setups so you can focus on writing code. It takes care of port mappings, file system concerns, and other default settings, and is regularly updated with bug fixes and security updates.To Install Docker Desktop <a href="https://docs.docker.com/desktop/" alt="not found">Click Here</a>

- #### Frappe
    Frappe, pronounced fra-pay, is a full stack, batteries-included, web framework written in Python and Javascript with MariaDB as the database. It is the framework which powers ERPNext, is pretty generic and can be used to build database driven apps. To install latest version <a href="https://frappeframework.com/docs/user/en/introduction" alt="not found">Click Here</a>


## Installation
1. Install Docker desktop and open command prompt.
2. Inside command promt type this command
   ```bash
   docker pull ubuntu:22.04
   docker run -dt --name bench -p 8000:8000 ubuntu:22.04 /bin/bash
   ```
4. Next setup frappe framework, to setup <a href="https://wiki.nestorbird.com/wiki/install-frappe-v15">Click here</a>
5. Navigate to **Customization > DocType**
6. Create new DocTypes.
7. Add the specified fields according to the provided instructions.
## Usage
1. open bench directory and inside that enable developer mode -
 ```bash
bench set-config -g developer_mode 1
  ```
2. start postgres service by running this command
   ```bash
   sudo service postgresql start
   ```
3. Start Bench with 2 commands
   ```bash
   bench use your_bench_name
   bench start
   ``` 
4. Access the "Student" module from the main menu.
5. Create new student records by filling in the required fields.
6. Optionally, utilize the "Create User" button to generate corresponding system users.
7. Save the record to store the student information in the database.


## Authors

- [@amanagnihotri1](https://www.github.com/amanagnihotri1)

