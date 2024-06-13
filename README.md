# BANK MANAGER APP
This is a simple command line interface banking application written in Python.
## FEATURES
<ul>
<li>Create a new user account</li>
<li>Check account balance</li>
<li>Deposit money into their account</li>
<li>withdraw money from their account</li>
</ul>

## PREQUISITES
<ol>
<li>Python 3.8 or higher</li>
<li>SQLite3</li>
</ol>

## how to run 
<ol>
<li>Clone the repository from git hub </li>
<li>Open the terminal and navigate to the cloned repository</li>
<li>enter the directory </li>
<li> open your VS code </li>
<li>Run the command `python -m lib.bank_cli`</li>
</ol>

## HOW TO USE
<ol>
<li>When you run the application, you will be presented with a menu to create a new user</li>
<li>Enter your name to create a new user</li>
<li>After creating a new user, you will be presented with a menu to check balance, deposit,withdraw and exit </li>
<li>Enter the corresponding number to perform the desired action</li>
</ol>

## code structure 
<ul>
<li>Bank Database : Stores user data </li>
<li> User :Represents a bank user with attributes and methods for balance operations.</li>
<li>BankCLI: Manages the command line interface and user interactions.</li>
