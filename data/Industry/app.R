#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(ggplot2)



industry = read_csv("industry.csv")

# Define UI for application that draws a histogram
ui <- fluidPage(
  selectInput(inputId = "x", label = "Select type of employee", choices = c("Persons", "Females", "Males"), selected = "Persons"),
  plotOutput(outputId = "barPlot")
)

# Define server logic required to draw a histogram
server <- function(input, output) {
 
  types <- reactive({input$x})
  Industry <- reactive({industry$Industry})
  
  output$barPlot <- renderPlot({
    
    ggplot(data = industry, aes(x = Persons, y = Industry)) + 
      geom_bar(stat = "identity", fill='navajowhite') + theme_classic()
  })
   
}

# Run the application 
shinyApp(ui = ui, server = server)
