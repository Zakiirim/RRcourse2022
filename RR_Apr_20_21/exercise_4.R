#Exercise 4

library(tidyverse)

# read the file with data
StudentsPerformance <- read.csv('StudentsPerformance.csv')

#don't use "/" in column names...
StudentsPerformance <- StudentsPerformance %>% 
  rename(race_ethnicity = `race/ethnicity`,
         math_score = `math score`,
         test_preparation_course = `test preparation course`,
         parental_education = `parental level of education`)

# the dataframe contains data about 5 groups
unique(StudentsPerformance$race_ethnicity)
length(unique(StudentsPerformance$race_ethnicity))

# print mean math score for each group
StudentsPerformance %>% 
  group_by(race_ethnicity) %>% 
  summarize(mean_math_score = mean(math_score))
  
# print mean math, reading, and writing scores for students who completed 
#the test preparation course and their parent obtained a degree

StudentsPerformance %>% 
  filter(test_preparation_course == "completed" &
         parental_education %in% c("associate's degree", 
                                   "bachelor's degree", 
                                   "master's degree")) %>% 
  summarize(math = mean(math_score),
            reading = mean(`reading score`),
            writing = mean(`writing score`))

# plot the histogram of math scores divided by reading scores for each student

StudentsPerformance %>% 
  mutate(value = math_score/`reading score`) %>% 
  ggplot(aes(x = value)) + 
  geom_histogram(stat  = "bin", fill = "steelblue") +
  theme_minimal()
