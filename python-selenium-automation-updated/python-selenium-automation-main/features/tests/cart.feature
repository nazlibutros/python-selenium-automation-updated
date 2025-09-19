# Created by rtbut at 9/10/2025
Feature: Tests for Cart functionality

  Scenario:   User can see “Your cart is empty” message
    Given Open Target main Page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown

  Scenario:   User can see added product into the cart
    Given Open Target main Page
    When Search for mug
    When Click on Add to Cart button
#    When Store product name
    When Confirm Add to Cart button from side navigation
    And Open Target cart Page
    Then Verify cart has 1 item(s)
#    Then Verify cart has correct product