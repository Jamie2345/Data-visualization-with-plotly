'''

    My code after completing the data visualization portion of Eric Matthes Python Crash Course A HANDS-ON , PROJECT-BASED
    INTRODUCTION TO PROGRAMMING

'''

# if I have a # in front of import its used in that class but ive already imported it
# above imports is the class you can find that import being used in

# GRAPHS (class: LineGraph, class: ScatterGraph & class: Styles)

import matplotlib.pyplot as plt  # used to plot graphs

# RANDOM WALK (class: RandomWalk)

from random import choice  # used to plot random walk

# INTERACTIVE DATA (class: PlotlyDice

from random import randint  # used to roll dice
from plotly.graph_objs import Bar, Layout  # used to make interactive graphs
from plotly import offline

# TEMPERATURE DATA (class: DownloadingData)

import csv  # used to read csv data
from datetime import datetime

# EARTHQUAKE DATA PROJECT (class: JsonData)

import json  # used to read json files
# from plotly.graph_objs import Scattergeo        # used to build world map I used a nested dict instead of import
# from plotly.graph_objs import Layout
# from plotly import offline

# WORKING WITH APIs (class: WorkingWithAPIs)

import requests
from operator import itemgetter


# Any text in green is info directly from the crash course that I thought was helpful.  (apart from list of classes)
# info is located in corresponding classes in the functions they relate to

# example of how to view each bit of info

# c = LineGraphs()
# c.better_line_graph()


class LineGraphs:

    def line_graph(self):
        squares = [1, 4, 9, 16, 25]  # data to plot
        fig, ax = plt.subplots()  # .subplots() can generate one or more plots in the same figure
        ax.plot(squares)  # ax represents a single plot in the figure .plot tries to plot the data
        plt.show()  # used to show the graph on screen (note you can zoom navigate and save plot images)

        '''
        The variable fig represents the entire figure or collection of plots that
        are generated. The variable ax represents a single plot in the figure and is
        the variable we’ll use most of the time.
        '''

    def better_line_graph(self):
        squares = [1, 4, 9, 16, 25]
        fig, ax = plt.subplots()
        ax.plot(squares, linewidth=3)  # sets thickness of line

        # Set chart title and label axes.

        ax.set_title("Square Numbers", fontsize=24)
        ax.set_xlabel("Value", fontsize=14)
        ax.set_ylabel("Square of Value", fontsize=14)

        # Set size of tick labels.

        ax.tick_params(axis='both', labelsize=14)

        # show graph
        plt.show()

        '''
        the method tick_params() styles the tick marks.
        The arguments shown here affect the tick marks on both the x and y-axes
        (axis='both') and set the font size of the tick mark labels to 14 (labelsize=14).
        '''

    def correct_line_graph(self):
        '''
        But now that we can read the chart better, we see that the data is not plotted correctly. Notice at the end of the graph that the square of 4.0 is shown
        as 25! Let’s fix that.
        When you give plot() a sequence of numbers, it assumes the first data
        point corresponds to an x-coordinate value of 0, but our first point corresponds to an x-value of 1. We can override the default behavior by giving
        plot() the input and output values used to calculate the squares:
        '''

        input_values = [1, 2, 3, 4, 5]
        squares = [1, 4, 9, 16, 25]
        fig, ax = plt.subplots()
        ax.plot(input_values, squares, linewidth=3)

        ax.set_title("Square Numbers", fontsize=24)
        ax.set_xlabel("Value", fontsize=14)
        ax.set_ylabel("Square of Value", fontsize=14)

        ax.tick_params(axis='both', labelsize=14)

        plt.show()


class Styles:

    def built_in_styles(self):
        '''
        Matplotlib has a number of predefined styles available, with good starting
        settings for background colors, gridlines, line widths, fonts, font sizes, and
        more that will make your visualizations appealing without requiring much
        customization.
        '''

        # To view all available styles you can do print(plt.style.available)

        input_values = [1, 2, 3, 4, 5]
        squares = [1, 4, 9, 16, 25]

        plt.style.use('seaborn')  # setting the style
        fig, ax = plt.subplots()
        ax.plot(input_values, squares, linewidth=3)

        ax.set_title("Square Numbers", fontsize=24)
        ax.set_xlabel("Value", fontsize=14)
        ax.set_ylabel("Square of Value", fontsize=14)

        ax.tick_params(axis='both', labelsize=14)

        plt.show()

    def print_all_styles(self):
        styles = plt.style.available
        print("All styles are {}".format(styles))


class ScatterGraphs():
    def plot_single_point(self):
        '''
        To plot a single point, use the scatter() method. Pass the single (x, y)
        values of the point of interest to scatter() to plot those values:
        '''

        plt.style.use('seaborn')  # setting style
        fig, ax = plt.subplots()
        ax.scatter(2, 4, s=200)  # plots a point  # s=200 sets the size of the dot

        # Set chart title and label axes.

        ax.set_title("Square Numbers", fontsize=24)
        ax.set_xlabel("Value", fontsize=14)
        ax.set_ylabel("Square of Value", fontsize=14)

        # Set size of tick labels.
        ax.tick_params(axis='both', which='major', labelsize=14)

        plt.show()

    def plot_series_of_points(self):
        '''
        To plot a series of points, we can pass scatter() to separate lists of x and y values, like this:
        '''

        x_values = [1, 2, 3, 4, 5]
        y_values = [1, 4, 9, 16, 25]

        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.scatter(x_values, y_values, s=200)

        ax.set_title("Square Numbers", fontsize=24)
        ax.set_xlabel("Value", fontsize=14)
        ax.set_ylabel("Square of Value", fontsize=14)

        ax.tick_params(axis='both', which='major', labelsize=14)

        plt.show()

    def plot_1000_points(self):
        # Note Python can plot 1000 points as easily as it plots 5 points

        x_values = range(1, 1001)
        y_values = [x ** 2 for x in x_values]

        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.scatter(x_values, y_values, s=10)

        ax.set_title("Square Numbers", fontsize=24)
        ax.set_xlabel("Value", fontsize=14)
        ax.set_ylabel("Square of Value", fontsize=14)

        ax.tick_params(axis='both', which='major', labelsize=14)

        plt.show()

        '''
        We start with a range of x-values containing the numbers 1 through
        1000. Next, a list comprehension generates the y-values by looping
        through the x-values (for x in x_values), squaring each number (x**2) and
        storing the results in y_values.
        '''

    def set_colour(self):
        x_values = [1, 2, 3, 4, 5]
        y_values = [1, 4, 9, 16, 25]

        fig, ax = plt.subplots()
        ax.scatter(x_values, y_values, c="red", s=50)  # c="red" sets colour to blue

        ax.set_title("Set Colours")

        plt.show()

    def set_colour_rgb(self):
        '''
        You can also define custom colors using the RGB color model. To define
        a color, pass the c argument a tuple with three decimal values
        (one each for red, green, blue in that order) using decimals from 0 to 1.
        The following graph uses green dots>
        '''

        x_values = [1, 2, 3, 4, 5]
        y_values = [1, 4, 9, 16, 25]

        fig, ax = plt.subplots()
        ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=50)  # c="red" sets colour to blue

        ax.set_title("Set RGB Colours")

        plt.show()

    def colour_map(self):
        '''
        A colormap is a series of colors in a gradient that moves from a starting to
        an ending color. You use colormaps in visualizations to emphasize a pattern
        in the data. For example, you might make low values a light color and high
        values a darker color
        '''

        '''
        The pyplot module includes a set of built-in colormaps. To use one of
        these colormaps, you need to specify how pyplot should assign a color to
        each point in the data set. Here’s how to assign each point a color based
        on its y-value:
        '''

        x_values = range(1, 1001)
        y_values = [x ** 2 for x in x_values]

        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.scatter(x_values, y_values, c=y_values, cmap=plt.get_cmap("Blues"), s=10)

        ax.set_title("Square Numbers", fontsize=24)
        ax.set_xlabel("Value", fontsize=14)
        ax.set_ylabel("Square of Value", fontsize=14)

        ax.tick_params(axis='both', which='major', labelsize=14)

        plt.show()

        # You can see all the colour maps available at https://matplotlib.org/

        # Go to Examples, scroll down to colour, and click Colourmap reference

        '''
        We pass the list of y-values to c, and then tell pyplot which colormap to
        use using the get_cmap argument. This code colors the points with lower y-values
        light blue and colors the points with higher y-values dark blue.
        c = ScatterGraphs()
        '''

    def save_auto(self):
        print("To get your program to automatically save to a file you can change plt.show() to plt.savefig()")

        '''
        plt.savefig('squares_plot.png', bbox_inches='tight')
        
        The first argument is a filename for the plot image, which will be saved
        in the same directory as scatter_squares.py. The second argument trims extra
        whitespace from the plot. If you want the extra whitespace around the plot,
        just omit this argument.
        '''


class CubesChallenge:

    # This challenge was to create a plot for first 5 cubic numbers then a plot for first 5000 cubic numbers

    # Then to add a colourmap

    def first_5(self):
        x_values = range(1, 6)
        y_values = [x ** 3 for x in x_values]

        plt.style.use('dark_background')
        fig, ax = plt.subplots()
        ax.scatter(x_values, y_values, c="red", s=20)

        ax.set_title("First 5 Cubic Numbers", fontsize=22)
        ax.set_xlabel("Numbers", fontsize=12)
        ax.set_ylabel("Cubic Values", fontsize=12)

        ax.tick_params(axis="both", which="major", labelsize=12)

        plt.show()

    def first_5000(self):
        x_values = range(1, 5001)
        y_values = [x ** 3 for x in x_values]

        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.scatter(x_values, y_values, c=(0.5, 0.5, 0.5), s=20)

        ax.set_title("First 5 Cubic Numbers", fontsize=22)
        ax.set_xlabel("Numbers", fontsize=12)
        ax.set_ylabel("Cubic Values", fontsize=12)

        ax.tick_params(axis="both", which="major", labelsize=12)

        plt.show()

    def colourmap_5000(self):
        x_values = range(1, 5001)
        y_values = [x ** 3 for x in x_values]

        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.scatter(x_values, y_values, c=y_values, cmap=plt.get_cmap("Greys"), s=25)

        ax.set_title("Colourmap for first 5000 cubic numbers", fontsize=20)
        ax.set_xlabel("Numbers", fontsize=12)
        ax.set_ylabel("Cubic Values", fontsize=12)

        ax.tick_params(axis='both', which='major', labelsize=12)

        plt.show()


class RandomWalk:
    def __init__(self, num_points):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([1, 2, 3, 4, 5])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([1, 2, 3, 4, 5])
            y_step = y_direction * y_distance

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

        plt.style.use('classic')
        fig, ax = plt.subplots()
        ax.scatter(self.x_values, self.y_values, c="red", s=15)

        ax.set_title("Your Random Walk")

        plt.show()

    def multiple_walks(self):
        while True:
            rw = RandomWalk(self.num_points)
            rw.fill_walk()

            keeprunning = input("Make another walk? (y/n): ")
            if keeprunning == 'y':
                continue
            break

    def styled_walk(self, size=15):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([1, 2, 3, 4, 5])
            x_step = x_direction * x_distance  # where to go to

            y_direction = choice([1, -1])
            y_distance = choice([1, 2, 3, 4, 5])
            y_step = y_direction * y_distance

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

        plt.style.use('classic')
        fig, ax = plt.subplots(figsize=(15, 9))  # figsize fills the screen
        point_numbers = range(self.num_points)
        ax.scatter(self.x_values, self.y_values, c=point_numbers, cmap=plt.get_cmap('Greys'), s=size,
                   edgecolors='none')  # edgecolors removes the outline around the dots

        ax.set_title("Your Random Walk")

        # Emphasize the first and last points.

        ax.scatter(0, 0, c='green', edgecolors='none', s=100)
        ax.scatter(self.x_values[-1], self.y_values[-1], c='red', edgecolors='none', s=100)

        # Remove the x and y axis

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        plt.show()

        '''
        we use range() to generate a list of numbers equal to the number
        of points in the walk. Then we store them in the list point_numbers, which
        we’ll use to set the color of each point in the walk.
        '''


class RandomChallenge:
    # This sections challenges were

    '''
    15-3. Molecular Motion: Modify rw_visual.py by replacing plt.scatter() with
    plt.plot(). To simulate the path of a pollen grain on the surface of a drop of
    water, pass in the rw.x_values and rw.y_values, and include a linewidth argument. Use 5000 instead of 50,000 points.
    '''

    # 15-4 was just to modify values in random walk class eg. make distance [1, 2, 3, 4, 5, 6, 7, 8] instead of 1 to 5

    '''
    15-5. Refactoring: The fill_walk() method is lengthy. Create a new method
    called get_step() to determine the direction and distance for each step, and
    then calculate the step. You should end up with two calls to get_step() in
    fill_walk():
    '''

    def __init__(self, points):
        self.points = points
        self.x_values = [0]
        self.y_values = [0]

    def MolecularMotion(self):
        while len(self.x_values) < self.points:
            x_direction = choice([1, -1])
            x_distance = choice([1, 2, 3, 4, 5])
            x_growth = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([1, 2, 3, 4, 5])
            y_growth = y_direction * y_distance

            x = self.x_values[-1] + x_growth
            y = self.y_values[-1] + y_growth

            self.x_values.append(x)
            self.y_values.append(y)

        plt.style.use('classic')
        fig, ax = plt.subplots(figsize=(15, 9))
        ax.plot(self.x_values, self.y_values, c='green', linewidth=0.3)
        ax.set_title("Path of pollen grain", fontsize=12)

        # Removing axes

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        plt.show()

    # Refactoring

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([1, 2, 3, 4, 5])

        step = direction * distance

        return step

    def fill_walk_refactored(self, size=5):
        while len(self.x_values) < self.points:
            x_step = self.get_step()
            y_step = self.get_step()

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

        plt.style.use('classic')
        point_numbers = range(self.points)
        fig, ax = plt.subplots(figsize=(15, 9))
        ax.scatter(self.x_values, self.y_values, c=point_numbers, cmap="Greys", s=size, edgecolors='none')

        # Title

        ax.set_title("Fill walk refactored version")

        # First and last points

        ax.scatter(0, 0, c='green', s=100, edgecolors='none')
        ax.scatter(self.x_values[-1], self.y_values[-1], c='red', s=100, edgecolors='none')

        # Removing axis

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        plt.show()


class PlotlyDice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):  # Simple func to roll the dice
        return randint(1, self.sides)

    def roll1_and_plot(self, rolls=100):
        results = []
        die = PlotlyDice()
        for i in range(rolls):
            rolled_die = die.roll()
            results.append(rolled_die)  # appends the result of .roll to a list of all the results

        # analyse results
        frequencies = []
        for e in range(1, die.sides + 1):
            frequency = results.count(e)  # counts how many times how many times each number appeared
            frequencies.append(frequency)

        # visualise results

        x_values = list(range(1, die.sides + 1))
        data = [Bar(x=x_values, y=frequencies)]

        x_axis_config = {'title': 'Result'}
        y_axis_config = {'title': 'Result Frequencies'}
        my_layout = Layout(title='Results of rolling a dice with {} sides {} times'.format(self.sides, rolls),
                           xaxis=x_axis_config, yaxis=y_axis_config)

        offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

    def roll_multiple_and_plot(self, amount_of_die=2, rolls_each_die=1000, sides=6):
        all_die_name = []
        for r in range(1, amount_of_die + 1):  # creating names for objects
            dice_name = 'die' + str(r)
            all_die_name.append(dice_name)

        for i in range(len(all_die_name)):  # initializing all objects
            all_die_name[i] = PlotlyDice(sides)

        # Rolling and storing the total of all rolls eg  3, 6, 4 = 13 it ill store 13
        results = []
        for roll_num in range(rolls_each_die):  # loops as many times as rolls each die is
            result = 0
            for i in range(len(all_die_name)):
                result += all_die_name[i].roll()
            results.append(result)

        # Analyse the results
        frequencies = []
        max_result = len(all_die_name) * sides  # if I have a 3 die all 6 sided the highest value is 3 * 6 = 18
        for number in range(len(all_die_name), max_result + 1):  # if I have 3 die the lowest value possible is 3
            frequency = results.count(number)
            frequencies.append(frequency)

        # Visualise the results

        x_values = list(range(len(all_die_name), max_result + 1))
        data = [Bar(x=x_values, y=frequencies)]

        x_axis_config = {'title': 'Result', 'dtick': 1}
        y_axis_config = {'title': 'Result Frequencies'}
        my_layout = Layout(
            title="Results of rolling {} dice with {} sides {} times".format(len(all_die_name), sides, rolls_each_die),
            xaxis=x_axis_config, yaxis=y_axis_config)

        offline.plot({'data': data, 'layout': my_layout}, filename='multiple dice.html')


class DownloadingData:
    # This won't work for you as the csv isn't on your computer

    def plot_month_temp(self):
        filename = r'C:\Users\jamie\OneDrive\Documents\sitka_weather_data.csv'  # https://github.com/ehmatthes/pcc_2e/blob/master/chapter_16/the_csv_file_format/data/sitka_weather_07-2018_simple.csv
        # to download select raw, copy text and paste into notepad then save as a csv
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for index, column_header in enumerate(header_row):
                print(index, column_header)

            # Get temperatures from this file

            dates, highs = [], []
            for row in reader:
                high = int(row[5])
                current_daytime = datetime.strptime(row[2], '%Y-%m-%d')
                highs.append(high)
                dates.append(current_daytime)

            # plot the data

            plt.style.use('seaborn')
            fig, ax = plt.subplots(linewidth=3, figsize=(15, 9))
            ax.plot(dates, highs, c='black')

            # Format Plot
            ax.set_title("Daily high temperatures, July 2018", fontsize=24)
            ax.set_ylabel('Temperature (F)', fontsize=17)
            ax.set_xlabel('', fontsize=7)
            fig.autofmt_xdate()

            ax.tick_params(axis='both', which='major', labelsize=16)

            plt.show()

    def plot_year_temp(self):
        filename = r'C:\Users\jamie\OneDrive\Documents\course_data\sitka_year_data.csv'  # https://github.com/ehmatthes/pcc_2e/blob/master/chapter_16/the_csv_file_format/data/sitka_weather_2018_simple.csv

        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for index, column_header in enumerate(header_row):
                print(index, column_header)

            # Get temperatures

            dates, temp_high, temp_low = [], [], []
            for row in reader:
                high = int(row[5])
                low = int(row[6])
                date = datetime.strptime(row[2], '%Y-%m-%d')
                temp_high.append(high)
                temp_low.append(low)
                dates.append(date)

            # Plotting data

            plt.style.use('seaborn')
            fig, ax = plt.subplots(figsize=(15, 9))
            ax.plot(dates, temp_high, c='black', linewidth=1, alpha=0.8)
            ax.plot(dates, temp_low, c='blue', linewidth=1, alpha=0.8)
            plt.fill_between(dates, temp_high, temp_low, facecolor='blue', alpha=0.1)

            # Formatting plot

            ax.set_title("Daily High And Low Temperature Of {} In 2018".format(row[1]))
            ax.set_xlabel("", fontsize=8)
            ax.set_ylabel("Temperature (F)", fontsize=17)
            fig.autofmt_xdate()

            ax.tick_params(axis='both', which='major', labelsize=14)

            plt.show()


class JsonData:
    def earthquake_data(self):
        '''
        Let’s start by loading the data and displaying it in a format that’s easier
        to read. This is a long data file, so instead of printing it, we’ll rewrite the
        data to a new file. Then we can open that file and scroll back and forth easily through the data:
        '''

        filename = r'C:\Users\jamie\OneDrive\Documents\course_data\earthquake_data.JSON'  # do the same as plot_month but put .JSON instead of .CSV

        # Explore the structure of the data

        with open(filename) as f:
            all_eq_data = json.load(f)

        readable_file = r'C:\Users\jamie\OneDrive\Documents\course_data\readable_eq_data.JSON'  # I would recommend opening this in your IDE not internet explorer
        with open(readable_file, 'w') as e:  # you need to save it first
            json.dump(all_eq_data, e, indent=4)

        # Making a list of earthquakes
        all_eq_dicts = all_eq_data['features']

        # Getting title
        json_title = all_eq_data['metadata']['title']
        '''
        Extracting Location Data
        
        The location data is stored under the key "geometry". Inside the geometry
        dictionary is a "coordinates" key, and the first two values in this list are the
        longitude and latitude. Here’s how we’ll pull this data:
        '''

        mags, lons, lats, hover_text = [], [], [], []
        for eq_dict in all_eq_dicts:
            mag = eq_dict['properties']['mag']
            lon = eq_dict['geometry']['coordinates'][
                0]  # coordinates are stored in geometry and longitude is first item
            lat = eq_dict['geometry']['coordinates'][1]  # better explination below
            title = eq_dict['properties']['title']
            mags.append(mag)
            lons.append(lon)
            lats.append(lat)
            hover_text.append(title)

        '''
        We make empty lists for the longitudes and latitudes. The code eq_dict
        ['geometry'] accesses the dictionary representing the geometry element of
        the earthquake u. The second key, 'coordinates', pulls the list of values
        associated with 'coordinates'. Finally, the 0 index asks for the first value in
        the list of coordinates, which corresponds to an earthquake’s longitude.
        '''

        # Plotting world map data easy way but doesn't look as good

        '''
        data = [Scattergeo(lon=lons, lat=lats)]
        my_layout = Layout(title='Global Earthquakes')

        fig = {'data' : data, 'layout' : my_layout}
        offline.plot(fig, filename='global_earthquakes.html')
        '''
        # Plotting world map data but looks good

        data = [{
            'type': 'scattergeo',
            'lon': lons,
            'lat': lats,
            'text': hover_text,
            'marker': {
                'size': [5 * mag for mag in mags],
                'color': mags,
                'colorscale': 'Viridis',
                'reversescale': True,
                'colorbar': {'title': 'Magnitude'}
            }
        }]

        '''
        Plotly offers a huge variety of customizations you can make to a data
        series, each of which can be expressed as a key-value pair. Here we’re using
        the key 'marker' to specify how big each marker on the map should be u.
        We use a nested dictionary as the value associated with 'marker', because
        you can specify a number of settings for all the markers in a series.
        We want the size to correspond to the magnitude of each earthquake. But if
        we just pass in the mags list, the markers would be too small to easily see the size
        differences. We need to multiply the magnitude by a scale factor to get an appropriate marker size.
        '''

        # plotting the rest of the graph

        my_layout = Layout(title=json_title)

        fig = {'data': data, 'layout': my_layout}
        offline.plot(fig, filename='global_earthquakes.html')

        '''
        Be sure to update the filename so you’re using the 30-day data set u.
        All the significant changes here occur in the 'marker' dictionary, because
        we’re only modifying the markers’ appearance. The 'color' setting tells
        Plotly what values it should use to determine where each marker falls on
        the colorscale v. We use the mags list to determine the color that’s used.
        The 'colorscale' setting tells Plotly which range of colors to use: 'Viridis'
        is a colorscale that ranges from dark blue to bright yellow and works well
        for this data set w. We set 'reversescale' to True, because we want to use
        bright yellow for the lowest values and dark blue for the most severe earthquakes x. The 'colorbar' setting allows us to control the appearance of
        the colorscale shown on the side of the map. Here we title the colorscale
        'Magnitude' to make it clear what the colors represent x.
        '''


class FireData:
    '''
    Using the data processing work from the first part of
    this chapter and the mapping work from this section, make a map that shows
    which parts of the world are affected by fires.
    '''

    def fire_data_csv(self):
        filename = r'C:\Users\jamie\OneDrive\Documents\course_data\Global_fires_24hrs.csv'
        max_loops = 10000  # used to keep data short not whole file

        # opening the file and getting headers
        with open(filename) as f:
            reader = csv.reader(f)
            header_text = next(reader)

            # getting indexes of data
            for index, column_header in enumerate(header_text):
                print(index, column_header)

            # keeping track of loops
            row_num = 0

            # adding data to lists
            lons, lats, brightness, hover_text = [], [], [], []
            for row in reader:
                bright = float(row[2])
                label = "Brightness: {}".format(bright)
                lats.append(row[0])
                lons.append(row[1])
                brightness.append(bright)
                hover_text.append(label)

                row_num += 1
                if row_num >= max_loops:
                    break

            # adding data from lists into a map of the world
            data = [{
                'type': 'scattergeo',
                'lon': lons,
                'lat': lats,
                'text': hover_text,
                'marker': {
                    'size': [bright / 20 for bright in brightness],
                    'color': brightness,
                    'colorscale': 'YlOrRd',
                    'reversescale': False,
                    'colorbar': {'title': 'Brightness'}
                }
            }]

            my_layout = Layout(title="Global Fire Activity")
            fig = {'data': data, 'layout': my_layout}
            offline.plot(fig, filename="Global_fire_activity.html")


class WorkingWithAPIs:
    '''
    A web API is a part of a website designed to interact with programs. Those
    programs use very specific URLs to request certain information. This kind
    of request is called an API call. The requested data will be returned in an
    360 Chapter 17
    easily processed format, such as JSON or CSV. Most apps that rely on external data sources, such as apps that integrate with social media sites, rely on
    API calls.
    '''

    def Git_hub(self):

        '''
        GitHub (https://github.com/) takes its name from Git, a distributed version
        control system. Git helps people manage their work on a project, so changes
        made by one person won’t interfere with changes other people are making.
        When you implement a new feature in a project, Git tracks the changes you
        make to each file. When your new code works, you commit the changes
        you’ve made, and Git records the new state of your project. If you make a
        mistake and want to revert your changes, you can easily return to any previously working state. (To learn more about version control using Git, see
        Appendix D.) Projects on GitHub are stored in repositories, which contain
        everything associated with the project: its code, information on its collaborators, any issues or bug reports, and so on.
        When users on GitHub like a project, they can “star” it to show their
        support and keep track of projects they might want to use. In this chapter,
        we’ll write a program to automatically download information about the
        most-starred Python projects on GitHub, and then we’ll create an informative visualization of these projects.
        '''

        '''
        GitHub’s API lets you request a wide range of information through API
        calls. To see what an API call looks like, enter the following into your
        browser’s address bar and press enter:
        https://api.github.com/search/repositories?q=language:python&sort=stars
        '''

        # Make an API call and store the response

        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        headers = {'Accept': 'application/vnd.github.v3+json'}
        r = requests.get(url, headers=headers)
        print(f"Status Code: {r.status_code}")

        # Store API response in a variable
        response_dict = r.json()
        print(f"Total Repositories: {response_dict['total_count']}")

        print(response_dict.keys())

        # Explore the details of the repositories
        repo_dicts = response_dict['items']
        print(f"Repositories Returned: {len(repo_dicts)}")

        # Examine first repository
        repo_dict = repo_dicts[0]
        print(f"\nKeys: {len(repo_dict)}")
        for Key in sorted(repo_dict.keys()):
            print(Key)

        print(
            "\nSelected Repository Information")  # this is to see what the data looks like to tell if it is what I want
        print(f"Name: {repo_dict['name']}")
        print(f"Owner {repo_dict['owner']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Created: {repo_dict['created_at']}")
        print(f"Updated: {repo_dict['updated_at']}")
        print(f"Description: {repo_dict['description']}")

        '''
        Most APIs are rate limited, which means there’s a limit to how many requests
        you can make in a certain amount of time. To see if you’re approaching
        GitHub’s limits, enter https://api.github.com/rate_limit into a web browser. 
        '''

        names, stars, repo_links, hover_text = [], [], [], []
        for repo in repo_dicts:
            names.append(repo['name'])
            stars.append(repo['stargazers_count'])

            # Getting the link to project
            repo_name = repo['name']
            repo_url = repo['html_url']
            repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
            repo_links.append(repo_link)

            # Getting ifo to put in hover text
            description = f"Description: {repo['description']}"
            owner = f"Owner: {repo['owner']['login']}"

            # sorting the time created and updated
            timecreated = (repo['created_at'])
            times = timecreated.split('-')
            year = times[0]
            month = times[1]
            day_almost = times[2]
            day = day_almost.split('T')

            new_created_time = f"Time Created: {day[0]}-{month}-{year}"

            timeupdated = (repo['updated_at'])
            times = timeupdated.split('-')
            year = times[0]
            month = times[1]
            day_almost = times[2]
            day = day_almost.split('T')

            new_updated_time = f"Time Updated: {day[0]}-{month}-{year}"

            # adding the hover text
            text = f"{description}<br />{owner}<br />{new_created_time}<br />{new_updated_time}"

            hover_text.append(text)

        print(repo_links)
        # visualizing

        data = [{
            'type': 'bar',
            'x': repo_links,
            'y': stars,
            'hovertext': hover_text,
            'marker': {
                'color': 'rgb(57, 106, 177)',
                'line': {'width': 1.5, 'color': 'rgb(57, 106, 250)'}
            },
            'opacity': 0.6,
        }]

        my_layout = {
            'title': 'Most-Stared Git-Hub Repositories',
            'titlefont': {'size': 28},
            'xaxis': {
                'title': 'Repository',
                'titlefont': {'size': 20},
                'tickfont': {'size': 14},
            },
            'yaxis': {
                'title': 'Stars',
                'titlefont': {'size': 20},
                'tickfont': {'size': 14},
            },
        }

        fig = {'data': data, 'layout': my_layout}
        offline.plot(fig, filename="Python_repos.html")

    def hackernewsAPI(self, sort_by="scores", amount_of_posts=10):
        if amount_of_posts > 25:
            print("Cannot Have More Than 25")  # here because it would take too long
            quit()
        # checking the sort_by to see if its scores or comments
        correct_sort = False
        if sort_by == "comments":
            correct_sort = True
        elif sort_by == "scores":
            correct_sort = True

        if not correct_sort:
            print("The valid sorting methods are sort_by 'scores' or 'comments'")
            quit()

        # Make api call and store the data
        url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
        r = requests.get(url)
        if r.status_code == 200:
            print(r.status_code)
            submission_ids = r.json()
            submission_dicts = []
            for submission_id in submission_ids[:amount_of_posts]:
                url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
                r = requests.get(url)
                if r.status_code == 200:
                    response_dict = r.json()

                    # dictionary for data
                    try:  # if there were 0 comments it would get error this fixes this
                        comments = response_dict['descendants']
                    except:
                        comments = 0

                    try:
                        project_link = response_dict['url']
                    except:
                        project_link = "None"

                    submission_dict = {
                        "creator": response_dict['by'],
                        "title": response_dict['title'],
                        "score": response_dict['score'],
                        "comments": comments,
                        "discuss_link": f"http://news.ycombinator.com/item?id={submission_id}",
                        "project_link": project_link,
                    }

                    submission_dicts.append(submission_dict)  # adds it to the big list of dictionaries

            if sort_by == "comments":
                submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

            else:
                submission_dicts = sorted(submission_dicts, key=itemgetter('score'), reverse=True)

            for submission_dict in submission_dicts:
                print(f"Creator: {submission_dict['creator']}")
                print(f"title: {submission_dict['title']}")
                print(f"score: {submission_dict['score']}")
                print(f"comments: {submission_dict['comments']}")
                print(f"discuss_link: {submission_dict['discuss_link']}")
                print(f"project_link {submission_dict['project_link']}\n")

            creators, titles, scores, comments, discuss_links, links, hover_text = [], [], [], [], [], [], []
            for i in range(len(submission_dicts)):
                creators.append(submission_dicts[i]['creator'])
                titles.append(submission_dicts[i]['title'])
                scores.append(submission_dicts[i]['score'])
                comments.append(submission_dicts[i]['comments'])
                # creating hyperlinks
                project_link = submission_dicts[i]['project_link']
                project_hyper_link = f"<a href='{project_link}'>Post/Project</a>"
                discussion_link = submission_dicts[i]['discuss_link']
                discussion_hyperlink = f"<a href='{discussion_link}'>Discussion</a>"
                links.append(f"{project_hyper_link}<br />{discussion_hyperlink}")

                # Hovering text
                creator = f"Creator: {creators[i]}"
                title = f"Title: {titles[i]}"
                score = f"Score: {scores[i]}"
                num_comments = f"Comments: {comments[i]}"

                text = f"{creator}<br />{title}<br />{score}<br />{num_comments}"
                hover_text.append(text)

            # Plotting The Data
            if sort_by == "comments":
                y_axis = comments
            else:
                y_axis = scores

            data = [{
                'type': 'bar',
                'x': links,
                'y': y_axis,
                'hovertext': hover_text,
                'marker': {
                    'color': 'rgb(57, 106, 177)',
                    'line': {'width': 1.5, 'color': 'rgb(57, 106, 250)'}
                },
                'opacity': 0.6,
            }]

            if 20 <= amount_of_posts <= 25:
                size = 11
            else:
                size = 14

            my_layout = {
                'title': f"Most Popular Hacker News Posts Ranked By {sort_by.title()}",
                'titlefont': {'size': 28},
                'xaxis': {
                    'title': 'Links To Posts And Post Discussions',
                    'titlefont': {'size': 20},
                    'tickfont': {'size': size},
                },
                'yaxis': {
                    'title': f"{sort_by.title()}",
                    'titlefont': {'size': 20},
                    'tickfont': {'size': 18},
                },
            }

            fig = {'data': data, 'layout': my_layout}
            offline.plot(fig, filename="Hacker_News_Data.html")

        else:
            print("STATUS CODE ERROR")


if __name__ == "__main__":
    # Make objects below:

    a = WorkingWithAPIs()
    a.Git_hub()

'''
    list of classes:

    LineGraphs
    ScatterGraphs                      
    CubesChallenge            my solution to problem in course more info inside of class
    RandomWalk                part on plotting a random walk
    RandomChallenge           my solution to problem in course more info inside of class
    PlotlyDice                working with plotly to make interactive visualizations
    DownloadingData           working with csv data
    JsonData                  working with data in json file
    FireData                  project in course for plotting a map of fires
    WorkingWithAPIs           working with api's using requests
'''
