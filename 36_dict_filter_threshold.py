scores={"Abhay":85,"Sachin":70}
threshold = 75

filtered_score = {key: value for key, value in scores.items() if value > threshold}

print("Filtered Dictonary: ", filtered_score)

