# Created by lucalorusso at 7/15/25
Feature: sale_status_mobile

  Scenario: User can filter by mobile sale status Out of Stocks
    Given Open the main page
    When Log in to the page
    And Enter email luca.lorusso@icloud.com
    And Enter your FistQAtesting
    And Click continue button
    When Click on off plan at bottom left menu
    Then Verify the off-plan opens
    When Click Sale Status
    And Click Out of Stocks button
    Then Verify each product contains the Out of Stocks tag on mobile