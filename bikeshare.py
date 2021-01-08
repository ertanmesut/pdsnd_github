import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, a month, and a day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input('Enter a name of the city to analyze (chicago, new york city, washington): '))
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print ('That\'s not a valid city. Please enter a valid city (chicago, new york city, washington)')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input("Do you want to see details of a specific month?\n If yes, type month name (e.g. January, February, ... ) from within first six months, else type 'all' : "))
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print('That\'s not a valid month. Please enter a valid month (e.g. January, February, ... ) from within first six month')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("Do you want to see details of a specific day?\n If yes, type day name (e.g. Monday, Tuesday, ...), else type 'all' : "))
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print('That\'s not a valid day. Please enter a valid day')

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
    # first, load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create two new columns for future use
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filtering by month if applicable
    if month != 'all':
        # using the index of the first six months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filtering by month to create the new dataframe
        df = df[df['month'] == month]

    # filtering by day of week if applicable
    if day != 'all':
        # filtering by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is : ", df['month'].mode()[0], "\n")

    # TO DO: display the most common day of week
    print("The most common day of week  is : ", df['day_of_week'].mode()[0], "\n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is ", df['hour'].mode()[0], "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is :", df['Start Station'].mode()[0], "\n")

    # TO DO: display most commonly used end station
    print("The most commonly used end station is :", df['End Station'].mode()[0], "\n")

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip Combination'] = df['Start Station'] + " - " + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['Trip Combination'].mode()[0], "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is", df['Trip Duration'].sum(), "\n")

    # TO DO: display mean travel time
    print("The mean travel time is", df['Trip Duration'].mean(), "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print("The count of user types are: \n", user_types, "\n")

    if city != 'washington':
        # Display counts of gender
        gender = df.groupby(['Gender'])['Gender'].count()
        print("The count of genders are: \n", gender, "\n")
        # Calculate earliest, most recent, and most common year of birth
        earliest_y_o_b = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        most_rec_y_o_b = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        most_com_y_o_b = df['Birth Year'].mode()[0]
        # Display earliest, most recent, and most common year of birth
        print("The earliest year of birth is :" ,int(earliest_y_o_b), "\n")
        print("The most recent year of birth is :", int(most_rec_y_o_b), "\n")
        print("The most common year of birth is :", int(most_com_y_o_b), "\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    x = 1
    while True:
        raw_data = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw_data.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
