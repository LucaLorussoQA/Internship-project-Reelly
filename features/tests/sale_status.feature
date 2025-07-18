# Created by lucalorusso at 7/15/25
Feature: sale_status

  Scenario: User can filter by sale status Out of Stocks
    Given Open the main page
    When Log in to the page
    And Enter email luca.lorusso@icloud.com
    And Enter your FistQAtesting
    And Click continue button
    When Click on off plan at the left side menu
    Then Verify the right page opens
    And Filter by sales status of Out of stock
    Then Verify each product contains the Out of Stocks tag
