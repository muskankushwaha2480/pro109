import csv
import pandas as pd 
import statistics 
import plotly.express as px
import plotly.figure_factory as ff 

df = pd.read_csv("StudentsPerformance.csv")

mathScore_list = df['math score'].tolist()

mathScore_mean = statistics.mean(mathScore_list)
mathScore_mode = statistics.mode(mathScore_list)
mathScore_median = statistics.median(mathScore_list)
mathScore_std = statistics.stdev(mathScore_list)

print("Mean of data : ",mathScore_mean)
print("Mode of data : ",mathScore_mode)
print("Median of data : ",mathScore_median)
print("std deviation of data : ",mathScore_std)

mathScore_first_std_deviation_start,mathScore_first_std_deviation_end = mathScore_mean - mathScore_std,mathScore_mean + mathScore_std
mathScore_second_std_deviation_start,mathScore_second_std_deviation_end = mathScore_mean - (2*mathScore_std), mathScore_mean + (2*mathScore_std)
mathScore_third_std_deviation_start,mathScore_third_std_deviation_end = mathScore_mean - (3*mathScore_std), mathScore_mean + (3*mathScore_std)

mathScore_list_of_data_within_1_std_deviation = [result for result in mathScore_list if result > mathScore_first_std_deviation_start and result < mathScore_first_std_deviation_end]
mathScore_list_of_data_within_2_std_deviation = [result for result in mathScore_list if result >mathScore_second_std_deviation_start and result <mathScore_second_std_deviation_end]
mathScore_list_of_data_within_3_std_deviation = [result for result in mathScore_list if result >mathScore_third_std_deviation_start and result < mathScore_third_std_deviation_end]

print("{}% of data for mathScore lies within 1 standard deviation ".format(len(mathScore_list_of_data_within_1_std_deviation)*100.0/len(mathScore_list)))
print("{}% of data for mathScore lies within 2 standard deviation ".format(len(mathScore_list_of_data_within_2_std_deviation)*100.0/len(mathScore_list)))
print("{}% of data for mathScore lies within 3 standard deviation ".format(len(mathScore_list_of_data_within_3_std_deviation)*100.0/len(mathScore_list)))

