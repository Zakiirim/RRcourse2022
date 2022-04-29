#Exercise 4

library(tidyverse)

StudentsPerformance <- read.csv('StudentsPerformance.csv')

StudentsPerformance <- StudentsPerformance %>% 
  rename(race_ethnicity = `race/ethnicity`,
         math_score = `math score`,
         test_preparation_course = `test preparation course`,
         parental_education = `parental level of education`)

unique(StudentsPerformance$race_ethnicity)
length(unique(StudentsPerformance$race_ethnicity))

StudentsPerformance %>% 
  group_by(race_ethnicity) %>% 
  summarize(mean_math_score = mean(math_score))
  
StudentsPerformance %>% 
  filter(test_preparation_course == "completed" &
         parental_education %in% c("associate's degree", 
                                   "bachelor's degree", 
                                   "master's degree")) %>% 
  summarize(math = mean(math_score),
            reading = mean(`reading score`),
            writing = mean(`writing score`))

StudentsPerformance %>% 
  mutate(value = math_score/`reading score`) %>% 
  ggplot(aes(x = value)) + 
  geom_histogram(stat  = "bin", fill = "steelblue") +
  theme_minimal()
