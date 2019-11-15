import random, csv

cards_to_generate = 500

random.seed(42)
num_list = list(range(1,76))
sample_num = 1

# generate headers
header_list = ['row']
for val in list(range(1,25)):
    header_list.append('val' + str(val))


with open('bingocards.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header_list)

    for val in list(range(cards_to_generate)):
        random_list = random.sample(num_list, 24)
        random_list = [sample_num] + random_list
        writer.writerow(random_list)
        sample_num = sample_num + 1