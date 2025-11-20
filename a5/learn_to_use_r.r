# Marcus Martin - LIS4369 Assignment 5

# Environment Setup
# install.packages("quantmod", dependencies = TRUE)

rm(list = ls(envir = globalenv()), envir = globalenv())
if (!is.null(dev.list())) dev.off()
gc()
cat("\014")

# Set working directory
setwd("/Users/jaya/lis4369/a5")

# Built-in Data Example: mtcars
data()
mtcars

mtcars$mpg
mtcars[, 2:4]
mtcars[mtcars$mpg > 20, c("mpg", "hp")]

mpg20 <- mtcars$mpg > 20
cols <- c("mpg", "hp")
mtcars[mpg20, cols]

attach(mtcars)
mpg20_alt <- mpg > 20
detach(mtcars)

# dplyr Examples
# install.packages("dplyr", dependencies = TRUE)
library(dplyr)

mtcars %>%
  filter(mpg > 20) %>%
  select(mpg, hp) %>%
  arrange(desc(mpg))

table(mtcars$mpg, mtcars$hp)

# Base R Plotting
plot(mtcars$disp, mtcars$mpg,
     xlab = "Engine Displacement",
     ylab = "Miles Per Gallon",
     main = "MPG vs Engine Displacement",
     las = 1)

# ggplot2 Examples
# install.packages("ggplot2", dependencies = TRUE)
library(ggplot2)

ggplot(mtcars, aes(x = disp, y = mpg)) +
  geom_point(color = "blue", size = 3) +
  labs(title = "Displacement vs MPG", x = "Engine Displacement", y = "Miles per Gallon")

ggplot(mtcars, aes(x = disp, y = mpg)) +
  geom_line(color = "darkgreen", linewidth = 1.2) +
  labs(title = "Displacement vs MPG (Line Plot)")

ggplot(pressure, aes(x = temperature, y = pressure)) +
  geom_line(color = "blue") +
  geom_point(size = 3) +
  labs(title = "Pressure vs Temperature")

# BOD (Biochemical Oxygen Demand)
barplot(BOD$demand, main = "Biochemical Oxygen Demand", names.arg = BOD$Time)

cylcount <- table(mtcars$cyl)
barplot(cylcount, main = "Number of Cars by Cylinder Count", xlab = "Cylinders", ylab = "Count")

ggplot(mtcars, aes(x = factor(cyl))) +
  geom_bar(fill = "royalblue3") +
  labs(title = "Cars by Cylinder Count", x = "Cylinders", y = "Frequency")

# Color Palettes
rainbow(5)
heat.colors(5)
terrain.colors(5)
topo.colors(5)
cm.colors(5)

mycolors <- rainbow(3)
mycolors2 <- heat.colors(3)

ggplot(mtcars, aes(x = factor(cyl))) +
  geom_bar(fill = mycolors) +
  labs(title = "Cylinder Counts with Rainbow Colors")

barplot(BOD$demand, col = rainbow(6))
barplot(BOD$demand, col = "royalblue3")

# Test Score Example
testscores <- c(96, 71, 85, 92, 82, 78, 72, 81, 68, 61, 78, 86, 90)
testcolors <- ifelse(testscores >= 80, "blue", "red")

barplot(testscores, col = testcolors,
        main = "Test Scores (Blue ≥ 80, Red < 80)",
        ylim = c(0, 100),
        las = 1)

testscores_sorted <- sort(testscores, decreasing = TRUE)
barplot(testscores_sorted, col = testcolors[order(testscores, decreasing = TRUE)],
        main = "Test Scores (Descending)", ylim = c(0, 100))

# Save Plots as PNG Files
png("cylinder_count.png", width = 800, height = 600, units = "px", pointsize = 12, bg = "white")
barplot(cylcount, main = "Cars by Cylinder Count")
dev.off()

png("cylinder_count2.png", width = 800, height = 600, units = "px", pointsize = 12, bg = "#ccccff")
barplot(cylcount, main = "Cars by Cylinder Count (Light Blue)")
dev.off()

png("cylinder_count3.png", width = 800, height = 600, units = "px", pointsize = 12, bg = "azure")
barplot(cylcount, main = "Cars by Cylinder Count (Azure BG)")
dev.off()

# Financial Data (quantmod)
# install.packages("quantmod", dependencies = TRUE)
library(quantmod)

getSymbols("AAPL")

barChart(AAPL, name = "AAPL (All Data)")
barChart(AAPL, subset = "last 14 days", name = "AAPL (2 Weeks)")
chartSeries(AAPL, subset = "last 14 days", theme = chartTheme("white"))
barChart(AAPL['2013-04-01::2013-04-12'], name = "AAPL April 2013")
barChart(AAPL['2020'], name = "AAPL 2020 Data")

# Save Workspace and History
save.image(file = "/Users/jaya/lis4369/a5/my_workspace.RData")
savehistory(file = "/Users/jaya/lis4369/a5/my_history.Rhistory")

list.files("/Users/jaya/lis4369/a5", pattern = "\\.R(Data|history)$")
