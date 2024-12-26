# Virtual-Memory-System-
This project simulates three different page replacement algorithms: FIFO (Fist In First Out), LRU (Least Recently Used), and Optimal. The simulation helps in understanding how these algorithms manage memory and handle page faultes.

## Table of contents
-[Introduction](#introduction)
-[Features](#features)
-[Installation](#installation)
-[Usage](#usage)
-[Example](#example)
-[Contributing](#contributing)
-[License](#license)

##Introduction
Memory management is a crucial aspect of operating systems. Page replacment algorithms are used to decide which memory pages to swap out when a page fault occurs. This project demonstrates the implementation and simulation of three common replacement algorithms.

##Features
-Simulates FIFO, LRU, and Optimal page replacement algorithms.
-Calculates and displays the number of page faultes.
-Shows the state of memory and page table after esch page request.

##Installation
Torun this project, ensure you have Python installedon your system. You can download from [python.org](https://www.python.org/downloads/).

Clone this repository:
```bash
git clone https://github.com/ayoushka/Virtual-Memory-System-.git
cd Virtual-Memory-System-

##Usage
```bash
python BOsQ2-2.py

##Example
Enter the size of phisical memory (in KB): 16
Enter the size of a page (in KB): 4
Enter the sequance of page requests (comma-seperated): 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Choose the page replacement algorithm (FIFO, LRU, Optimal): FIFO

##Contributing
Feel free to open issues or submit pull requests.

##License
This project is licensed under the MIT License. See the LICENSE file for more details.
Feel free to customize this README file according to your project's specific details and requirements
