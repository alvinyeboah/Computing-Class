import csv 

Country_name=[]
Population=[]
Literacy_rate=[]
mobile_subscriptions=[]
internet_users=[]
production =[]
consumption =[]
dict1= {}
count = -1



with open("/Users/alvinyeboah/Documents/Uni/Computing/Assignments/CA4/CountryData.csv", 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader, None) #this makes it ignore the first line, because theyre titles
    for column in csv_reader:
        count += 1
        Country_name.append(column[0])
        Population.append(column[1])
        Literacy_rate.append(column[2])
        mobile_subscriptions.append(column[3])
        internet_users.append(column[4])
        production.append(column[5])
        consumption.append(column[6])
        dict1[column[0]] = count
    

def query():
    user_input= input("Hello! What country would you like information on? ")
    user_input_new = user_input[0].upper() + user_input[1:]
    for x,y in dict1.items():
        if user_input_new == x:
            print(f"{x} has a population of {Population[y]} and a literacy rate of {Literacy_rate[y]}%. The estimate of the number of mobile subscriptions is {mobile_subscriptions[y]}, while that of internet users is {internet_users[y]}.Ghana produces {production[y]} billion KWh of electricity annually, while it consumes {consumption[y]} billion KWh of electricity.")


def new_file():
    output_file_path = 'output.txt'
    with open(output_file_path, 'w') as file:
        file.write(f"Country\tMobile subscriptions per capita\tInternet users per capita\n")
        for i in range(len(Country_name)):
            file.write(f"{Country_name[i]}\t{(float(mobile_subscriptions[i]) / float(Population[i]))}\t{(float(internet_users[i]) / float(Population[i]))}\n")

def report():
    total_population = 0
    