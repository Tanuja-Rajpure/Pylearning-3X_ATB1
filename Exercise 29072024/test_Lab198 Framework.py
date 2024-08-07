#Framework-
# A structure that provides foundation to a developing software application/ test automation
# CHaracteristics of framework
#1- Structure for organising code and resources
#2- Folder structure to maintain test cases
#3- To follow best practices and design patterns
#4- Promote scalabilty and flexibility

# Framework Vs Library
# Library- Bunch of re-useable code
# Framework uses library in code for eg requests library , Pytest

#Types of Framework
#1- Linear Automation framework- Record and playback
# - Simple manner run cases, but do not maintain it
#- It has code duplicasy, Maintainance is high

#2- Module Driven framewrok- Has different module
#- For eg E commerce website- Registration- Login- Order- payment- SHipping-Confirmation
# PROS- Facilitates independent scripts creation and better organization
# CONS- Requires more time for analysis and identification of re-useble modules

#3- Data Driven Framework
# This allows tester to input single test script that can execute tests for all test data from a table
# And expect test output in same folder
# For eg login test with 100 u/n and pw, so script can take data from file- cs/json/excel
# PROS- Reduces no of scripts required and efficient for testing various scenarios
# CONS- Must have strong programing skills and manage data source effectively

#4 - Keyword Driven Framework E.g. Robot Framework
# Keywords created in test automation to make it reuseable
# Also known as table driven testing
# This framework uses keywords defined in different external file to execute test cases
# Each keyword corresponds to a specific action in the application
# PROS - Code reuseability through shared keywords
# CONS- Complex ad time consuming process, Requires solid understanding of framework

#5- Behaviour Driven development - BDD
# This emphasizes collaboration among developers, testers and business analysts by using natural language to define test cases
# Feature file(PO/PM/BA)->Gherkin syntax-Given, when,then-->
# Test Runner-Glue-feature file-steps?
# Steps (code)- created by AT / Dev/ SDET
# PROS- Non technical person can understand test cases
# CONS- Require some technical knowledge and nowdays PO/PM don't write feature file- so only tester has to do

#6- Hybrid Testing framework
# Combines elements from various frameworks to leverage their strength while minimizing weaknesses
# It can incorporates aspects of data-driven and keyword driven frameworks
# PROS Offers flexibility and adaptability to different testing needs , maximizes code reuse
# CONS - Can increase automation efforts due to scripting, may be complex

#6 - TDD - Test driven development
# Used by developers mostly
# Create test cases- use then for software development

