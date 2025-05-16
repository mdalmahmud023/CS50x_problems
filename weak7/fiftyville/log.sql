-- Keep a log of any SQL queries you execute as you solve the mystery.

-- to see the crime happend on the time and the place. And to get the description.
SELECT * FROM crime_scene_reports WHERE year = 2024 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

-- check interviews of bakery
SELECT * FROM interviews WHERE transcript LIKE '%bakery%';

--ruth: 10 within minutes
-- Eugene: ATM on Leggett Street and saw the thief there withdrawing some money
--Raymond: talked to them for less than a minute &  they were planning to take the earliest flight out of Fiftyville tomorrow.

-- CHECKING bakery sequrity log
SELECT * FROM bakery_security_logs JOIN people ON bakery_security_logs.license_plate = people.license_plate WHERE year = 2024 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25;

-- checking ATM info
SELECT * FROM atm_transactions WHERE atm_location = 'Leggett Street' AND year = 2024 AND month = 7 AND day = 28;

-- checking with name
SELECT name, transaction_type, amount FROM atm_transactions JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number JOIN people ON bank_accounts.person_id = people.id WHERE atm_location = 'Leggett Street' AND year = 2024 AND month = 7 AND day = 28;

-- CHECKING PHONE CALLS
SELECT * FROM phone_calls WHERE year = 2024 AND month = 7 AND day = 28 AND duration < 60;
--checking with names
SELECT name, caller, receiver, duration FROM phone_calls JOIN people on phone_calls.caller = people.phone_number WHERE year = 2024 AND month = 7 AND day = 28 AND duration < 60;

--From 3 witness there are two name common which are Bruce and Diana. So one of them was thief.

--checking the id of the the fiftyville
SELECT * FROM airports;    --8

--checking the flight
SELECT * FROM flights JOIN airports ON flights.destination_airport_id = airports.id  WHERE origin_airport_id = 8 AND year = 2024 AND month = 7 AND day = 29;

-- the thif ESCAPED to New York City. Because it was the earliest flight. FLight id = 36
-- checking the passengers of this two flights
SELECT name FROM people JOIN passengers ON people.passport_number = passengers.passport_number WHERE flight_id = 36 AND people.name IN ('Bruce', 'Diana');

-- Bruce is the thief

--Checking the ACCOMPLICE
SELECT name FROM phone_calls JOIN people ON phone_calls.receiver = people.phone_number WHERE caller =(SELECT phone_number FROM people WHERE name = 'Bruce') AND year = 2024 AND month = 7 AND day = 28 AND duration < 60;
