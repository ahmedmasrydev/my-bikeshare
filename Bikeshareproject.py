#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
    print('Hello! Let\'s explore some US bikeshare data! ')

    city=input('Please select the name of city between "Chicago,New york city or Washington ": ')
    city=city.lower()
    while city not in CITY_DATA.keys() :
           print('Missing!')
           city=input('Please renter the name of chosen city above: ')

    monthes=['all', 'january', 'february','march','april','may' , 'june']
    month=input('Please enter month between january and june only or select "all" for all: ')
    month=month.lower()
    while month not in monthes :
          print('Missing!')
          month=input('Please renter chosen month mentioned or "all"for all: ')

    days=['all','monday','tuesday','wendesday','Thursday','friday','satarday','sunday']
    day=input('Please enter a day from week or "all"for all: ')
    day=day.lower()
    while day not in days:
         print('Missing!')
         day=input('Please renter a day from week or "all"fo all: ')
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
    df= pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    common_month = df['month'].mode()[0]

    print('Most common month:',common_month)
    common_day = df['day_of_week'].mode()[0]

    print('Most common day :',common_day)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print('Most common hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    common_start_station=df['Start Station'].mode()[0]
    print('Most common used start station: ',common_start_station)

    common_end_station=df['End Station'].mode()[0]
    print('Most common used end station: ',common_end_station)

    common_start_station+'AND'+common_end_station
    print('Most frequent combination of start station and end station trip: ',common_start_station+' AND '+common_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel=df['Trip Duration'].sum()
    print('Total travel time in days:  ',total_travel/(60*60*24),'Day')

    mean_travel=df['Trip Duration'].mean()
    print('Mean travel time in minutes: ',mean_travel/60,'Min.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(user_types)

    if 'Gender' in df.columns:
        gender_types= df['Gender'].value_counts()
        print(gender_types)
    else:
        print('Gender data is missing for this city')


    if 'Birth Year' in df.columns:
        Earliest_year=df['Birth Year'].min()
        print('Earliest year: ',Earliest_year)
        Recent_year=df['Birth Year'].max()
        print('Recent year: ',Recent_year)
        Most_common_year_of_birth=df['Birth Year'].mode()[0]
        print('Most common year of birth: ',Most_common_year_of_birth)
    else:
        print('Birth Year data is missing for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    """
    Display contents of the CSV file to the display as requested by
    the user.
    """

    start_loc = 0
    end_loc = 5

    display_active = input("Do you want to see the raw data?: ").lower()

    if display_active == 'yes':
        while end_loc <= df.shape[0] - 1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            end_display = input("Do you wish to continue?: ").lower()
            if end_display == 'no':
                break
def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:
