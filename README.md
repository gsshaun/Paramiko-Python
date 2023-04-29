# Uploading a CSV file via SSH and executing a PHP command

This Python script transfers a local CSV file to a remote server via SSH and executes a PHP command to import the file into a MySQL database using [Paramiko](http://www.paramiko.org/).

## Prerequisites
- Python 3.x
- Paramiko library (`pip install paramiko`)

## Connection Details
The connection details and file paths are defined in a separate file called `connection_details.py`. Make sure to update the values with your own information before running the script.

## Usage
To run the script, navigate to the directory where the script is saved and run the following command:

```python python paramiko_script.py```

If you encounter any issues, make sure to check that the connection details and file paths in `connection_details.py` are correct.
