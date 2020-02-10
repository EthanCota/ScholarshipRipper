# ScholarshipRipper
The purpose of the script is to scrape and organize a large amount of scholarships. This script only works with a corresponding text file that contains the correct codes for the scholarships.

I obtained the codes from [The Ultimate Scholarship Book](http://www.ultimatescholarshipbook.com) which I highly recommend purchasing for yourself. The website is also what I am using to get the information.

Here is how the script works as of the most recent committ:
1. Reads *'code.txt'* and its corresponding codes
2. Uses the [Selenium](https://selenium.dev) module to navegate to http://ultimatescholarshipbook.com and enter a code
3. Uses Selenium to store information from the information obtained after entering the code
4. (TODO) Enters information into a Google/Excel Spreadsheet
