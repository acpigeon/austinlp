import csv # the csv module lets us csv file objects to read from and write to


dates, AAPL, GOOG, MSFT, DELL = [], [], [], [], []


with open('prices.csv', 'rU') as file:
	csv_object = csv.reader(file, delimiter=',', quotechar='"')
	for row in csv_object:
		# Step 1: Row structure (will cause problems later)
		#print row, type(row) # Horizontal structure

		# Step 2: Column structure (much better)
		#print row[0], type(row[0])
		#print row[1], type(row[1])
		#print row[2], type(row[2])
		#print row[3], type(row[3])
		#print row[4], type(row[4])

		# Step 3 get this stuff in arrays
		# Remember, each of these arrays is analogous to an Excel column
		dates.append(row[0])
		AAPL.append(row[1])
		GOOG.append(row[2])
		MSFT.append(row[3])
		DELL.append(row[4])

# Set up some values we will need later
# .pop(0) removes the first value (header row) of each array and stores it
apple_ticker = AAPL.pop(0)
google_ticker = GOOG.pop(0)
microsoft_ticker = MSFT.pop(0)
dell_ticker = DELL.pop(0)

# Array referencing starts at 0 to read from the beginning, and -1 to start from the end
apple_return = float(AAPL[-1])/float(AAPL[0])
google_return = float(GOOG[-1])/float(GOOG[0])
microsoft_return = float(MSFT[-1])/float(MSFT[0])
dell_return = float(DELL[-1])/float(DELL[0])

investment = 1000

# Set up output columns
label, apple_output, google_output, microsoft_output, dell_output = [], [], [], [], []

label.append("Start Value")
apple_output.append(AAPL[0])
google_output.append(GOOG[0])
microsoft_output.append(MSFT[0])
dell_output.append(DELL[0])

label.append("End Value")
apple_output.append(AAPL[-1])
google_output.append(GOOG[-1])
microsoft_output.append(MSFT[-1])
dell_output.append(DELL[-1])



label.append("Percent Return")
apple_output.append(apple_return)
google_output.append(google_return)
microsoft_output.append(microsoft_return)
dell_output.append(dell_return)


label.append("Dollar Return")
apple_output.append(apple_return * investment)
google_output.append(google_return * investment)
microsoft_output.append(microsoft_return * investment)
dell_output.append(dell_return * investment)


# zip() takes each array given to it and "zips" them up to resemble columns
output = zip(label, apple_output, google_output, microsoft_output, dell_output)
headers = ["", apple_ticker, google_ticker, microsoft_ticker, dell_ticker]
output.insert(0, headers)

output_file = csv.writer(open('portfolio.csv', 'ab'), delimiter=",", quotechar='"')
for row in output:
    output_file.writerow(row)
