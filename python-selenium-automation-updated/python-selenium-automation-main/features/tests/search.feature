Feature: Tests for Target search functionality

#  Scenario: User can search for a product in Target
#    Given Open Target main Page
#    When Search for tea
#    Then Verify search results are shown for tea


  Scenario: A logged out user can navigate to Sign In
    Given Open Target main Page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened

  Scenario Outline: User can search for a product in Target
    Given Open Target main Page
    When Search for <product>
    Then Verify search results are shown for <expected_product>
    Examples:
    |product  |expected_product |
    |iphone   |iphone           |
    |coffee   |coffee           |
    |tea      |tea              |
