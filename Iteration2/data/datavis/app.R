library(shiny)
library(toastui)
library(tidyverse)


my_calendar_data <- data.frame(
  title = "Holiday",
  start = c("2023-01-01 00:00:00", "2023-01-26 00:00:00", "2023-03-13 00:00:00", "2023-04-07 00:00:00", "2023-04-25 00:00:00", "2023-06-12 00:00:00", "2023-09-29 00:00:00", "2023-11-07 00:00:00", "2023-12-25 00:00:00", "2023-12-26 00:00:00"),
  end = c("2023-01-02 00:00:00", "2023-01-26 00:00:00", "2023-03-13 00:00:00", "2023-04-10 00:00:00", "2023-4-25 00:00:00", "2023-06-12 00:00:00", "2023-09-29 00:00:00", "2023-11-07 00:00:00", "2023-12-25 00:00:00", "2023-12-26 00:00:00")
)





ui <- fluidPage(
  column(8,
         calendarOutput("calendar", width = "100%", height = "200px")
  )
 
)

server <- function(input, output) {
  output$calendar <- renderCalendar({
    calendar(navigation = TRUE, defaultDate = Sys.Date()) %>%
      cal_schedules(my_calendar_data)
  })
  
}

shinyApp(ui, server)