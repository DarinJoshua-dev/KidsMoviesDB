import sqlite3

# Create a Database instance using connection and cursor

connection = sqlite3.connect('movies_sqlite.db')

cursor = connection.cursor()

# Create a TABLE movies that stores values

command="""CREATE TABLE IF NOT EXISTS movies(m_id INTEGER PRIMARY KEY, name TEXT, actor TEXT, actress TEXT, director TEXT, year of release INTEGER)"""

cursor.execute(command)

# Insert the data to the TABLE

cursor.execute("INSERT INTO movies VALUES(1, 'The Lion King' , 'Roger Allers' , 'Matthew Broderick' , 'Moira Kelly' , '1994' )")
cursor.execute("INSERT INTO movies VALUES(2, 'Lady and the Tramp' , 'Wilfred Jackson' , 'Larry Roberts' , 'Barbara Luddy' , '1955' )")
cursor.execute("INSERT INTO movies VALUES(3, 'Babys Day Out' , 'Patrick Read Johnson' , 'Adam Robert Worton' , 'Lara Flynn Boyle' , '1994' )")
cursor.execute("INSERT INTO movies VALUES(4, 'Charlie and the Chocolate Factory' , 'Tim Burton' , 'Freddie Highmore' , 'Helena Bonham Carter' , '2005' )")
cursor.execute("INSERT INTO movies VALUES(5, 'Ratatouille' , 'Brad Bird' , 'Patton Oswalt' , 'Janeane Garofalo' , '2007' )")
cursor.execute("INSERT INTO movies VALUES(6, 'The Incredibles' , 'Brad Bird' , 'Craig T. Nelson' , 'Holly Hunter' , '2004' )")
cursor.execute("INSERT INTO movies VALUES(7, 'Coco' , 'Lee Unkrich' , 'Anthony Gonzalez' , 'Alanna Ubach' , '2017' )")
cursor.execute("INSERT INTO movies VALUES(8, 'Toy Story' , 'John Lasseter' , 'Tom Hanks' , 'Annie Potts' , '1995' )")
cursor.execute("INSERT INTO movies VALUES(9, 'Kung Fu Panda' , 'Mark Osborne' , 'Jack Black' , 'Angelina Jolie' , '2008' )")
cursor.execute("INSERT INTO movies VALUES(10, '101 Dalmations' , 'Stephen Herek' , 'Jeff Daniels' , 'Glenn Close' , '1996' )")
cursor.execute("INSERT INTO movies VALUES(11, 'A Bugs Life' , 'John Lasseter' , 'Dave Foley' , 'Hayden Panettiere' , '1998' )")
cursor.execute("INSERT INTO movies VALUES(12, 'Finding Nemo' , 'Andrew Stanton' , 'Albert Brooks' , 'Ellen DeGeneres' , '2003' )")
cursor.execute("INSERT INTO movies VALUES(13, 'Big Hero 6' , 'Don Hall' , 'Ryan Potter' , 'Jamie Chung' , '2014' )")
cursor.execute("INSERT INTO movies VALUES(14, 'Monsters Inc' , 'Pete Docter' , 'John Goodman' , 'Jennifer Tilly' , '2001' )")
cursor.execute("INSERT INTO movies VALUES(15, 'Onward' , 'Dan Scanlon' , 'Tom Holland' , 'Julia Louis-Dreyfus' , '2020' )")
cursor.execute("INSERT INTO movies VALUES(16, 'Inside Out' , 'Pete Docter' , 'Richard Kind' , 'Amy Poehler' , '2015' )")
cursor.execute("INSERT INTO movies VALUES(17, 'Frozen' , ' Jennifer Lee' , 'Kristen Bell' , 'Jonathan Groff' , '2001' )")
cursor.execute("INSERT INTO movies VALUES(18, 'Jurassic Park' , 'Steven Spielberg' , 'Sam Neill' , 'Laura Dern' , '1993' )")
cursor.execute("INSERT INTO movies VALUES(19, 'Dr. Dolittle' , 'Betty Thomas' , 'Eddie Murphy' , 'Kristen Wilson ' , '1998' )")
cursor.execute("INSERT INTO movies VALUES(20, 'Home Alone' , 'Chris Columbus' , 'Macaulay Culkin' , 'Catherine O Hara ' , '2001' )")


# Retrieve the results

cursor.execute("SELECT * FROM movies")

results1 = cursor.fetchall()

print(results1)

cursor.execute("SELECT name FROM movies WHERE actor ='Brad Bird'")

results2 = cursor.fetchall()

print(results2)

# Commit changes 
connection.commit()

# Close database connection
connection.close()