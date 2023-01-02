from plotnine import ggplot, aes, geom_line
import pandas as pd
from random import choices

population = [0, 1]
weights = [0.5, 0.5]

data_sequence = open("data01.txt", "r").read()
#print(data_sequence)
sequence_size = 20
probality_of_one = 0.5
sequence_predictions = {}
sequence_probability = {}
sequence_occurences = {}
sequence_hits = {}
our_param = 0.1
hit = 0


accuracies = []
hits = []
positions = []
sizes = []
data_to_plot = {}

def updateProb(occ, hit):
    # updatedProb = 0
    # for o in range(1, occ + 1):
    #     updatedProb += pow(prob, o)
    # # print(updatedProb)
    # return updatedProb
    return hit / occ




if sequence_size > len(data_sequence):
    print("Window is to big")

i = 0

for ch in data_sequence[sequence_size:len(data_sequence):1]:
    if data_sequence[0 + i:sequence_size + i] not in sequence_predictions:
        chosen = choices(population, weights)
        if chosen == 1:
            if ch == '1':
                sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 1
                # sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(1, our_param)
                sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = 1
                sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                sequence_hits[str(data_sequence[0 + i:sequence_size + i])] = 1
                hit += 1
            else:
                sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 0
                # sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(1, our_param)
                sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = 0
                sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                sequence_hits[str(data_sequence[0 + i:sequence_size + i])] = 0
        else:
            if ch == '0':
                sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 0
                # sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(1, our_param)
                sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = 1
                sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                sequence_hits[str(data_sequence[0 + i:sequence_size + i])] = 1
                hit += 1
            else:
                sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 1
                # sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(1, our_param)
                sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = 0
                sequence_hits[str(data_sequence[0 + i:sequence_size + i])] = 1
                sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1

    else:
        if sequence_probability[str(data_sequence[0 + i:sequence_size + i])] >= 0.5:
            if ch == sequence_predictions[str(data_sequence[0 + i:sequence_size + i])]:
                if ch == '1':
                    # sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] + 1
                    sequence_hits[str(data_sequence[0 + i:sequence_size + i])] = sequence_hits[str(data_sequence[0 + i:sequence_size + i])] + 1
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], sequence_hits[str(data_sequence[0 + i:sequence_size + i])])
                    hit += 1
                elif ch == '0':
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1
                    if sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] == 0:
                        sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                        sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 1
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], sequence_hits[str(data_sequence[0 + i:sequence_size + i])])
                    hit += 1
            else:
                if ch == '1':
                    # sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1
                    if sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] == 0:
                        sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                        sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 0
                    sequence_hits[str(data_sequence[0 + i:sequence_size + i])] = sequence_hits[str(data_sequence[0 + i:sequence_size + i])] + 1
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], sequence_hits[str(data_sequence[0 + i:sequence_size + i])])
                elif ch == '0':
                    # sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1
                    if sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] == 0:
                        sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                        sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 1
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], sequence_hits[str(data_sequence[0 + i:sequence_size + i])])
        else:
            if ch == sequence_predictions[str(data_sequence[0 + i:sequence_size + i])]:
                if ch == '1':
                    # sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1
                    if sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] == 0:
                        sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                        sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 0
                    sequence_hits[str(data_sequence[0 + i:sequence_size + i])] = sequence_hits[str(data_sequence[0 + i:sequence_size + i])] + 1
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], sequence_hits[str(data_sequence[0 + i:sequence_size + i])])
                    hit += 1
                elif ch == '0':
                    # sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] + 1
                    sequence_hits[str(data_sequence[0 + i:sequence_size + i])] = sequence_hits[str(data_sequence[0 + i:sequence_size + i])] + 1
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], sequence_hits[str(data_sequence[0 + i:sequence_size + i])])
                    hit += 1
            else:
                if ch == '1':
                    # sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1
                    if sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] == 0:
                        sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                        sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 0
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], sequence_hits[str(data_sequence[0 + i:sequence_size + i])])
                elif ch == '0':
                    # sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1
                    if sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] == 0:
                        sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                        sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 1
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], sequence_hits[str(data_sequence[0 + i:sequence_size + i])])

    # if (i % 100 == 0 or i < 100) and i != 0:
    if i != 0:
        accuracies.append(float(hit/i))
        hits.append(hit)
        positions.append(i)
        sizes.append(len(sequence_occurences) + len(sequence_predictions) + len(sequence_probability))
        data_to_plot[i] = hit



    i += 1
    if i >= len(data_sequence):
        break

# print("\n\n")
# print(sequence_predictions)
# print("\n\n")
# print(sequence_probability)
# print("\n\n")
# print(sequence_occurences)
# print("\n\n")

# print(F"NUMER I: {str(i + sequence_size)} blad: {accuracies} = {hit} / {i + sequence_size}")

print(data_to_plot)

j = 1
pdd = ({
    'size [bites]': [0],
    'errors': [accuracies[0]]
})
for elem in accuracies:
    # pdd['characters'].append(j)
    pdd['errors'].append(elem)
    # print(pdd)
    # j += 1

for el in sizes:
   pdd['size [bites]'].append(el) 

pd_data = pd.DataFrame(pdd, columns=['size [bites]', 'errors'])

# pd_data.drop(pd_data.loc[pd_data['characters'] < sequence_size].index, inplace=True)
pd_data.drop(pd_data.loc[pd_data['errors'] > 1].index, inplace=True)

print(pd_data)
g = ggplot(pd_data) + aes(x='size [bites]', y='errors') + geom_line()
print(g)

# print(hit / i)