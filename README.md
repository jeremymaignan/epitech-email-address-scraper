# EPITECH Email Addresses Scraper

### Purpose: 
Script scraping my university intranet to collect the email addresses of current and past students.

### History
I was browsing on the intranet of my university, when I was intrigued by a specific feature. On the profil section you can see a graph containing all students you worked with for at least one project.

First, when you hover over someone's picture, you can see the email address of this student.

Second, when you double click on someone's picture, another graph appears with the students he or she worked with. You can do that without any limit...

I quickly understood that I could easily scrap all email addresses of all students with a Python script.

![Facebook Screenshot](https://github.com/jeremymaignan/epitech-email-addresses-scraper/blob/master/Screenshot%202021-10-18%20at%2014.53.31.png?raw=trueg)


### Steps
1. In the browers, extract the HTTP requests allowing to get all partners of a student and my authentification token. https://intra.epitech.eu/user/{email_address}/binome/
2. Init two lists; `$email_to_process = ["jeremy.maignan@epitech.eu"]` and `$done = []` containing the list of email address processed.
3. Pop an email address from the list `$email_to_process`, send the request with this user and add the email address to the list `$done`.
4. Parse the new email addresses from response of my request, add them all to the list `$email_to_process` (only if not already in the list `$done`).
5. Repeat the process until the list `$email_to_process` is empty.
6. Finaly, export the list of email addresses to a file.

This is how I scraped more than 16k email addresses.
