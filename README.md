# PYTHON_MANAGER_PROJECT
The goal of the project is to build a simplified and proof-of-concept software application for managing an electronic table reservation book for a restaurant in the evening of a specific day. The software is composed of a user interface and business logic part written in Python and an SQL database management system to store the data.


##  Application domain model 
We suppose the restaurant has a certain number of tables, numbered sequentially with integers from 1 to 𝑛 (𝑛 ≥ 9). The restaurant manager, which is our software user, can receive table reservation requests and operate on the software in order to update the booking records in the system. A reservation is requested by a guest that tells the manager
- his/her name
- personal phone number
- number of guests for the table
The date and time are unnecessary information since, for sake of simplicity, we are supposing the software manages only one evening. The reservation is accepted if there is a table with the right capacity: among the tables that can accommodate the guests, one with the least number of seats gets actually reserved. The guests are not allowed to book with a name or phone number already existing in the reservations.
The guests can request the cancellation of a reservation by providing name or phone number.

## User interaction
The restaurant manager can interact with the system with regular operations that are
intended to manage guest reservations:
- Record the reservation of a table
- Show a reservation
- Cancel a reservation
- List all the reservations
- List all the unreserved tables
Moreover, the software can fulfill the following simple statistical operations:
- Show the number of reserved tables
- Show the number of tables reserved with a specified number of guests
- Show the number of booked guests overall
- Show the number of unreserved seats overall
- Show the table(s) with the greatest number of unreserved seats
- Show the reserved table(s) with the greatest number of unreserved seats

The program shall show an error (as specified later on) in case any of the operations above cannot be accomplished (e.g. adding an existing reservation, adding a reservation that cannot be accomodated, showing or cancelling a non-existing reservation, …).

## Program specification
The Python program, that communicates wih the DBMS storing the data, shall repeatedly: 
1) output only the prompt character > ("greater than" symbol) in a line, and 
2) wait for a user's command as input, and then 
3) possibly output the corresponding outcome, according to the following specifications:

## Command Syntax Description
1) R g phoneNumber bookingName --> Reserve a table for g guest(s) under the name bookingName with number phoneNumber, choosing one least capacity table as specified above. Assumptions (for sake of simplicity): phoneNumber is a string of decimal digits, bookingName is a single word formed by letters only.
Example commands:
R 3 35452489 Martin
R 5 0214327 Anna

2) S phoneNumberOrBookingName -->Show the information of a certain reservation identified by phoneNumberOrBookingName (that must be a phone number or a booking name), with output in the format: t g s phoneNumber bookingName, where t is the table number, g is the
number of booked guests and s is the total number of seats for the table t.
Example output:
7 3 5 35452489 Martin

3) C phoneNumberOrBookingName -->Cancel a reservation identified by phoneNumberOrBookingName
Example command:
C Anna

4) L --> List all the reservations, one per line complying with the same format as for the S command's output.
Example output:
7 3 5 35452489 Martin
9 5 5 0214327 Anna

5) U -->List all the unreserved tables, one per line complying with the format: t s, where t is the table number and s is the number of seats for the table t.

6) NT Output the number of reserved tables

7) NT g Output the number of tables that have a reservation for g guests each.

8) NG Output the number of booked guests overall

9) NU Output the number of unreserved seats overall

10) GU Show the information about table(s) with the greatest number of unreserved seats, one per line with the format: t g s, where t is the table number, g is the number of booked guests (0 if unreserved) and s is the total number of seats for the table t.
Example output:
2 7 9
7 3 5
8 0 2

11) GR Show the information about reserved table(s) with the greatest number of unreserved seats, one per line. Output similar to GU command, but the field g cannot be 0.

12) X Exit (close) the program
