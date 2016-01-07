# 13.1 review exercises

import sqlite3

# Create a temporary database connection in RAM
with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()

    # Create a "Roster" table with Name, Species and IQ fields
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")

    # Add some data into the database
    roster_data = (
        ("Jean-Baptiste Zorg", "Human", 122),
        ("Korben Dallas", "Meat Popsicle", 100),
        ("Ak'not", "Mangalore", -5)
    )
    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", roster_data)

    # Update the Species of Korben Dallas to "Human"
    c.execute("UPDATE Roster SET Species=? WHERE Name=?",
              ('Human', 'Korben Dallas'))

    # Display the names and IQs of everyone classified as Human
    c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    for row in c.fetchall():
        print(row)
