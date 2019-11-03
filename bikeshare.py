#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    # """
    # Asks user to specify a city, month, and day to analyze.

    # Returns:
    #     (str) city - name of the city to analyze
    #     (str) month - name of the month to filter by, or "all" to apply no month filter
    #     (str) day - name of the day of week to filter by, or "all" to apply no day filter
    # """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("0: chicago\n1: new york city\n2: washington")

    city_id = input("please to choose one index to start  analysis of data, index:")
    citys = ['chicago', 'new york city', 'washington']

    # TO DO: get user input for month (all, january, february, ... , june)
    print("0: All\n1: January\n2: February\n3: March\n4: April\n5: May\n6: June")

    month_id = input("please to choose one index to start  analysis of data, index:")
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("0: All\n1: Monday\n2: Tuesday\n3: Wednesday\n4: Thursday\n5: Friday\n6: Saturday\n7: Sunday")


    day_id = input("please to choose one index to start  analysis of data, index:")
    days = ['all', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    print('-'*40)
    return citys[int(city_id)], months[int(month_id)], days[int(day_id)]


def load_data(city, month, day):
    # """
    # Loads data for the specified city and filters by month and day if applicable.

    # Args:
    #     (str) city - name of the city to analyze
    #     (str) month - name of the month to filter by, or "all" to apply no month filter
    #     (str) day - name of the day of week to filter by, or "all" to apply no day filter
    # Returns:
    #     df - Pandas DataFrame containing city data filtered by month and day
    # """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city]).dropna(axis = 0)
    

    # # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    # """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print("The most common month is : " + months[df['Start Time'].dt.month.mode()[0]] + ".")

    # TO DO: display the most common day of week

    print("The most common Weekday Name is : " + df['Start Time'].dt.weekday_name.mode()[0] + ".")

    # TO DO: display the most common start hour

    print("The most common Start Hour is : " + str(df['Start Time'].dt.hour.mode()[0]) + ".")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    # """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print("The most common Start Station is : " + df['Start Station'].mode()[0] + ".")

    # TO DO: display most commonly used end station

    print("The most common End Station is : " + df['End Station'].mode()[0] + ".")

    # TO DO: display most frequent combination of start station and end station trip
    df["combination"] = "Start Station:(" + df['Start Station'] + ") and End Station:(" + df['End Station'] + ")"
    print("The most frequent combination of the trip is: \n    " + df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total Trip Duration is: " + str(df["Trip Duration"].sum()) + "s.")

    # TO DO: display mean travel time
    print("The average Trip Duration is: %.2fs." % df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The most common User Types is : " + df['User Type'].mode()[0] + ".")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("The most common gender is : " + df['Gender'].mode()[0] + ".")
    else:
        print("The " + city + "'s dataframe doesn't have column named Gender.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("The most common Birth Year is : " + str(df['Birth Year'].mode()[0])[:-2] + ".")
        print("The most min Birth Year is : " + str(df['Birth Year'].min())[:-2] + ".")
        print("The most max Birth Year is : " + str(df['Birth Year'].max())[:-2] + ".")
    else:
        print("The " + city + "'s dataframe doesn't have column named Birth Year.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)

        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
