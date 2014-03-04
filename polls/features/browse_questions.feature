Feature: Polls
    In order to vote for polls
    As a visitor
    I want to browse all polls' question

    Scenario: Browse polls' question
        Given I have a list of polls
        When I visit "/polls/"
        Then I should see a list of polls question