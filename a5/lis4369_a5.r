############################################################
# Resources for clearing panes, data, memory:
############################################################
# http://www.sthda.com/english/articles/17-tips-tricks/75-clear-user-interface-and-free-memory-in-rrstudio/
# http://datacornering.com/how-to-clear-rstudio-panes-with-code/

# Clear RStudio console, environment, plot panes and free up memory at once:
rm(list = ls(envir = globalenv()), envir = globalenv())
if (!is.null(dev.list())) dev.off()
gc()
cat("\014")

# Breakdown:
# 1. Clear RStudio console window (identical to Ctrl+L):
# cat("\014")

# 2. Clear RStudio environment window (equivalent to click button
#    “clear objects from workspace” in Environment panel):
# rm(list = ls(envir = globalenv()), envir = globalenv())

# 3. Clear RStudio plot window (equivalent to click button
#    “clear all plots” in Plots panel):
# if (!is.null(dev.list())) dev.off()

# 4. Free up memory for RStudio:
# gc()


############################################################
# Set working directory  (*MY* working directory – YOURS will be different)
############################################################
# Windows example from instructor:
# setwd("C:/webdev/repos/classes/lis4369_python/a5")

# Your Mac working directory:
setwd("/Users/martin/Downloads/lis4369/a5")


############################################################
# Data Types
############################################################
# R has a wide variety of data types including:
# scalars, vectors (numerical, character, logical),
# matrices, data frames, and lists.

############################################################
# Assignment
############################################################
# Scalars: The most basic way to store a number is through assignment.
# Assignment is specified with "<-" characters.
# Assigns number on right of assignment symbol, and stores it in
# variable on left.

a <- 9          # assign value
a               # print value of a
a + 5           # print a + 5

b <- sqrt(a)    # assign square root of a to b
b               # print value of b


############################################################
# Nonscalar data types: vectors
############################################################
# Easiest way to store list of numbers is using the c command.
# Note: c means "combine".
# Vectors (one-dimensional arrays), by default, are specified
# with the c command.

c <- c(1, 2, 5, 3, 6, -2, 4)    # numeric vector
# or...
# c <- vector(1, 2, 5, 3, 6, -2, 4)  # also numeric vector
print(c)

typeof(c)        # print data type

is.list(c)       # FALSE
is.vector(c)     # TRUE

d <- c("one", "two", "three")   # character vector
d
typeof(d)        # print data type

e <- c(TRUE, TRUE, TRUE, FALSE, TRUE, TRUE, FALSE)  # logical vector
e
typeof(e)        # print data type

# To refer to row in Python, use index.
# In R, refer to object in ith row and jth column by OBJECTNAME[i, j].
# In R, refer to column name by OBJECTNAME$ColumnName.
# ***Note***: Python index starts with 0. R starts with 1!


############################################################
# Strings
############################################################
# String specified by using quotes – either single or double quotes work:
my_str <- "Hello World!"
my_str
typeof(my_str)   # print data type


############################################################
# Some intrinsic functions on scalar a, and vector c
############################################################
sqrt(a)

sqrt(c)  # Research why this produces an error!

a^2      # scalar squared
c^2      # vector squared

min(c)
max(c)
mean(c)
sum(c)


############################################################
# Reading CSV file (comma separated values)
############################################################
# Command: read.csv() reads file into data frame (similar to Python).
# Requires at least one argument: name of file.
# If three arguments:
#   1) name of file
#   2) indicates if first row are labels/headers
#   3) indicates separator character

url <- "https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/Stat2Data/Titanic.csv"
titanic <- read.csv(file = url, head = TRUE, sep = ",")

# To get more information, use help command:
# help(read.csv)

titanic          # displays all data from file

summary(titanic) # summary(): generic function used to produce result summaries
# Note: Python uses NaN to denote missing values, while R uses NA.

dir()            # list files in current working directory
getwd()          # determine current working directory

names(titanic)   # print headers (Note: “X” column is used for numbering rows)

# variable "titanic" contains the 7 columns of data.
# Each column assigned name based on header row (first line in file).
# Access each column using "$".
titanic$Name     # prints names
titanic$Age      # prints ages

attributes(titanic)  # returns object's attribute list
ls()                 # print list of variables defined in session


############################################################
# Basic Statistics for Titanic ages
############################################################
# Get mean, median, quantiles, minimum, maximum, variance,
# and standard deviation of passengers' ages:

mean(titanic$Age)              # returns NA, due to missing values

# Example: remove missing values
mean(titanic$Age, na.rm = TRUE)
quantile(titanic$Age, na.rm = TRUE)
min(titanic$Age, na.rm = TRUE)
max(titanic$Age, na.rm = TRUE)
var(titanic$Age, na.rm = TRUE)
sd(titanic$Age, na.rm = TRUE)

# summary() function prints min, max, mean, median, and quantiles
# (here, also number of NA's):
summary(titanic$Age, na.rm = TRUE)


############################################################
# Handling missing values and plotting
############################################################
# complete.cases() returns logical vector indicating which cases are complete
# List rows of data with missing values:
titanic[!complete.cases(titanic), ]

# na.omit() returns object with listwise deletion of missing values
# create new dataset without missing data
titanic_no_missing_data <- na.omit(titanic)
titanic_no_missing_data      # display new dataset w/o missing values!

# Charting/plotting – RESEARCH THE FOLLOWING COMMANDS!
# https://www.cyclismo.org/tutorial/R/plotting.html
help(stripchart)             # help command

# Send plots to a PDF file in your working directory
pdf(file = "myplotfile.pdf")
stripchart(titanic_no_missing_data$Age)   # strip chart

# histogram
# hist(titanic_no_missing_data$Age,
#      main = "Distribution of Titanic Passengers Ages",
#      xlab = "Ages")

# boxplot
boxplot(titanic_no_missing_data$Age)

dev.off()


# Or… plotted horizontally and saved as PNG
# png(filename = "boxplot.png",
#     width = 800, height = 600, units = "px",
#     pointsize = 12, bg = "chartreuse")
boxplot(titanic_no_missing_data$Age,
        main = "Distribution of Titanic Passengers Ages",
        xlab  = "Ages",
        horizontal = TRUE)
# dev.off()


############################################################
# Scatter plot: relationship between Age and Survival
############################################################
# png(filename = "scatter_plot.png",
#     width = 800, height = 600, units = "px",
#     pointsize = 12, bg = "#ccffff")
plot(titanic_no_missing_data$Age,
     titanic_no_missing_data$Survived,
     main = "Relationship Between Ages and Survival",
     xlab  = "Age",
     ylab  = "Survived")
# dev.off()


############################################################
# Save workspace
############################################################
# stores entire workspace to file named .RData by default.
# Ensures you won’t lose work!  Next R restart, workspace will be loaded.
save.image()
# quit()
