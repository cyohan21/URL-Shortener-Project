# Python Library Management Project

## Overview

This application allows users to:

- Shorten a URL  
- Get the Original URL (from a shortened url)
- View All Shortened URLs

## How It Works

When you launch the program, you will see the following prompt:  

> Welcome to the URL Shortener App! Please enter one of the following: :
>> 1: Shorten URL
>> 
>> 2: Get Original URL
>> 
>> 3: View URL Map
>> 
>> 4: Exit

If you enter `1`, the program will prompt you to enter a URL. If the URL already exists, it will return its shortened version.

If you enter `2`, you will be prompted to enter the shortened URL. If it exists, it will return the original URL.
If the book does not exist, an error message will appear.  

If you enter `3`, you will be shown a list of all shortened URLs in pretty-print format.
If the list is empty, the program will return an error message indicating so.

If you enter `4`, the program will close with a farewell message:  

> Goodbye!
