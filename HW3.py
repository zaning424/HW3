import csv
import glob
import os
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

purpose = []
def merge_csv():
    csv_list = glob.glob('*.csv')
    for i in csv_list:
        df = open(i, 'rb').read()
        for row in df:
            del row
            break
        with open('result.csv','ab') as file:
            file.write(df)


def find_name():
    with open('result.csv') as companys:
        reader = csv.DictReader(companys)
        name = [row['Name'] for row in reader]
    return name


def find_purpose():
    with open('result.csv') as companys2:
        reader2 = csv.DictReader(companys2)
        purpose = [row['Purpose'] for row in reader2]
    return purpose


def find_score(list):
    score = []
    for elem in list:
        if elem == 'Purpose':
            continue
        analyzer = SentimentIntensityAnalyzer()
        score.append(analyzer.polarity_scores(elem)['compound'])
    return score


def score_sort(name, purpose):
    score_list = find_score(purpose)
    # print(len(score_list))
    # print(len(name))
    d = {}
    i = 0
    j = 0
    while True:
        if name[i] == 'Name':
            i += 1
            continue
        d[name[i]]= score_list[j]
        i += 1
        j += 1
        if i == len(name) -1:
            break
    sorted_score = sorted(d.items(), key = lambda x: x[1])
    return sorted_score


def best_company(list):
    return list[0:10]


def worst_company(list):
    return list[-11:-1]
# print(len(d))
# print(len(sorted_score))
# print(sorted_score[0:9])
# print(sorted_score[-10:-1])

if __name__ == "__main__":
    merge_csv()
    name1 = find_name()
    purpose1 = find_purpose()
    Sorted_list1 = score_sort(name1, purpose1)
    print(best_company(Sorted_list1))
    print(worst_company(Sorted_list1))


#  Worst
# [('Green, Holland and Bennett', -0.6486),
# ('Willis and Sons', -0.6486),
# ('Andrews Group', -0.6486),
# ('Mcclain, Mccarthy and Lozano', -0.6486),
# ('Huffman, Norton and Cantu', -0.6486),
# ('Washington-Mccormick', -0.6486),
# ('Delgado Ltd', -0.2732),
# ('Cruz, Powell and Deleon', -0.1027),
# ('Turner Group', -0.1027)]
# ('Delgado Group', -0.1027)

# Best
#[('Powell-Hamilton', 0.7184)
# ('Diaz-Ross', 0.7269),
# ('Jackson Group', 0.7269),
# ('Hill-Martin', 0.7351),
# ('Hall, Heath and Perez', 0.743),
# ('Cabrera, Levine and Underwood', 0.7579),
# ('Barajas LLC', 0.765),
# ('Roberts-Huff', 0.7717),
# ('Stokes and Sons', 0.7845),
# ('Singh PLC', 0.8271)]
