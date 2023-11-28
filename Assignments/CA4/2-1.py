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
    with open("/Users/alvinyeboah/Documents/Uni/Computing/Assignments/CA4/CountryData.csv", 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)  
        
        total_population = 0
        most_populous_country = ""
        most_population = 0
        least_populous_country = ""
        least_population = float('inf')  
        total_literacy_rate = 0
        total_weighted_literacy_rate = 0
        total_mobile_subscriptions_per_capita = 0
        total_internet_users_per_capita = 0
        electricity_exporters = []
        electricity_importers = []

        for row in csv_reader:
            country_name = row[0]
            population = int(row[1])
            literacy_rate = float(row[2])
            mobile_subscriptions = float(row[3])
            internet_users = float(row[4])
            production = float(row[5])
            consumption = float(row[6])

            total_population += population
            total_literacy_rate += literacy_rate
            total_mobile_subscriptions_per_capita += mobile_subscriptions / population
            total_internet_users_per_capita += internet_users / population

            if population > most_population:
                most_population = population
                most_populous_country = country_name

            if population < least_population:
                least_population = population
                least_populous_country = country_name

            total_weighted_literacy_rate += (literacy_rate * population)

            if production > consumption:
                electricity_exporters.append(country_name)
            elif consumption > production:
                electricity_importers.append(country_name)

        # Calculate average literacy rate
        average_literacy_rate = total_weighted_literacy_rate / total_population

        print(f"The total population of Africa is {total_population}")
        print(f"The most populous country is {most_populous_country} with a population of {most_population}")
        print(f"The least populous country is {least_populous_country} with a population of {least_population}")
        print(f"The countries with the highest literacy rate is {most_populous_country}")
        print(f"The countries with the lowest literacy rate is {least_populous_country}")
        print(f"The average literacy rate in Africa is {average_literacy_rate}%")
        print(f"The countries with the highest number of mobile subscriptions per capita is {most_populous_country}")
        print(f"The countries with the lowest number of mobile subscriptions per capita is {least_populous_country}")
        print(f"The countries with the highest number of internet users per capita is {most_populous_country}")
        print(f"The countries with the lowest number of internet users per capita is {least_populous_country}")
        print(f"The electricity exporters are: {electricity_exporters}")
        print(f"The electricity importers are: {electricity_importers}")


report()


    
