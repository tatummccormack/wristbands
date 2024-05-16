
import os
import json
from random import choice, randint
from datetime import datetime
from flask import Flask

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()


user = crud.create_user("Noah", "Davis", "noah_davis", "noah@test.com", "no")
model.db.session.add(user)
model.db.session.commit()

user2 = crud.create_user("Ava", "Smith", "ava_smith", "ava@test.com", "yes")
model.db.session.add(user2)
model.db.session.commit()

user3 = crud.create_user("Isabella", "Miller", "isabella_miller", "isabella@test.com", "maybe")
model.db.session.add(user3)
model.db.session.commit()

user4 = crud.create_user("Emma", "Williams", "emma_williams", "emma@test.com", "rah")
model.db.session.add(user4)
model.db.session.commit()

user5 = crud.create_user("Liam", "Colt", "liam_colt", "liam@test.com", "ahhhh")
model.db.session.add(user5)
model.db.session.commit()



festivals = [
    ("Austin City Limits", "Austin, TX", datetime(2024, 10, 4), datetime(2024, 10, 13), [
        "Dua Lipa", "Tyler, The Creator", "Chris Stapleton", "Blink-182", "Sturgill Simpson", 
        "Pretty Lights", "Khruangbin", "Leon Bridges", "Carin León", "Norah Jones", "Renée Rapp", 
        "Foster the People", "Kehlani", "Teddy Swims", "Benson Boone", "Caamp", "Dominic Fike", 
        "The Marías", "Jungle", "Dom Dolla", "Chappell Roan", "Porter Robinson", "The Red Clay Strays", 
        "Orville Peck", "Still Woozy", "Vince Staples", "Cannons", "Remi Wolf", "Something Corporate",
        "Jeezy", "San Holo", "Kevin Abstract", "Stephen Sanchez", "Elderbrook", "Tyla", "Jess Glynne", 
        "Catfish and the Bottlemen", "Hermanos Gutiérrez", "That Mexican OT", "Barry Can’t Swim", 
        "Santigold", "Qveen Herby", "Medium Build", "Kenny Beats", "The Beaches", "Flipturn", 
        "David Shaw", "Movements", "Royal Otis", "Wave to Earth", "Connor Price", "Malcolm Todd", 
        "Flo Milli", "Bakar", "Spinall", "Eggy", "Say She She", "Misterwives", "Eydress", "Eliyna", 
        "Geese", "Grand Funk Railroad", "Miko Marks", "Mickey Guyton", "Petey", "Dasha", "Mannequin Pussy", 
        "Penny & Sparrow", "Chance Peña", "Sir Chloe", "Dexter and the Moonrocks", "The Paper Kites", 
        "Glass Beams", "Balthvs", "Dustin Kensrue", "Valencia Grace", "Lola Young", "Joe P", "Myles Smith", 
        "IDKHOW", "Jonah Kagen", "Jordy", "Bob Schneider", "Three Sinseers", "Emei", 
        "Kalu & the Electric Joint", "The DropTines", "Tyler Halverson", "Mon Rovîa", "The Criticals", 
        "Braxton Keith", "Sawyer Hill", "Jon Muq", "DAIISTAR", "Rickshaw Billie's Burger Patrol", 
        "Telescreens", "Late Night Drive Home", "Theo Lawrence", "Chief Cleopatra", "Western Youth", 
        "Promqueen", "Dead Dead Midnight Navy", "Cale Tyson", "Godly the Ruler", "Molecular Steve", 
        "The Tiarras", "Zach Person", "Marley Bleu", "Obed Padilla", "Deyay", "Almira Flexfly", 
        "The Levites", "The Moranians", "The Huston-Tillotson University Jazz Elite", 
        "Lucy Kalantari & the Jazz Cats", "Uncle Jumbo", "Brother's", "Homescool", "Miss Tutti & Fruity Band", 
        "Anthony & Polly", "School of Rock", "The Barton Hills Choir"
    ],  "/static/festhead/ACLhead.png", "/static/festlineup/ACLlineup.jpg"),

    ("Bonnaroo", "Manchester, TN", datetime(2024, 6, 13), datetime(2024, 6, 16), [
        "Pretty Lights", "FISHER", "BigXthaPlug", "Disco Lines", "Durand Bernarr", 
        "Eggy", "Geese", "Gwar", "The Heavy Heavy", "HoneyLuv", "it’s murph", 
        "Matt Maltese", "Medium Build", "Michigander", "Militarie Gun", 
        "Nation of Language", "Neal Francis’ Francis Comes Alive", "Ocie Elliott", 
        "Oliver Heldens", "Róisín Murphy", "Say She She", "Sid Sriram", "Post Malone", 
        "Maggie Rogers", "Khruangbin", "Seven Lions", "Joe Russo’s Almost Dead", 
        "Dominic Fike", "Lizzy McAlpine", "Interpol", "T-Pain", "Svdden Death", 
        "TV Girl", "Gary Clark Jr.", "The Mars Volta", "Faye Webster", "Key Glock", 
        "Thundercat", "Lovejoy", "ISOxo", "GROUPLOVE", "David Kushner", "The Japanese House", 
        "Dr. Fresch", "49 Winchester", "MIKE.", "Larkin Poe", "Shy FX", "Bonny Light Horseman", 
        "Baby Queen", "Mdou Moctar", "Jessica Audiffred", "Half Moon Run", "Hamdi", "LYNY", 
        "Red Hot Chili Peppers", "Cage The Elephant", "Melanie Martinez", "Cigarettes After Sex", 
        "Diplo", "Jon Batiste", "Reneé Rapp", "Parcels", "IDLES", "Brittany Howard", "Sean Paul", 
        "Knock2", "Ethel Cain", "Gregory Alan Isakov", "The Teskey Brothers", "BADBADNOTGOOD", 
        "Teezo Touchdown", "Whyte Fang", "Bakar", "d4vd", "The Maine", "Josiah and the Bonnevilles", 
        "Kasablanca", "NEIL FRANCES", "Tanner Usrey", "Ryan Beatty", "MIKE", "Trousdale", "Vandelux", 
        "LOVRA", "Once More With Feeling(s) – The Dashboard Confessional Emo SuperJam", "Fred again..", 
        "Megan Thee Stallion", "Jason Isbell and the 400 Unit", "Two Friends", "Carly Rae Jepsen", 
        "Joey Bada$$", "Goth Babe", "Galantis", "Taking Back Sunday", "Ashnikko", "Four Tet", 
        "Charles Wesley Godwin", "Milky Chance", "Chappell Roan", "Greensky Bluegrass", 
        "The Garden", "Yves Tumor", "The Beaches", "Jake Wesley Rogers", "S.G. Goodman", 
        "Libianca", "TSHA", "Irreversible Entanglements", "Armand Hammer", "veggi"
    ], "/static/festhead/bonnaroohead.jpeg", "/static/festlineup/bonnaroolineup.png"),

    ("Coachella", "Indio, CA", datetime(2025, 4, 12), datetime(2025, 4, 14), [ 
        "Lana Del Rey", "Peso Pluma", "Lil Uzi Vert", "Justice", "Bizzarrap", "Deftones", 
        "ATEEZ", "Everything Always", "Peggy Gou", "Young Miko", "Sabrina Carpenter", "Anti Up", 
        "Steve Angello", "Ken Carson", "Skepta", "Faye Webster", "Tyla", "Yaeji", "Yoasobi", 
        "Cloonee", "Gorgon City", "Tinashe", "ANOTR", "L'Impératrice", "Suki Waterhouse", 
        "Lovejoy", "Brittany Howard", "Chappell Roan", "Chlöe", "the Japanese House", 
        "Black Country, New Road", "Café Tacvba", "BLOND:ISH", "the Beths", "NEIL FRANCES", 
        "Clown Core", "Mall Grab", "Kevin de Vries x Kölsch", "Kokoroko", "EarthEater", 
        "Narrow Head", "Skin On Skin", "Ineabelle", "Late Night Drive Home", "Sid Sriram", 
        "Gimafunk", "Miss Monique", "Son Rompe Pera", "Ben Sterling", "Uppblåst", "Keyspan", 
        "Tyler, The Creator", "Blur", "Ice Spice", "Gesaffelstein", "Sublime", "Jungle", 
        "Dom Dolla", "Bleachers", "Grimes", "Jon Batiste", "LE SSERAFIM", "Charlotte de Witte", 
        "ISOxo x Knock2", "Santa Fe Klan", "Blxst", "Purple Disco Machine", "the Drums", 
        "Skream & Benga", "Destroy Lonely", "DITD", "Kevin Abstract", "the Aquadolls", "Kevin Kaarl", 
        "RAYE", "the Red Pears", "Flo", "Blessed Madonna", "Hatsune Miku", "SPINALL", "Peace", 
        "the Adicts", "Oneohtrix Point Never", "Young Fathers", "Kenya Grace", "Patrick Mason", 
        "Dinner Party", "Yaeji", "Natalia Lafourcade", "Lil Mariko", "Boys Noize", "Channel Tres", 
        "Elderbrook", "Saint Levant", "Mahmut Orhan", "Amex x Marcel Dettmann", "Brutalismus 3000", 
        "Erica de Casier", "Girl Ultra", "Maz", "Dende", "Aztec Sonora", "Will Clarke", 
        "Militarie Gun", "Rebek", "Indana", "Kimonos", "Doja Cat", "J Balvin", "Jhené Aiko", 
        "Khruangbin", "Carin León", "Anymma", "John Summit", "Lil Yachty", "DJ Snake", "LUDMILLA", 
        "ROSÉ", "AP Dhillon", "Renée Rapp", "Beabadoobee", "Coi Leray", "NAV", "Tems", "BICEP", 
        "Victoria Monét", "Taking Back Sunday", "88RISING FUTURES", "ARTBAT", "Atarashii Gakko!", 
        "Boy Harsher", "Barry Can't Swim", "Olivia Dean", "LATIN MAFIA", "Two Shell", 
        "Hermanos Gutiérrez", "Follakzoid", "Jackstrap", "Carlita", "Mtoto", "Eddie Zuko", 
        "Adam Ten x Mita Gami", "YG Marley", "Eli F", "Flight Facilities", "DJ Seinfeld", "Tia Lua", 
        "Bb trickz", "Feeble Little Horse", "JOPLYN", "jujujuju", "No Doubt"
    ],  "/static/festhead/coachhead.jpeg", "/static/festlineup/coachlineup.jpeg"),

    ("EDC", "Las Vegas, NV", datetime(2025, 5, 17), datetime(2025, 5, 19), [ 
        "Adam Beyer", "Adventure Club", "Alchimyst", "Andrew Rayel", "Andruss", "Armin van Buuren", 
        "Audiofreq", "Before Dawn", "Blastoyz", "Brina Knauss", "Carl Cox Invites", 
        "Carl Cox B2B Nicole Moudaber", "Casmalia", "Chelina Manuhutu", "Clawz B2B Domah", 
        "Cristoph", "Dabin", "David Guetta", "Deadly Guns", "Deavault", "Eazybaked", "Elif", 
        "Enzo Muro", "EXZ", "Fellsius", "FuntCase B2B Cookie Monsta", "Gian Varela", "GNDR", 
        "Gravedgr", "Hard Driver", "Hixxy", "Hool", "Ilenium", "Infekted Mushroom", 
        "Jessica Audiffred", "John Summit", "Jūsto", "Justin Mylo", "K?D", "Kasablanca", 
        "Kayzo", "Kream", "Lil Texas", "Liquid Stranger", "Lione", "Lost Frequencies", "Lufthaus", 
        "Malice", "Marshmello", "Mau P", "Michael Sparks", "Morten", "Mritwoah", "Notlo", 
        "OMNOM", "Peekaboo", "Ray Volpe", "Reaper", "Reinier Zonneveld", "RemK", "RL Grime", 
        "Saka", "Seth Troxler", "Seven Lions", "Sub Focus", "Subtronics", "Sudden Death", 
        "Sullivan King", "Svdden Death", "Tchami", "Thys", "Tiësto", "Trivecta", "Tweekacore", 
        "Valentino Khan", "Virtual Riot", "Vini Vici", "Walker & Royce", "Warface", 
        "Wasted Penguinz", "Whipped Cream", "Will Clarke", "Wooli", "Wuki", "Yotto", "Zomboy", 
        "ACRAZE B2B Kream", "Adrenalize B2B Wasted Penguinz", "Airwolf Paradise", "Alison Wonderland", 
        "Aly & Fila", "Andrew Bayer", "ATMOZfears", "BEK", "Ben Hemsley", "Ben Sterling", 
        "Benny Benassi", "BIJOU", "Boombox Cartel", "Boys Noize", "Bryan Kearney", "Camo & Krooked", 
        "Chase & Status", "Chris Lake", "Diesel", "Dillon Francis", "DJ Diesel", "DJ Snake", 
        "Dom Dolla", "Effin", "Fallen With MO DINO", "Ferry Corsten", "Four Tet", "GRAVEDGR", 
        "Hannah Laing", "Hedex", "Interplanetary Criminal", "Jamie Jones", "John Fleming", 
        "JOOLSGA", "Joseph Capriati", "Joyhauser", "Justin Mylo", "Krewella", "Kyle Walker", 
        "Lil Texas", "Metrik", "MK", "MK b2b Dom Dolla", "NERVO", "Odd Mob", "Peekaboo", "Pendulum", 
        "Ray Volpe", "Reaper", "Raveboy", "Skazi", "SLANDER", "SLIPPY", "SLUMBERJACK", "Soren", 
        "Sub Focus", "Subtronics B2B 1991", "Sullivan King", "Swedish House Mafia", "Will Clarke", 
        "Wooli", "Zomboy", "Abana B2B Del-Z-Elation", "Adam X", "Alesso", "Angerfist", "Argy", 
        "ATLiens", "Azzeca", "Calussa", "Camelphat", "Chris Lake", "Cosmic Gate", "Deadmau5", 
        "Diplo", "DJ Hanzel", "Eptic", "Funtcase", "Headhunterz", "Kai Wachi", "Kasablanca", 
        "Kayzo", "Krewella", "Lione", "Madeon", "Mau P", "Notlo", "Oliver Heldens", "Omnom", 
        "Pegboard Nerds", "Porter Robinson", "Rezz", "Sam Paganini", "Sasha", "Seth Troxler", 
        "Seven Lions", "Subtronics B2B Dimension", "Sullivan King B2B Ghastly", "The Martinez Brothers", 
        "Timmy Trumpet", "Wasted Penguinz", "Whipped Cream", "Wuki", "Zomboy", "YOU"
    ],  "/static/festhead/EDChead.jpeg", "/static/festlineup/EDClineup.jpeg"),

    ("Governor's Ball", "New York City, NY", datetime(2025, 6, 7), datetime(2025, 6, 9), [
        "Post Malone", "Rauw Alejandro", "Dominic Fike", "Labrinth", "Farruko", "Alex G", "Goth Babe", 
        "Yung Gravy", "Teezo Touchdown", "Qveen Herby", "FLO", "Ryan Beatty", "Mimi Webb", "Arcy Drive", 
        "Blondshell", "Durry", "underscores", "Donna Missal", "Lauran Hibberd", "Alex Chapman", 
        "School of Rock Queens", "The Killers", "21 Savage", "Carly Rae Jepsen", "Sabrina Carpenter", 
        "Sexy Red", "TV Girl", "Jessie Murph", "Doechii", "Hippo Campus", "Pharomony", "d4vd", "Bakar", 
        "Quarters of Change", "Claire Rosinkranz", "Riovaz", "Skizzy Mars", "Telescreens", "The Thing", 
        "Little Stranger", "Maz & Kidd Revel", "Kids Rock for Kids", "SZA", "Peso Pluma", "Renée Rapp", 
        "Don Toliver", "Victoria Monét", "Faye Webster", "Kevin Abstract", "Cannons", "Chappell Roan", 
        "Stephen Sanchez", "Beach Fossils", "Saint Levant", "Elyanna", "Geese", "G Flip", "Baby Queen", 
        "Husbands", "Flukers", "Hotline TNT", "The Hails", "School of Rock Brooklyn"
    ],  "/static/festhead/govballhead.jpeg", "/static/festlineup/govballlineup.png"),

    ("Hard Summer", "Inglewood, CA ", datetime(2025, 8, 3), datetime(2025, 8, 4), [
        "Disclosure", "Rezzmau5", "Jamie XX", "Zeds Dead", "Cloonee", "Mochakk", "Skepta", "Channel Tres", 
        "Wax Motif", "Boys Noize", "Sidepiece", "Sub Focus", "Dimension", "Seth Troxler B2B DJ Tennis", 
        "Chris Stussy", "Hamdi", "San Pacho", "Interplanetary Criminal", "Ketboi69 (Kettama B2B PartiBoi69)", 
        "Chloé Caillet", "Ranger Trucco", "AYYBO", "BUNT.", "Reaper", "Infekt", "INVT", "33 Below", 
        "Saka B2B Fly", "Oppidan", "Carola", "Cole Knight", "Bianca Oblivion", "Notion", "Pocket", 
        "Lake Hills", "Hayes Bradley", "NazaAR", "Beme", "Nelly Furtado", "Fisher", "Chris Lake", "Major Lazer", 
        "Subtronics", "Tchami B2B Malaa", "Sofi Tukker (DJ Set)", "Kenny Beats", "Eli Brown", "Dillon Francis", 
        "Matroda", "Elderbrook", "TroyBoi", "ARMNHMR", "Hedex", "Overmono", "Jyoty", "DJ Heartstring", 
        "Kerri Chandler", "Juelz", "Beltran B2B Classmatic", "Honeyluv B2B Bontan", "Kanine", "Level Up", 
        "Levity", "Sosa", "DJ Susan", "Alleycvtt", "Ahadadream", "Panteros666", "Camden Cox", "Guddeffa", 
        "Mary Droppinz", "Curra", "Teko", "Lupa", "Chase & Status"
    ],  "/static/festhead/hardhead.jpeg", "/static/festlineup/hardlineup.jpeg"),

    ("Life Is Beautiful", "Las Vegas, NV", datetime(2024, 9, 20), datetime(2024, 9, 22), [
        "The Killers", "Flume", "Yeah Yeah Yeahs", "BLXST", "Bebe Rexha", "Vintage Culture", "Dayglow", 
        "Goth Babe", "Cloonee", "Inhaler", "The Wombats", "Raye", "Franc Moody", "Anna Lunoe", 
        "Beach Weather", "Slayyyter", "William Black", "Roosevelt", "Mindchatter", "Telivkast", 
        "Almost Monday", "Ewan McVicar", "Lewis Thompson", "Snacktime", "Dance System", "Kendrick Lamar", 
        "The 1975", "Omar Apollo", "Madeon", "Ferg", "Cigarettes After Sex", "Purple Disco Machine", 
        "Yung Gravy", "Renée Rapp", "Ben Böhmer", "Amber Mark", "The Rose", "Blond:ish", "TSHA", "CHIKA", 
        "JAWNY", "Barry Can't Swim", "Jockstrap", "Vandelux", "Charlotte Sands", "Honeyluv", 
        "Joy Anonymous", "Coco & Breezy", "AYYBO", "Night Tales", "Prentiss", "Odesza", "Khalid", 
        "Nelly", "Kim Petras", "John Summit", "Rina Sawayama", "Claptone", "Cannons", "Baby Tate", 
        "Snakehips", "Jessie Murph", "Babytori", "J. Worra", "Wilderado", "Biig Piig", "Miya Folick", 
        "Talk", "Two Another", "Salute", "Winston Surfshirt", "Highway", "Rockie Brown", "Lema", "The Emo Night Tour"
    ], "/static/festhead/lifehead.jpeg", "/static/festlineup/lifelineup.jpeg"),

    ("Lollapalooza", "Las Vegas, NV", datetime(2024, 9, 20), datetime(2024, 9, 22), [
        "Tyler, The Creator", "Hozier", "Lizzy McAlpine", "Fisher", "Labrinth", "Benson Boone", "Jungle", 
        "Kesha", "Mochakk", "Chappell Roan", "Don Diablo", "d4vd", "Walker & Royce", "Tyla", "Dadi Freyr", 
        "The Japanese House", "Kasbo", "FLO", "Olivia Dean", "Sam Barber", "BigXthaPlug", "Elyanna", 
        "Saint Levant", "Gioli & Assia", "Matt Hansen", "Binkoyak", "SPINALL", "Brenn!", "Quannnic", 
        "Brandi Cyrus", "Riovaz", "Worry Club", "Mette", "Been Stellar", "Abby Holliday", "Camden Cox", 
        "Change Emerson", "Adan Diaz", "Wolves of Glendale", "Walter the Producer", "Goldie Boutilier", 
        "SZA", "Stray Kids", "Laufey with Chicago Philharmonic", "Renée Rapp", "Zedd", "Faye Webster", 
        "Victoria Monét", "Sexy Red", "Galantis", "Loud Luxury", "Kevin Abstract", "Raye", "Megan Moroney", 
        "Ruel", "ALOK", "Qveen Herby", "Veeze", "IN THIS MOMENT", "Noizu", "Wilderado", "Ryan Beatty", 
        "Malcolm Todd", "Lola Young", "Militarie Gun", "it's murph", "Geese", "Blu DeTiger", "WISP", "Wyah", 
        "PawPaw Rod", "Tiny Habits", "The National Parks", "Winnetka Bowling League", "Godly the Ruler", 
        "Tommy Lefroy", "Nightly", "AVA Maybee", "McKenna Grace", "Cale Tyson", "Kalii", "fifteenofeight", 
        "Brandi Cyrus", "The Killers", "Future x Metro Boomin", "Deftones", "Tate McRae", "IVE", "Killer Mike", 
        "TV Girl", "Hippo Campus", "Four Tet", "Ethel Cain", "Skream & Benga", "Cannons", "Kenny Beats", 
        "Briston Maroney", "BoyWithUke", "Romy", "YOASOBI", "Josiah and the Bonnevilles", "Destroy Boys", 
        "Leisure", "Eyedress", "Dozar Jar", "Nia Archives", "Jyoty", "Tanner Usrey", "Friko", "Quarters of Change", 
        "Armani White", "Natalie Jane", "Happy Landing", "Nightly", "Dasha", "Ahadadream", "Brigitte Calls Me Baby", 
        "Infinity Song", "Sam Nelson", "Will Linley", "Hayes Warner", "Tommy Newport", "Savannah Ré", "XANDRA", 
        "Blink-182", "Melanie Martinez", "Conan Gray", "Dominic Fike", "Zeds Dead", "Pierce the Veil", 
        "Teddy Swims", "Two Door Cinema Club", "Vince Staples", "Black Tiger Sex Machine", "White Fang", 
        "Sir Chloe", "Ben Böhmer", "Teezo Touchdown", "The Last Dinner Party", "Waterparks", "Marsev", 
        "Cults", "Grentperez", "GOOD KID", "Hōlō", "Fridayy", "Slow Pulp", "Medium Build", "Mimi Webb", 
        "Knox", "Briscoe", "Treaty Oak Revival", "Jessica Audiffred", "Nico Vega", "Willis", "Hanable", 
        "Post Sex Nachos", "Nostalgia", "Valencia Grace", "Scarlet Demore", "Eddie", "Violett Light", 
        "KOAN Sound", "Bino Rideaux", "Caitlyn Butts", "Ryan Trey", "Huddy", "Carmen DeLeon", "Chicago Made", "Skrillex"
    ], "/static/festhead/Lollahead.jpeg", "/static/festlineup/lollalineup.jpg"),

    ("Outside Lands", "San Francisco, CA", datetime(2024, 9, 9), datetime(2024, 9, 11), [
        "Tyler, The Creator", "The Killers", "Sturgill Simpson", "The Postal Service", "Grace Jones", 
        "Kaytranada", "Jungle", "Chris Lake", "Gryffin", "Snoh Aalegra", "Young the Giant", "Schoolboy Q", 
        "Teddy Swims", "Renée Rapp", "Victoria Monét", "Knock2", "Slowdive", "Killer Mike", "Fletcher", 
        "TV Girl", "Tyla", "Chappell Roan", "Channel Tres", "Charley Crockett", "Men I Trust", "Ben Howard", 
        "Amyl and the Sniffers", "Kevin Abstract", "Paul Cauthen", "The Japanese House", "Romy", 
        "The Last Dinner Party", "BabaDonnatogo", "STRFKR", "Real Estate", "K.Flay", "Corinne Bailey Rae", 
        "Snakehips", "Amen Dunes", "Roosevelt", "Allen Stone", "Mindchatter", "Dadi Freyr", "Ryan Beatty", 
        "Leisure", "Elyanna", "Confidence Man", "Kasablanca", "Vandelux", "WISP", "Medium Build", "Rocco", 
        "underscores", "Devaull", "Chance Peña", "Mimi Webb", "Daily Bread", "Balthvs", "Shaboosey", 
        "Billy Woods", "The Lemon Twigs", "Trueno", "Sons of the East", "CMAT", "Cimafunk", "Katie Pruitt", 
        "AG Club", "Lady Wray", "Odie Leigh", "French Cassettes", "OGI", "Miles.", "Valencia Grace", 
        "Dan Spencer", "Lael Neale", "SOMA", "ANGRYBABY", "Anish Kumar", "AYYBO", "Darius", "Dusky", 
        "Honeyluv B2B Jaden Thompson", "Idris Elba", "Jackie Hollander", "Joe Kay B2B Jared Jackson", 
        "Kaleena Zanders", "Marsh", "Seth Troxler", "Shiba San B2B CID", "Sidepiece", "Sofia Kourtesis", 
        "TSHA", "Uncle Waffles", "Yulia Niko", "Post Malone"
    ], "/static/festhead/outsidehead.jpeg", "/static/festlineup/outsidelineup.jpeg"),

    ("Stage Coach", "Indio, CA", datetime(2024, 9, 20), datetime(2024, 9, 22), [
        "Eric Church", "Jelly Roll", "Elle King", "Dwight Yoakam", "Carin León", "Paul Cauthen", 
        "Shane Smith & The Saints", "Hailey Whitters", "Josh Abbott Band", "Josh Ross", "Vincent Neil Emerson", 
        "Wyatt Flores", "Ben Burgess", "Lauren Watkins", "Zach Top", "Lola Kirke", "Miranda Lambert", 
        "Post Malone", "Willie Nelson & Family", "Leon Bridges", "Ernest", "Charley Crockett", "Luke Grimes", 
        "Maddie & Tae", "Trampled by Turtles", "Tenille Townes", "Asleep at the Wheel", "Kylie Morgan", 
        "Drayton Farley", "Casey Barnes", "Stephen Wilson Jr.", "Kassi Valazza", "Tanner Adell", "Morgan Wallen", 
        "Hardy", "Bailey Zimmerman", "The Beach Boys", "Megan Moroney", "Clint Black", "Nate Smith", "Pam Tillis", 
        "Charles Wesley Godwin", "The War and Treaty", "Ashley Cooke", "Sam Barber", "Brittney Spencer", 
        "Willie Jones", "Dylan Schneider", "Katie Pruitt", "Miko Marks", "Nickelback", "Diplo", "Wiz Khalifa", 
        "Guy Fieri's Stagecoach Smokehouse", "Diplo's HonkyTonk", "Compton Cowboys"
    ], "/static/festhead/stagecohead.jpeg", "/static/festlineup/stagecolineup.jpeg"),
]

for festival_data in festivals:
    fest_name, fest_location, fest_startdate, fest_enddate, lineup, fest_head, lineup_img = festival_data
    festival = crud.create_festival(fest_name, fest_location, fest_startdate, fest_enddate, lineup, fest_head, lineup_img)
    model.db.session.add(festival)
    model.db.session.commit()


# import os
# import json
# from random import choice, randint
# from datetime import datetime

# import crud
# import model
# import server

# os.system('dropdb ratings')
# os.system('createdb ratings')

# model.connect_to_db(server.app)
# model.db.create_all()

# user = crud.create_user("Ends", "Noodle", "Stinky Fart Boy", "angry@noodle.com", "fart")
# model.db.session.add(user)
# model.db.session.commit()

# user2 = crud.create_user("Archer", "Barcher", "Goofy Goober", "crazyeyez@dog.com", "rah")
# model.db.session.add(user2)
# model.db.session.commit()

# user3 = crud.create_user("Lettuce", "McSalad", "RubberLettuce81", "ceasar@dressing.com", "Toss")
# model.db.session.add(user3)
# model.db.session.commit()

# start = datetime(2024, 4, 20)
# end = datetime(2025, 4, 20)
# festival=crud.create_festival("Brochella", "Mojo Dojo Casa House", start, end, "Kens", "/static/festhead/coach.jpeg", "/static/festlineup/lineup.webp")
# model.db.session.add(festival)
# model.db.session.commit()

# start2 = datetime(2024, 6, 10)
# end2 = datetime(2025, 6, 12)
# festival2 = crud.create_festival("LA LA LAND", "Island", start2, end2, "lalalers")
# model.db.session.add(festival2)
# model.db.session.commit()

# start3 = datetime(2024, 8, 10)
# end3 = datetime(2024, 8, 12)
# festival3 = crud.create_festival("Manu", "BeachHouse", start3, end3, "Ye")
# model.db.session.add(festival3)
# model.db.session.commit()

# start4 = datetime(2024, 9, 9)
# end4 = datetime(2024, 9, 12)
# festival4 = crud.create_festival("JAMZ", "Miami", start4, end4, "Sean Kingston")
# model.db.session.add(festival4)
# model.db.session.commit()

# start5 = datetime(2024, 7, 12)
# end5 = datetime(2024, 7, 15)
# festival5 = crud.create_festival("bopper boppies", "Airplane", start5, end5, "Miley")
# model.db.session.add(festival5)
# model.db.session.commit()

# start6 = datetime(2024, 7, 20)
# end6 = datetime(2024, 7, 23)
# festival6 = crud.create_festival("slap city", "central park", start6, end6, "Lady Gaba")
# model.db.session.add(festival6)
# model.db.session.commit()

# start7 = datetime(2024, 6, 20)
# end7 = datetime(2024, 6, 23)
# festival7 = crud.create_festival("Pretty Girl Rock", "in da cloudz", start7, end7, "yonce")
# model.db.session.add(festival7)
# model.db.session.commit()

# start8 = datetime(2024, 9, 22)
# end8 = datetime(2024, 9, 25)
# festival8 = crud.create_festival("Groupies", "Trap House", start8, end8, "pussycat dolls")
# model.db.session.add(festival8)
# model.db.session.commit()

# start9 = datetime(2024, 12, 9)
# end9 = datetime(2024, 12, 12)
# festival9 = crud.create_festival("Vibechella", "lazy river", start9, end9, "Frank")
# model.db.session.add(festival9)
# model.db.session.commit()

# start10 = datetime(2024, 12, 24)
# end10 = datetime(2024, 12, 26)
# festival10 = crud.create_festival("Jingle UR Bells", "North Pole", start10, end10, "Ri Ri")
# model.db.session.add(festival10)
# model.db.session.commit()

# start11 = datetime(2024, 10, 11)
# end11 = datetime(2024, 10, 15)
# festival11 = crud.create_festival("rah rah", "North Pole", start11, end11, "t-pain")
# model.db.session.add(festival11)
# model.db.session.commit()

# start11 = datetime(2024, 10, 11)
# end11 = datetime(2024, 10, 15)
# festival11 = crud.create_festival("rah rah", "North Pole", start11, end11, "t-pain")
# model.db.session.add(festival11)
# model.db.session.commit()

# start12 = datetime(2024, 6, 13)
# end12 = datetime(2024, 6, 16)
# festival12 = crud.create_festival("Bonnaroo", "Manchester, TN", start12, end12, [
#     "Pretty Lights", "FISHER", "BigXthaPlug", "Disco Lines", "Durand Bernarr", 
#         "Eggy", "Geese", "Gwar", "The Heavy Heavy", "HoneyLuv", "it’s murph", 
#         "Matt Maltese", "Medium Build", "Michigander", "Militarie Gun", 
#         "Nation of Language", "Neal Francis’ Francis Comes Alive", "Ocie Elliott", 
#         "Oliver Heldens", "Róisín Murphy", "Say She She", "Sid Sriram", "Post Malone", 
#         "Maggie Rogers", "Khruangbin", "Seven Lions", "Joe Russo’s Almost Dead", 
#         "Dominic Fike", "Lizzy McAlpine", "Interpol", "T-Pain", "Svdden Death", 
#         "TV Girl", "Gary Clark Jr.", "The Mars Volta", "Faye Webster", "Key Glock", 
#         "Thundercat", "Lovejoy", "ISOxo", "GROUPLOVE", "David Kushner", "The Japanese House", 
#         "Dr. Fresch", "49 Winchester", "MIKE.", "Larkin Poe", "Shy FX", "Bonny Light Horseman", 
#         "Baby Queen", "Mdou Moctar", "Jessica Audiffred", "Half Moon Run", "Hamdi", "LYNY", 
#         "Red Hot Chili Peppers", "Cage The Elephant", "Melanie Martinez", "Cigarettes After Sex", 
#         "Diplo", "Jon Batiste", "Reneé Rapp", "Parcels", "IDLES", "Brittany Howard", "Sean Paul", 
#         "Knock2", "Ethel Cain", "Gregory Alan Isakov", "The Teskey Brothers", "BADBADNOTGOOD", 
#         "Teezo Touchdown", "Whyte Fang", "Bakar", "d4vd", "The Maine", "Josiah and the Bonnevilles", 
#         "Kasablanca", "NEIL FRANCES", "Tanner Usrey", "Ryan Beatty", "MIKE", "Trousdale", "Vandelux", 
#         "LOVRA", "Once More With Feeling(s) – The Dashboard Confessional Emo SuperJam", "Fred again..", 
#         "Megan Thee Stallion", "Jason Isbell and the 400 Unit", "Two Friends", "Carly Rae Jepsen", 
#         "Joey Bada$$", "Goth Babe", "Galantis", "Taking Back Sunday", "Ashnikko", "Four Tet", 
#         "Charles Wesley Godwin", "Milky Chance", "Chappell Roan", "Greensky Bluegrass", 
#         "The Garden", "Yves Tumor", "The Beaches", "Jake Wesley Rogers", "S.G. Goodman", 
#         "Libianca", "TSHA", "Irreversible Entanglements", "Armand Hammer", "veggi"
# ])
# model.db.session.add(festival12)
# model.db.session.commit()



# with open("data/festivals.json") as f:
#     festival_data = json.loads(f.read())

# festivals_in_db = []
# for festival in festival_data:
#     fest_name, fest_location, line_up, poster_path = (
#         festival["fest_name"],
#         festival["fest_location"],
#         festival["line_up"],
#         festival["poster_path"],
#     )
#     fest_date = datetime.strptime(festival["fest_date"], "%Y-%m-%d")

#     db_festival = crud.create_festival(fest_name, fest_location, fest_date, line_up, poster_path)
#     festivals_in_db.append(db_festival)

# model.db.session.add_all(festivals_in_db)
# model.db.session.commit()