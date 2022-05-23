import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    print ("Here you will input a city from the next list to display data \n ")
    
    # provide a list of avilable cities and ensure the user will input one of them (lower case or upper case)
    for city in CITY_DATA:
         print ("-",city, end = "\n")
    
    while True:
        city = input ("please choose a city from the above list \n ").lower()
        if city not in CITY_DATA:
            print ("please enter a correct city name from the above list \n ")
        else :
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    print ("Here you will input a month from the next list to display data \n ")
    
    # provide a list of avilable months and ensure the user will input one of them (lower case or upper case)
    for month in months:
        print("-", month, end = "\n")
    
    while True :
        month = input ("please chose month from the above list or choose all to display all months \n ").lower()
        if month != 'all' and month not in months:
            print ("please enter a correct month from the above list or choose all to display all months \n ")
        else :
            break
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print ("Here you will input a day to display data \n ")
    
    # provide a list of days and ensure the user will input one of them (lower case or upper case)
    for day in days:
        print ("-", day, end = "\n")
    
    while True :
        day = input ("please chose day from the above list or choose all to display all days \n ").lower()
        if day != 'all' and day not in days:
            print ("please enter a correct day from the above list or choose all to display all dayss \n ")
        else :
            break
        

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from the start time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if needed
    if month != 'all' :
        # use the index of the months list to get the corresponding int
        months_list = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months_list.index(month)+1
        
        # filter by month to create the new dataframe
        df = df[df["month"] == month]
        
    # filter by day of week if needed
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def display_raw_date(df):
    """
    Displays rows of dtat according to user input
    args :
       df : pandas dataframe containing city data filtered by day and month returned from load_data() function
    
    returns:
        5 lines of the dataframe if the user choes yes and so on 
    """
    j = 0
    valid_descions = ["yes","no"]
    while True :       # to ensure a valid input
        user_descion = input("would you like to see raw data or not , please answer yes or no:- ").lower()
        while True :    ## if the user choes yes the function will display 5 lines and so on
            if user_descion == "yes":
                print(df[j:j+5])
                user_descion = input("would you like to see the next 5 raw data or not , please answer yes or no:- ").lower()
                j +=5
            else:
                break
        if user_descion not in valid_descions :
            print ("please enter a correct answer \n ") 
        else:
            break
    
    
def time_stats(df):
    """
        Displays statistics on the most frequent times of travel.
        
       args :
           df : pandas dataframe containing city data filtered by day and month returned from load_data() function
    
       return :
           the most common month, the most common day, and the most common start hour 
    
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month_number = df["month"].mode()[0]
    common_month_name = calendar.month_name[common_month_number]
    print ("the most common month is : ", common_month_name)

    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print ("the most common day is : ", common_day)
    
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour =df['hour'].mode()[0]
    print ("the most common start hour is : ", common_start_hour)                                       
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
        Displays statistics on the most popular stations and trip.
    
         args :
            df : pandas dataframe containing city data filtered by day and month returned from load_data() function
    
       return :
            most commonly used start station, most commonly used end station, most frequent combination of start station and end station trip 
    
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print ("the common start station : ",common_start_station)
    
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print ("the common end station : ",common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_stations = df.groupby(['Start Station','End Station']).size().sort_values(ascending = False).head(1)
    print ("the most frequent combination of start station and end station trip : ",common_start_end_stations)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
        Displays statistics on the total and average trip duration.
        
        args :
            df : pandas dataframe containing city data filtered by day and month returned from load_data() function
    
       return :
           total travel time and mean travel time
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time_seconds = df['Trip Duration'].sum()     #display the total travel time in second
    
    # to diplay the total travel time in simple readable format
    total_hours = total_travel_time_seconds//3600            #take the hours      
    total_mins = (total_travel_time_seconds % 3600)//60      #take the minutes
    total_seconds = (total_travel_time_seconds % 3600)%60     # the reminder is the seconds
    print ("the total travel time : ",total_hours , "hours ",total_mins ,"minutes",total_seconds ,"seconds" )
    
    # TO DO: display mean travel time
    mean_travel_time_seconds = df['Trip Duration'].mean()       #display the mean travel time in second 
    
     # to diplay the mean travel time in simple readable format
    mean_hours = mean_travel_time_seconds//3600            #take the hours      
    mean_mins = (mean_travel_time_seconds % 3600)//60      #take the minutes
    mean_seconds = (mean_travel_time_seconds % 3600)%60     # the reminder is the seconds
    print ("the mean travel time : ",mean_hours , "hours ",mean_mins ,"minutes",mean_seconds ,"seconds" )
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
        Displays statistics on bikeshare users.
        
        args :
            df : pandas dataframe containing city data filtered by day and month returned from load_data() function
    
       return :
           counts of user types and (counts of gender, earliest, most recent, and most common year of birth) for chicago and new york city
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df["User Type"].value_counts()
    print("the counts of user types :- \n", counts_user_types.to_string());
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print ("counts of gender :- \n",gender_count.to_string())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df :
        earliest_birth_year = int(df['Birth Year'].min())
        print("the earliest birth year : ", earliest_birth_year)
        
        most_recent_birth_year = int(df['Birth Year'].max())
        print("the most recent birth year : ", most_recent_birth_year)
        
        common_birth_year = int(df['Birth Year'].mode()[0])
        print("the most common birth year : ", common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_raw_date(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

