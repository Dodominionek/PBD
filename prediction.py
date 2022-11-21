data_sequence = open("data01.txt", "r").read()
print(data_sequence)
window_size = 10
probality_of_one = 0.5
sequence_predictions = {}
sequence_probability = {}
sequence_occurences = {}
our_param = 0.1
hit = 0

if window_size > len(data_sequence):
    print("Window is to big")

i = 0

for ch in data_sequence[window_size:len(data_sequence):1]:
    print(ch, "\n")
    if data_sequence[0 + i:window_size + i] not in sequence_predictions:
        print("ins")
        if probality_of_one >= 0.5:
            if ch == 1:
                sequence_predictions[str(data_sequence[0 + i:window_size + i])] = 1
                sequence_probability[str(data_sequence[0 + i:window_size + i])] = probality_of_one + our_param
                sequence_occurences[str(data_sequence[0 + i:window_size + i])] = 1
                hit += 1
            else:
                sequence_predictions[str(data_sequence[0 + i:window_size + i])] = 0
                sequence_probability[str(data_sequence[0 + i:window_size + i])] = probality_of_one - our_param
                sequence_occurences[str(data_sequence[0 + i:window_size + i])] = 1
        else:
            if ch == 0:
                sequence_predictions[str(data_sequence[0 + i:window_size + i])] = 0
                sequence_probability[str(data_sequence[0 + i:window_size + i])] = probality_of_one - our_param
                sequence_occurences[str(data_sequence[0 + i:window_size + i])] = 1
                hit += 1
            else:
                sequence_predictions[str(data_sequence[0 + i:window_size + i])] = 1
                sequence_probability[str(data_sequence[0 + i:window_size + i])] = probality_of_one + our_param
                sequence_occurences[str(data_sequence[0 + i:window_size + i])] = 1
            
    else:
        if sequence_probability[str(data_sequence[0 + i:window_size + i])] >= 0.5:
            if ch == sequence_predictions[str(data_sequence[0 + i:window_size + i])] and ch == 1:
                sequence_probability[str(data_sequence[0 + i:window_size + i])] = probality_of_one + pow(our_param, sequence_occurences[str(data_sequence[0 + i:window_size + i])])
                sequence_occurences[str(data_sequence[0 + i:window_size + i])] = sequence_occurences[str(data_sequence[0 + i:window_size + i])] + 1
                hit += 1
            elif ch == sequence_predictions[str(data_sequence[0 + i:window_size + i])] and ch == 0:
                sequence_probability[str(data_sequence[0 + i:window_size + i])] = probality_of_one - pow(our_param, sequence_occurences[str(data_sequence[0 + i:window_size + i])])
                sequence_occurences[str(data_sequence[0 + i:window_size + i])] = sequence_occurences[str(data_sequence[0 + i:window_size + i])] - 1
        else:
            if ch == sequence_predictions[str(data_sequence[0 + i:window_size + i])] and ch == 0:
                sequence_probability[str(data_sequence[0 + i:window_size + i])] = probality_of_one - pow(our_param, sequence_occurences[str(data_sequence[0 + i:window_size + i])])
                sequence_occurences[str(data_sequence[0 + i:window_size + i])] = sequence_occurences[str(data_sequence[0 + i:window_size + i])] + 1
                hit += 1
            elif ch == sequence_predictions[str(data_sequence[0 + i:window_size + i])] and ch == 1:
                sequence_probability[str(data_sequence[0 + i:window_size + i])] = probality_of_one + pow(our_param, sequence_occurences[str(data_sequence[0 + i:window_size + i])])
                sequence_occurences[str(data_sequence[0 + i:window_size + i])] = sequence_occurences[str(data_sequence[0 + i:window_size + i])] - 1
    i += 1

print("\n\n")
print(sequence_predictions)
print("\n\n")
print(sequence_probability)
print("\n\n")
print(sequence_occurences)
print("\n\n")

print(hit / i)