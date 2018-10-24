### This tool creates random data.
### Address section adapted from rplaces.py by Mark Burgess
### v2.2 - 2/28/18
### Bart Cross

import random # For random number generator
import os     # For function to check file size

city_names = ["Adams Center", "Ahsahka", "Alcoa", \
"Allendale", "Altamonte Springs", "Amberson", "Ancona", "Ansley", "Aragon", "Ark", \
"Arroyo Seco", "Aspen", "Auburn Hills", "Awendaw", "Bakers Mills", "Banner", \
"Barnhill", "Batavia", "Bazine", "Beaverville", "Belews Creek", "Bellport", \
"Bennington", "Berrien Springs", "Biddle", "Biglerville", "Black Earth", "Blandon", \
"Blue Bell", "Bock", "Bondsville", "Boscobel", "Bowling Green", "Bradgate", "Brave", \
"Bridger", "Broadlands", "Brooks", "Bruner", "Bucoda", "Buras", "Burr Hill", "Cabazon", \
"California Hot Springs", "Camp", "Canby", "Capay", "Carle Place", "Carrollton", \
"Casscoe", "Catlett", "Cedar Mountain", "Centerport", "Chamisal", "Charlton", "Cherokee", \
"Chicago Ridge", "Chloride", "Cinebar", "Clarks Hill", "Clementon", "Cloudcroft", "Coburn", \
"Colby", "Coloma", "Comptche", "Constable", "Copeland", "Cornwall On Hudson", \
"Cotton Valley", "Cowpens", "Creekside", "Cropsey", "Crumrod", "Cupertino", "Dahinda", \
"Dansville", "Dawn", "Debord", "Delavan", "Dennison", "Devol", "Dillon Beach", "Doerun", \
"Doss", "Drayden", "Duck", "Dunmore", "Eads", "East Berkshire", "East Granby", \
"East Orleans", "East Waterboro", "Eckert", "Edson", "Elaine", "Elk Mountain", \
"Ellison Bay", "Elwin", "Engadine", "Eros", "Eton", "Ewell", "Fairlawn", "Fannettsburg", \
"Faywood", "Fidelity", "Fiskeville", "Flora Vista", "Ford", "Fort Ann", "Fort Knox", \
"Fort Sumner", "Foxburg", "Freeburg", "Frontenac", "Galax", "Garden City", "Gates Mills", \
"Germfask", "Gillett Grove", "Glen Arbor", "Glendive", "Gobler", "Goodhue", "Gower", \
"Grand Rapids", "Grassflat", "Green Creek", "Greenview", "Grove City", "Gulston", "Hagan", \
"Halltown", "Hanna", "Harlan", "Harsens Island", "Hat Creek", "Hayden", "Hebron", \
"Henniker", "Hershey", "Higginson", "Hillman", "Hobson", "Hollowville", "Honea Path", \
"Horace", "Housatonic", "Hughson", "Hurdle Mills", "Icard", "Indian Hills", "Iowa City", \
"Island Grove", "Jacksboro", "Jayton", "Jesse", "Jonestown", "Kaiser", "Kasota", \
"Keithsburg", "Kennedale", "Ketchum", "Killen", "Kingstree", "Klamath River", "Kremlin", \
"La Jolla", "Laceyville", "Lake Ann", "Lake Milton", "Lamartine", "Langston", "Latonia", \
"Layton", "Leechburg", "Lenapah", "Letts", "Likely", "Linesville", "Little Hocking", \
"Lockesburg", "Lone", "Lookeba", "Lothair", "Lowndes", "Lumber City", "Lyndell", "Mackay", \
"Maida", "Manasquan", "Mansfield Center", "Marathon Shores", "Marion Station", "Mart", \
"Massapequa", "Mauriceville", "Mc Adams", "Mc Donough", "Mc Quady", "Meadow Creek", "Melba", \
"Mer Rouge", "Mesick", "Middle Village", "Milesville", "Millport", "Minersville", \
"Mississippi State", "Mollusk", "Montcalm", "Moorcroft", "Mormon Lake", "Mott", \
"Mount Hood Parkdale", "Mount Wilson", "Muldraugh", "Muscatine", "Nanuet", "Naugatuck", \
"Nellysford", "New Auburn", "New Florence", "New Meadows", "New Ulm", "Newmanstown", \
"Nimitz", "Norene", "North Canton", "North Java", "North Scituate", "Northville", \
"O Fallon", "Ocala", "Ogallala", "Olancha", "Oliver Springs", "Onset", "Ore City", \
"Orson", "Otter Creek", "Oyster", "Pala", "Panama City", "Parker Ford", "Patoka", \
"Pea Ridge", "Pekin", "Penns Grove", "Perry Park", "Phenix City", "Pierre", "Pine Hill", \
"Pioche", "Plano", "Plum City", "Pollard", "Poplar Bluff", "Port Norris", "Poston", \
"Pownal", "Priddy", "Pryor", "Quanah", "Radisson", "Randolph Center", "Rayland", \
"Red Lake Falls", "Reeds Spring", "Renton", "Rhododendron", "Ridge", "Rio Dell", \
"Rixeyville", "Rock Glen", "Rocky Point", "Ronks", "Roslyn Heights", "Roxobel", \
"Rush Springs", "Sabula", "Saint Cloud", "Saint Marys", "Salley", "San Fidel", \
"Sandersville", "Santaquin", "Saukville", "Schaumburg", "Scott City", "Searsmont", \
"Sellersville", "Shade", "Shaw", "Shepherdsville", "Shonto", "Sikeston", "Singer", \
"Slate Spring", "Smiths Creek", "Solana Beach", "South Amboy", "South Hadley", \
"South Richmond Hill", "Southold", "Spiro", "Springport", "Stanville", "Steelville", \
"Stillman Valley", "Storrie", "Stroud", "Suisun City", "Sun Valley", "Suwannee", \
"Sybertsville", "Talladega", "Tarrytown", "Telluride", "Tewksbury", "Thomson", "Tigrett", \
"Titus", "Tonkawa", "Township Of Washington", "Trexlertown", "Truro", "Turners", \
"Two Rivers", "Unicoi", "Upton", "Valley Ford", "Vandervoort", "Verdon", "Vienna", \
"Viroqua", "Wagoner", "Walkertown", "Waltonville", "Warners", "Waterboro", "Wausa", \
"Weedsport", "Wenden", "West Copake", "West Hills", "West Plains", "Westby", "Wevertown", \
"White Mills", "Whitley City", "Wildorado", "Willow Spring", "Winfall", "Winthrop Harbor", \
"Wolverine", "Woodville", "Wyandotte", "Yawkey", "Yucca Valley"]

state_abbs = ["AL", "AK", "AZ", "AR",\
"CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",\
"LA", "ME", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR",\
"MD", "MA", "MI", "MN", "MS", "MO", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT",\
"VA", "WA", "WV", "WI", "WY"]

street_names = ["Main Street", "Church Street",\
"Main Street North", "High Street", "Elm Street", "Main Street South", "Chestnut Street",\
"Washington Street", "Maple Street", "Walnut Street", "Main Street West", "Broad Street",\
"2nd Street", "Center Street", "Maple Avenue", "Main Street East", "Park Avenue",\
"Pine Street", "South Street", "Water Street", "School Street", "Union Street",\
"North Street", "Oak Street", "Market Street", "Spring Street", "River Road", "Court Street",\
"Prospect Street", "Front Street", "Park Street", "3rd Street", "Washington Avenue",\
"Cedar Street", "Cherry Street", "Central Avenue", "Franklin Street", "Highland Avenue",\
"Bridge Street", "Spruce Street", "West Street", "State Street", "1st Street", "East Street",\
"4th Street", "Locust Street", "Pleasant Street", "Ridge Road", "Adams Street", "Church Road",\
"Dogwood Drive", "Elizabeth Street", "Green Street", "Jefferson Street", "Lincoln Avenue",\
"Mill Street", "Pennsylvania Avenue", "Hill Street", "Jackson Street", "Park Place",\
"Creek Road", "Delaware Avenue", "Division Street", "Dogwood Lane", "Durham Road",\
"Fairview Avenue", "Front Street North", "Garden Street", "Laurel Lane", "Monroe Street",\
"Prospect Avenue", "Railroad Avenue", "Willow Street", "10th Street", "13th Street",\
"4th Avenue", "Buckingham Drive", "Cedar Lane", "Cottage Street", "Devon Road", "Elm Avenue",\
"Franklin Court", "John Street", "Lafayette Avenue", "Lake Street", "Laurel Street",\
"Mulberry Street", "Olive Street", "Riverside Drive", "5th Street South",\
"5th Street West", "6th Street North", "7th Street", "Bank Street", "Belmont Avenue",\
"Brookside Drive", "Cambridge Court", "Chapel Street", "Charles Street", "College Street",\
"Colonial Avenue", "Creekside Drive", "Crescent Street", "Cypress Court", "Essex Court",\
"Forest Drive", "Garfield Avenue", "George Street", "Glenwood Avenue", "Hamilton Street",\
"Highland Drive", "James Street", "King Street", "Laurel Drive", "Orange Street",\
"Oxford Court", "Poplar Street", "Route 11", "Smith Street", "Surrey Lane", "Tanglewood Drive",\
"Deerfield Drive", "Devonshire Drive", "Durham Court", "Eagle Road", "Fawn Lane",\
"Forest Street", "Fulton Street", "Harrison Avenue", "Henry Street", "Hillcrest Avenue",\
"Lake Avenue", "Lantern Lane", "Linden Street", "Magnolia Court", "Magnolia Drive",\
"Mechanic Street", "Mulberry Court", "Park Drive", "Pheasant Run",\
"Route 9", "Sherwood Drive", "Strawberry Lane", "Summit Street", "Taylor Street",\
"Wall Street", "Williams Street", "Windsor Court", "Woodland Road", "14th Street",\
"Sheffield Drive", "Spruce Avenue", "Summer Street", "Sunset Avenue", "Sycamore Drive",\
"Valley Drive", "Valley View Road", "Victoria Court", "Warren Avenue", "Warren Street",\
"West Avenue", "Westminster Drive", "Willow Drive", "Wood Street", "York Street"]

female_names = ["Mary", "Patricia",\
"Linda", "Barbara", "Elizabeth", "Jennifer", "Maria", "Susan",\
"Margaret", "Dorothy", "Lisa", "Nancy", "Karen", "Betty", "Helen",\
"Sandra", "Donna", "Carol", "Ruth", "Sharon", "Michelle", "Laura",\
"Sarah", "Kimberly", "Deborah", "Jessica", "Shirley", "Cynthia",\
"Angela", "Melissa", "Brenda", "Amy", "Anna", "Rebecca",\
"Virginia", "Kathleen", "Pamela", "Martha", "Debra", "Amanda",\
"Stephanie", "Carolyn", "Christine", "Marie", "Janet", "Catherine",\
"Frances", "Ann", "Joyce", "Diane", "Alice", "Julie", "Heather",\
"Teresa", "Doris", "Gloria", "Evelyn", "Jean", "Cheryl", "Mildred",\
"Katherine", "Joan", "Ashley", "Judith", "Rose", "Janice", "Kelly",\
"Nicole", "Judy", "Christina", "Kathy", "Theresa", "Beverly",\
"Denise", "Tammy", "Irene", "Jane", "Lori", "Rachel", "Marilyn",\
"Andrea", "Kathryn", "Louise", "Sara", "Anne", "Jacqueline",\
"Wanda", "Bonnie", "Julia", "Ruby", "Lois", "Tina", "Phyllis",\
"Norma", "Paula", "Diana", "Annie", "Lillian", "Emily", "Robin",\
"Peggy", "Crystal", "Gladys", "Rita", "Dawn", "Connie", "Florence",\
"Tracy", "Edna", "Tiffany", "Carmen", "Rosa", "Cindy", "Grace",\
"Wendy", "Victoria", "Edith", "Kim", "Sherry", "Sylvia",\
"Josephine", "Thelma", "Shannon", "Sheila", "Ethel", "Ellen",\
"Elaine", "Marjorie", "Carrie", "Charlotte", "Monica", "Esther",\
"Pauline", "Emma", "Juanita", "Anita", "Rhonda", "Hazel", "Amber",\
"Eva", "Debbie", "April", "Leslie", "Clara", "Lucille", "Jamie",\
"Joanne", "Eleanor", "Valerie", "Danielle", "Megan", "Alicia",\
"Suzanne", "Michele", "Gail", "Bertha", "Darlene", "Veronica",\
"Jill", "Erin", "Geraldine", "Lauren", "Cathy", "Joann",\
"Lorraine", "Lynn", "Sally", "Regina", "Erica", "Beatrice",\
"Dolores", "Bernice", "Audrey", "Yvonne", "Annette", "June",\
"Samantha", "Marion", "Dana", "Stacy", "Ana", "Renee", "Ida",\
"Vivian", "Roberta", "Holly", "Brittany", "Melanie", "Loretta",\
"Yolanda", "Jeanette", "Laurie", "Katie", "Kristen", "Vanessa",\
"Alma", "Sue", "Elsie", "Beth", "Jeanne", "Vicki", "Carla", "Tara",\
"Rosemary", "Eileen", "Terri", "Gertrude", "Lucy", "Tonya", "Ella",\
"Stacey", "Wilma", "Gina", "Kristin", "Jessie", "Natalie", "Agnes",\
"Vera", "Willie", "Charlene", "Bessie", "Delores", "Melinda",\
"Pearl", "Arlene", "Maureen", "Colleen", "Allison", "Tamara",\
"Joy", "Georgia", "Constance", "Lillie", "Claudia", "Jackie",\
"Marcia", "Tanya", "Nellie", "Minnie", "Marlene", "Heidi",\
"Glenda", "Lydia", "Viola", "Courtney", "Marian", "Stella",\
"Caroline", "Dora", "Jo"]

male_names = ["James", "John",\
"Robert", "Michael", "William", "David", "Richard", "Charles",\
"Joseph", "Thomas", "Christopher", "Daniel", "Paul", "Mark",\
"Donald", "George", "Kenneth", "Steven", "Edward", "Brian",\
"Ronald", "Anthony", "Kevin", "Jason", "Matthew", "Gary",\
"Timothy", "Jose", "Larry", "Jeffrey", "Frank", "Scott", "Eric",\
"Stephen", "Andrew", "Raymond", "Gregory", "Joshua", "Jerry",\
"Dennis", "Walter", "Patrick", "Peter", "Harold", "Douglas",\
"Henry", "Carl", "Arthur", "Ryan", "Roger", "Joe", "Juan", "Jack",\
"Albert", "Jonathan", "Justin", "Terry", "Gerald", "Keith",\
"Samuel", "Willie", "Ralph", "Lawrence", "Nicholas", "Roy",\
"Benjamin", "Bruce", "Brandon", "Adam", "Harry", "Fred", "Wayne",\
"Billy", "Steve", "Louis", "Jeremy", "Aaron", "Randy", "Howard",\
"Eugene", "Carlos", "Russell", "Bobby", "Victor", "Martin",\
"Ernest", "Phillip", "Todd", "Jesse", "Craig", "Alan", "Shawn",\
"Clarence", "Sean", "Philip", "Chris", "Johnny", "Earl", "Jimmy",\
"Antonio", "Danny", "Bryan", "Tony", "Luis", "Mike", "Stanley",\
"Leonard", "Nathan", "Dale", "Manuel", "Rodney", "Curtis",\
"Norman", "Allen", "Marvin", "Vincent", "Glenn", "Jeffery",\
"Travis", "Jeff", "Chad", "Jacob", "Lee", "Melvin", "Alfred",\
"Kyle", "Francis", "Bradley", "Jesus", "Herbert", "Frederick",\
"Ray", "Joel", "Edwin", "Don", "Eddie", "Ricky", "Troy", "Randall",\
"Barry", "Alexander", "Bernard", "Mario", "Leroy", "Francisco",\
"Marcus", "Micheal", "Theodore", "Clifford", "Miguel", "Oscar",\
"Jay", "Jim", "Tom", "Calvin", "Alex", "Jon", "Ronnie", "Bill",\
"Lloyd", "Tommy", "Leon", "Derek", "Warren", "Darrell", "Jerome",\
"Floyd", "Leo", "Alvin", "Tim", "Wesley", "Gordon", "Dean", "Greg",\
"Jorge", "Dustin", "Pedro", "Derrick", "Dan", "Lewis", "Zachary",\
"Corey", "Herman", "Maurice", "Vernon", "Roberto", "Clyde", "Glen",\
"Hector", "Shane", "Ricardo", "Sam", "Rick", "Lester", "Brent",\
"Ramon", "Charlie", "Tyler", "Gilbert", "Gene", "Marc", "Reginald",\
"Ruben", "Brett", "Angel", "Nathaniel", "Rafael", "Leslie",\
"Edgar", "Milton", "Raul", "Ben", "Chester", "Cecil", "Duane",\
"Franklin", "Andre", "Elmer", "Brad", "Gabriel", "Ron", "Mitchell",\
"Roland", "Arnold", "Harvey", "Jared", "Adrian", "Karl", "Cory",\
"Claude", "Erik", "Darryl", "Jamie", "Neil", "Jessie", "Christian",\
"Javier", "Fernando", "Clinton", "Ted", "Mathew", "Tyrone",\
"Darren", "Lonnie", "Lance", "Cody", "Julio", "Kelly", "Kurt",\
"Allan"]

last_names = ["Smith",\
"Johnson", "Williams", "Jones", "Brown", "Davis", "Miller",\
"Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson",\
"White", "Harris", "Martin", "Thompson", "Garcia", "Martinez",\
"Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall",\
"Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill",\
"Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter",\
"Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell",\
"Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez",\
"Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy",\
"Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard",\
"Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson",\
"Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes",\
"Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell",\
"Long", "Patterson", "Hughes", "Flores", "Washington", "Butler",\
"Simmons", "Foster", "Gonzales", "Bryant", "Alexander", "Russell",\
"Griffin", "Diaz", "Hayes", "Myers", "Ford", "Hamilton", "Graham",\
"Sullivan", "Wallace", "Woods", "Cole", "West", "Jordan", "Owens",\
"Reynolds", "Fisher", "Ellis", "Harrison", "Gibson", "McDonald",\
"Cruz", "Marshall", "Ortiz", "Gomez", "Murray", "Freeman", "Wells",\
"Webb", "Simpson", "Stevens", "Tucker", "Porter", "Hunter",\
"Hicks", "Crawford", "Henry", "Boyd", "Mason", "Morales",\
"Kennedy", "Warren", "Dixon", "Ramos", "Reyes", "Burns", "Gordon",\
"Shaw", "Holmes", "Rice", "Robertson", "Hunt", "Black", "Daniels",\
"Palmer", "Mills", "Nichols", "Grant", "Knight", "Ferguson",\
"Rose", "Stone", "Hawkins", "Dunn", "Perkins", "Hudson", "Spencer",\
"Gardner", "Stephens", "Payne", "Pierce", "Berry", "Matthews",\
"Arnold", "Wagner", "Willis", "Ray", "Watkins", "Olson", "Carroll",\
"Duncan", "Snyder", "Hart", "Cunningham", "Bradley", "Lane",\
"Andrews", "Ruiz", "Harper", "Fox", "Riley", "Armstrong",\
"Carpenter", "Weaver", "Greene", "Lawrence", "Elliott", "Chavez",\
"Sims", "Austin", "Peters", "Kelley", "Franklin", "Lawson",\
"Fields", "Gutierrez", "Ryan", "Schmidt", "Carr", "Vasquez",\
"Castillo", "Wheeler", "Chapman", "Oliver", "Montgomery",\
"Richards", "Williamson", "Johnston", "Banks", "Meyer", "Bishop",\
"McCoy", "Howell", "Alvarez", "Morrison", "Hansen", "Fernandez",\
"Garza", "Harvey", "Little", "Burton", "Stanley", "Nguyen",\
"George", "Jacobs", "Reid", "Kim", "Fuller", "Lynch", "Dean",\
"Gilbert", "Garrett", "Romero", "Welch", "Larson", "Frazier",\
"Burke", "Hanson", "Day", "Mendoza", "Moreno", "Bowman", "Medina",\
"Fowler"]

gender = ["m", "f"]

def gen_ssn():
    qty = int(input('How many numbers would you like? '))
    n = input('What would you like the file name to be? ')
    fhand = open(n,'w')
    count = 0
    while count < qty:
        area = random.randint(1, 899)
        if area == 666:
            area += 1
        group = random.randint(1, 99)
        serial = random.randint(1, 9999)
        ssn = "{0:03d}-{1:02d}-{2:04d}".format(area, group, serial)
        fhand.write(ssn)
        fhand.write('\n')
        count = count + 1
    fhand.close()

def gen_add():
    count = 0
    qty = int(input('How many addresses would you like? '))
    n = input('What would you like the file name to be? ')
    fhand = open(n,'w')

    while count < qty:
        number = str(random.randint(10, 15000))
        street = random.choice(street_names)
        full_address = number + " " + street
        city = random.choice(city_names)
        state = random.choice(state_abbs)
        z = random.randint(1, 98000)
        zip = str(z).zfill(5)
        fhand.write(full_address)
        fhand.write(",")
        fhand.write(city)
        fhand.write(",")
        fhand.write(state)
        fhand.write(",")
        fhand.write(zip)
        fhand.write('\n')
        count = count + 1
    fhand.close()
    
def gen_name():
    qty = int(input('How many names would you like? '))
    separate = input('Would you like the names (s)eperate or (c)ombned?')
    n = input('What would you like the file name to be? ')
    fhand = open(n,'w')
    count = 0
    while count < qty:
        g = random.choice(gender)
        if g == "m":
            fname = random.choice(male_names)
        else:
            fname = random.choice(female_names)
        
        lname = random.choice(last_names)
        
        if separate == "s":
            fhand.write(fname)
            fhand.write(",")
            fhand.write(lname)
            fhand.write('\n')
        else:
            fhand.write(fname)
            fhand.write(" ")
            fhand.write(lname)
            fhand.write('\n')           
        count = count + 1
    fhand.close()
    
def gen_file():
    print('This will create a file of random 9 digit numbers.\n')
    size = input('How big would you like the file in megabytes? ')
    n = input('What would you like the file name to be? ')
    fhand = open(n,'w')

    sizem = int(size) # Size in megabytes
    sizeb = sizem * 1024 * 1024  # Convert to bytes

    lines = sizeb / 902  # Calculates the number of lines needed. Each line of 100,
                         # 9-digit numbers is 902 bytes

    counti = 0
    countl = 0
    line = []

    ### This section creates a dictionary of line numbers at 10%, 20%, etc...
    ### through the file to show progress
    counter = 10
    increment = int(lines / 10)
    progress = {}
    while counter <= 100:
	    progress[int(counter * increment / 10)] = counter
	    counter = counter + 10
	
    while countl < lines:
	    while counti <= 100:
		    line.append(random.randint(1000000,9999999))
		    counti = counti + 1
	    newline = str(line[0:counti - 1])
	    fhand.write(newline)
	    fhand.write('\n')
	    if countl in progress:  # This checks to see if we hit a progress milestone
		    print(progress[countl],'% complete')
	    counti = 0
	    line = []
	    countl = countl + 1

    fhand.close()
	
    b = int(os.path.getsize(n))
    k = int(os.path.getsize(n) / 1024)
    m = int(os.path.getsize(n) / 1024 / 1024)

    lines = int(lines)

    print('\n')
    print('The file',n,'is', '{0:,d}'.format(lines), 'lines long.')
    print('{0:,d}'.format(b),'bytes')
    print('{0:,d}'.format(k),'kilobytes')
    print('{0:,d}'.format(m),'megabytes')
    print('\n')
    
def gen_date():
    count = 0
    qty = int(input('How many dates would you like? '))
    n = input('What would you like the file name to be? ')
    fhand = open(n,'w')
    date = []

    while count < qty:
        month = random.randint(1, 12)
        day = random.randint(1,31)
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day == 31:
                day = day - 1
        elif month == 2:
            if day == 29 or day == 30 or day == 31:
                day = day - 4
        month = str(month)
        day = str(day)
        year = str(random.randint(1910, 2016))
        date = (month + "/" + day + "/" + year)
        fhand.write(date)
        fhand.write('\n')
        count = count + 1

### Main Program

print('This program will create random data.\n')
print('What type of data would you like?')
print('1 - Social Security Numbers')
print('2 - Addresses')
print('3 - Names')
print('4 - Dates')
print('5 - File')
print('q - Quit')
choice = input('Enter Choice: ')

while choice != 'q':
    if choice == '1':
        gen_ssn()
    elif choice == '2':
        gen_add()
    elif choice == '3':
        gen_name()
    elif choice == '4':
        gen_date()
    elif choice == '5':
        gen_file()
    elif choice == 'q':
        #print('Quitting')
        break
    choice = input('Enter Choice: ')

#print('Complete!')
#input('Press enter to close')






