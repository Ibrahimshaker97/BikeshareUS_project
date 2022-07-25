import calendar
import time 
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city= input ('Choose one of the cities (chicago, new york city, washington): ').lower()
        if city not in CITY_DATA:
            print("\ninvalid city Choose one of the cities(chicago, new york city, washington)\n")
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Choose a month from January --> June or type all to view all: ').lower()
        months =['january', 'february', 'march','april', 'may' , 'joune']
        if month != 'all' and month not in months:
            print('\ninvalid month name check spilling or write the full month name\n')
        else:
            break    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('please enter a day as (sat,sun,mon,....,etc) or type all to view all: ').lower()
        days=['wed', 'thu', 'fri', 'sat', 'sun', 'mon', 'tue']
        if day !='all' and  day not in days:
            print('\nplease enter a valid day name\n')
        else:
            break

    print('-'*50)
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
    df=pd.read_csv(CITY_DATA[city])
    df=df.rename(columns={'Start Time':'ST'})
    df['ST']= pd.to_datetime(df['ST'])
    df['month']= df['ST'].dt.month
    df['day']=df['ST'].dt.day_name().str[:3]
    df['hour']=df['ST'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march','april', 'may' , 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common months
    mcm= df['month'].mode()[0]
    print("The most common month: ",calendar.month_abbr[mcm])
    # TO DO: display the most common day of week
    mcd= df['day'].mode()[0]
    print("The most common day of week: {}".format(mcd))
    # TO DO: display the most common start hour
    mcsh=df['hour'].mode()[0]
    print("The most common start hour: {}".format(mcsh))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mcsst=df['Start Station'].mode()[0]
    print('The most commonly used start station is : {}'.format(mcsst))
    print()
    # TO DO: display most commonly used end station
    mcest=df['End Station'].mode()[0]
    print('The most commonly used end station is : {}'.format(mcest))
    print()
    # TO DO: display most frequent combination of start station and end station trip
    frequent_stations = df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most frequent start and end station: ',frequent_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    # TO DO: display mean travel time
    avg_trip=df['Trip Duration'].mean()
    print('The Total trip duration: {} Sec\nor {} Hour \nAverage trip duration: {} Sec \nor {} Hour'.format(total_time,total_time/3600,avg_trip,avg_trip/3600))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types.to_string())
    print()
    # TO DO: Display counts of gender
    if ('Birth Year') in df.columns:
        gender = df['Gender'].value_counts()
        print(gender.to_string())
        print()
    # TO DO: Display earliest, most recent, and most common year of birth
        ey=df['Birth Year'].min().astype(int)
        oy=df['Birth Year'].max().astype(int)
        cy=df['Birth Year'].mode()[0].astype(int)
        print('Earliest Year: {}\nMost recent: {}\nMost common: {}'.format(ey,oy,cy))
    else:
        print('Gender data: NA\nBirth Year data: NA')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def Raw_Data(df):
    """display the raw data from csv file"""
    n=0
    respond=input('Do you want to see raw data Yes or No: ').lower()
    while True:
        
        if respond == 'yes':

            print(df[n:n+5])    
            print()
            respond=input('Do you want to see next set of raw data Yes or No: ').lower()
            n=n+5
        elif respond != 'yes':   
            break
    print('-'*50)    



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        Raw_Data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
