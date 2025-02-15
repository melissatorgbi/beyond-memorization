import pandas as pd

file_name = "output/" #add filename to evaluate without .csv extension on string

results = pd.read_csv(file_name+".csv")
f = open(file_name+".txt", "w")

#calculate overall accuracy
total_accuracy = round(sum(results.Target==results.Response)/len(results),2)
f.write("Overall metrics" + "\nnumber: " + str(len(results)) + "\naccuracy: " + str(total_accuracy))
print(total_accuracy)

#calculate accuracy for each "type" in reasoning data 
for item in results.Type.unique().tolist():
    subset = results.where(results.Type==item).dropna(subset=['Type'])
    subset_accuracy = round(sum(subset.Target==subset.Response)/len(subset),2)
    
    #write to text file
    f.write("\n\nType: " + item + "\nnumber: " + str(len(subset)) + "\naccuracy: " + str(subset_accuracy) )


f.close()

