# EPITECH Email Address Scraper

### Purpose: 
Scrape my university's intranet in order to collect the email addresses of past and current students.

### History
I was browsing my university's intranet, when I became intrigued by a specific feature. On the profile section you can see a graph containing all of the students you have worked with for at least one project.

Firstly, when you hover over someone's picture, you can see their email address.

Secondly, when you double click on someone's picture, another graph appears with the students they have worked with. You can do that without any limit.

I quickly understood that I could easily scrape all email addresses of all students with a Python script.

![Facebook Screenshot](https://github.com/jeremymaignan/epitech-email-addresses-scraper/blob/master/Screenshot%202021-10-18%20at%2014.53.31.png?raw=trueg)


### Steps
1. In the brower, with the console, extract the HTTP requests allowing to get all partners of one student and my authentication token. https://intra.epitech.eu/user/{email_address}/binome/
2. Initialize two lists; `$email_to_process = ["jeremy.maignan@epitech.eu"]` and `$done = []` containing the list of email addresses processed.
3. Pop an email address from the list `$email_to_process`, send the request with this user and add the email address to the list `$done`.
4. Parse the new email addresses from response of the request, add them all to the list `$email_to_process` (only if not already in the list `$done`).
5. Repeat the process until the list `$email_to_process` is empty.
6. Finally, export the list of email addresses to a file.

This is how I scraped more than 16.000 email addresses.
