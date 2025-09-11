Feature: Tests to verify Header UI elements

  Scenario: Verify header has {expected_amount} links
    Given Open Target main Page{expected_amount}
    Then Verify header has 6 links
#  Then Verify header has links