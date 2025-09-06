Feature: Tests for Target search functionality

  Scenario: User can search for a product in Target
    Given Open Target main Page
    When Search for a product
    Then Verify search results are shown

  Scenario: User can see “Your cart is empty” message
    Given Open Target main Page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown

  Scenario: A logged out user can navigate to Sign In
    Given Open Target main Page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened
