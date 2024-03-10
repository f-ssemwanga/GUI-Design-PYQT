data = [('Avatar', 'Fox', '01 July 2009', '12'),
        ('Spider-Man 3', 'Sonny', '16 April 2007', '12'),
        ('The Dark Knight Rises', 'WB', '12 July 2012', '12'),
        ('The Hobbit', 'WB', '13 December 2013', 'U'),
        ('Harry Potter and the half-blood prince', 'WB', '15 July 2009', 'U'),
        ("Pirates of the Caribbean: Dead Man's Chest", 'BV', '24 June 2006', 'U'),
        ('Shrek 2', 'DW', '19 May 2004', 'U'),
        ("Pirates of the Caribbean: At the World's end", 'BV', '19 May 2007', '12'),
        ('Skyfall', 'WB', '23 October 2012', '12'),
        ('Titanin', 'Fox', '19 December 1997', '12')]
title_data =""
for record in data:
    title_data += str(record[0])+"\n"
    print(title_data)