library(rmarkdown)
setwd(".")

for(season in 1:8){
  rmarkdown::render("Assignment 3.Rmd",
                    output_file = sprintf("Reports/GameOfThrones_season%s_report.html", season),
                    params = list(season = season))
}
