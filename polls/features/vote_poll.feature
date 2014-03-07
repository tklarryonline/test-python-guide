Feature: Polls
    Scenario: Display message when use does not choose option to submit
        Given I have a list of polls
        When I visit "/polls/"
        And I click on a poll question link
        Then I should see the poll detail
        When I click button "Submit"
        Then I should see the text "You have to choose an option"