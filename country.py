import json

index = 'cca2'
input_file = 'countries.json'
output_file = "countries_{}.json".format(index)

with open(input_file, "r") as read_file:
    countries = json.load(read_file)
    if countries:
        new_countries = {}
        for country in countries:
            new_countries.update({country[index]: country})

        with open(output_file, "w") as write_file:
            json.dump(new_countries, write_file)
        write_file.close()

    read_file.close()
