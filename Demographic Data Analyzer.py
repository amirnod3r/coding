import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    print(race_count)

    # What is the average age of men?
    average_age_men = df[df['sex']=='Male']
    df2 =average_age_men['age'].mean()
    print(df2)

    # What is the percentage of people who have a Bachelor's degree?
    degrees = df['education']
    per_bachelors = df[df['education']=='Bachelors']
    count_bachelors= len(per_bachelors)
    count_all_degrees= len(degrees)
    percentage_bachelors = ( count_bachelors / count_all_degrees) * 100
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    num_bachelors_50k= len(df[(df.salary == '>50K') & (df.education == 'Bachelors')])
    num_Masters_50k= len(df[(df.salary == '>50K') & (df.education == 'Masters')])
    num_Doctorate_50k= len(df[(df.salary == '>50K') & (df.education == 'Doctorate')])
    sum_50 = num_bachelors_50k + num_Masters_50k + num_Doctorate_50k
    higher_education_rich = (sum_50 / len(df.education)) * 100
    
    # What percentage of people without advanced education make more than 50K?
    
    higher_education = ['Bachelors','Masters','Doctorate']
    lower_edu = df[(~df.education.isin(higher_education)) & (df.salary == '>50K')]
    lower_education_rich = (len(lower_edu)/len(df)) * 100
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = None
    lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    percentage_1 = df[(df['hours-per-week'] == 1) & (df.salary=='>50K')]
    num_min_workers = rich_percentage= (len(percentage_1) / len(df)) * 100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = 'United-States'
    country1 = df[(df['native-country'] == 'United-States') & (df.salary == '>50K')]
    country = len(country1)
    total = len(df)
    highest_earning_country_percentage = (country / total) * 100

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
