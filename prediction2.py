data_sequence = open("data01.txt", "r").read()
# print(data_sequence)
# sequence_size = 10
probality_of_one = 0.5
sequence_predictions = {}
sequence_probability = {}
sequence_occurences = {}
# our_param = 0.1
hit = 0

def updateProb(occ, prob):
    updatedProb = 0
    for o in range(1, occ + 1):
        updatedProb += pow(prob, o)
    # print(updatedProb)
    return updatedProb


def algorithm(sequence_size, our_param):
    if sequence_size > len(data_sequence):
        print("Window is to big")

    hit = 0
    i = 0
    for ch in data_sequence[sequence_size:len(data_sequence):1]:
    # for ch in data_sequence[sequence_size:10:1]:
        print(data_sequence[0 + i:sequence_size + i])
        print(ch)
        if data_sequence[0 + i:sequence_size + i] not in sequence_predictions:
            # print(data_sequence[0 + i:sequence_size + i])
            # print(ch)
            if probality_of_one >= 0.5:
                sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 1
                if ch == sequence_predictions[str(data_sequence[0 + i:sequence_size + i])]:
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(1, our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                    hit += 1
                else:
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(1, our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 0
            else:
                sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 0
                if ch == sequence_predictions[str(data_sequence[0 + i:sequence_size + i])]:
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(1, our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                    hit += 1
                else:
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(1, our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 0

        else:
            if sequence_probability[str(data_sequence[0 + i:sequence_size + i])] >= 0.5:
                if ch == sequence_predictions[str(data_sequence[0 + i:sequence_size + i])]:
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] + 1
                    hit += 1
                else:
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1
            else:
                if ch == sequence_predictions[str(data_sequence[0 + i:sequence_size + i])]:
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] + 1
                    hit += 1
                else:
                    sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
                    sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1

            if sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] < 0:
                sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = 1 - sequence_probability[str(data_sequence[0 + i:sequence_size + i])]
                sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                if sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] == 1:
                    sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 0
                else:
                    sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 1
        # print(sequence_probability[str(data_sequence[0 + i:sequence_size + i])])
        
        i += 1

        print(hit)
    
    print(sequence_predictions)
    print(sequence_probability)
    print(sequence_occurences)


        # if data_sequence[0 + i:sequence_size + i] not in sequence_predictions:
        #     if probality_of_one >= 0.5:
        #         if ch == 1:
        #             print("not sequence 1 hit")
        #             sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 1
        #             sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(1, our_param)
        #             sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
        #             hit += 1
        #         else:
        #             print("not sequence 1 miss")
        #             sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 0
        #             sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(1, our_param)
        #             sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
        #     else:
        #         if ch == 0:
        #             print("not sequence 0 hit")
        #             sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 0
        #             sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(1, our_param)
        #             sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
        #             hit += 1
        #         else:
        #             print("not sequence 0 miss")
        #             sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] = 1
        #             sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(1, our_param)
        #             sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = 1
                
        # else:
        #     if sequence_probability[str(data_sequence[0 + i:sequence_size + i])] >= 0.5:
        #         if ch == sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] and ch == 1:
        #             print("one hit")
        #             sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
        #             sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] + 1
        #             hit += 1
        #         elif ch == sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] and ch == 0:
        #             print("one miss")
        #             sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
        #             sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1
        #     else:
        #         if ch == sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] and ch == 0:
        #             print("zero hit")
        #             sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one - updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
        #             sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] + 1
        #             hit += 1
        #         elif ch == sequence_predictions[str(data_sequence[0 + i:sequence_size + i])] and ch == 1:
        #             print("zero miss")
        #             sequence_probability[str(data_sequence[0 + i:sequence_size + i])] = probality_of_one + updateProb(sequence_occurences[str(data_sequence[0 + i:sequence_size + i])], our_param)
        #             sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] = sequence_occurences[str(data_sequence[0 + i:sequence_size + i])] - 1
        # i += 1

    # print("\n\n")
    # print(sequence_predictions)
    # print("\n\n")
    # print(sequence_probability)
    # print("\n\n")
    # print(sequence_occurences)
    # print("\n\n")

    # print(hit / i)

algorithm(5, 0.1)