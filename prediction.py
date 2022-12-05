from plotnine import ggplot, aes, geom_line
import pandas as pd

data_sequence = open("data01.txt", "r").read()
#print(data_sequence)
sequence_size = 10
probality_of_one = 0.5
sequence_predictions = {}
sequence_probability = {}
sequence_occurences = {}
our_param = 0.1
hit = 0


accuracies = []
hits = []
positions = []
data_to_plot = {}

def updateProb(occ, prob):
    updatedProb = 0
    for o in range(1, occ + 1):
        updatedProb += pow(prob, o)
    # print(updatedProb)
    return updatedProb



if sequence_size > len(data_sequence):
    print("Window is to big")

i = 0

for ch in data_sequence[sequence_size:len(data_sequence):1]:
    if data_sequence[0 + i:sequence_size + i] not in sequence_predictions:
        if probality_of_one >= 0.5:
            if ch == '1':
                sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 1
                sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(1, our_param)
                sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                hit += 1
            else:
                sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 0
                sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(1, our_param)
                sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
        else:
            if ch == '0':
                sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 0
                sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(1, our_param)
                sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                hit += 1
            else:
                sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 1
                sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(1, our_param)
                sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1

    else:
        if sequence_probability[str(data_sequence[0 + i:sequence_size + i])] >= 0.5:
            if ch == sequence_predictions[str(data_sequence[0 + i:sequence_size + i])]:
                if ch == '1':
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] + 1
                    hit += 1
                elif ch == '0':
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1
                    hit += 1
            else:
                if ch == '1':
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1
                elif ch == '0':
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1
        else:
            if ch == sequence_predictions[str(data_sequence[0 + i:sequence_size + i])]:
                if ch == '1':
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1
                    hit += 1
                elif ch == '0':
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] + 1
                    hit += 1
            else:
                if ch == '1':
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1
                elif ch == '0':
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1

    if i == 300 or i == 500 or i == 1000 or i == 5000 or i == 10000 or i == 20000 - sequence_size - 1:
        accuracies.append(float(hit/i))
        hits.append(hit)
        positions.append(i)
        data_to_plot[i] = hit


    i += 1

# print("\n\n")
# print(sequence_predictions)
# print("\n\n")
# print(sequence_probability)
# print("\n\n")
# print(sequence_occurences)
# print("\n\n")

print(F"NUMER I: {str(i + sequence_size)} blad: {accuracies} = {hit} / {i + sequence_size}")

print(data_to_plot)

pd_data = pd.DataFrame(
    [
        [300, accuracies[0]],
        [500, accuracies[1]],
        [1000, accuracies[2]],
        [5000, accuracies[3]],
        [10000, accuracies[4]],
        [20000, accuracies[5]]
    ],
    columns=['characters', 'errors']    
)

#pd_data = pd.DataFrame([data_to_plot])

print(pd_data)
g = ggplot(pd_data) + aes(x='characters', y='errors') + geom_line()
print(g)

# print(hit / i)