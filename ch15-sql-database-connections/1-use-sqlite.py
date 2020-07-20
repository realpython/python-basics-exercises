# 15.1 - Use SQLite
# Solutions to review exercises

import sqlite3

# Create a temporary database connection in RAM
with sqlite3.connect(":memory:") as connection:
    c = connection.cursor()

    # Exercise 1
    # Create a "Roster" table with Name, Species and Age fields
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, Age INT)")

    # Exercise 2
    # Add some data into the database
    roster_data = (
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29),
    )
    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", roster_data)

    # Exercise 3
    # Update the Name of Jadzia Dax to "Ezri Dax"
    c.execute(
        "UPDATE Roster SET Name=? WHERE Name=?", ("Ezri Dax", "Jadzia Dax")
    )

    # Exercise 4
    # Display the names and ages of everyone classified as Bajoran
    c.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    for row in c.fetchall():
        print(row)
