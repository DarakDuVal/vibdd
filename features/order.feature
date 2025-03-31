Feature: order articles in shopping cart

  Scenario: user orders articles in cart
    Given user has at least one article in shopping cart
    When starting order process
    Then user is asked for customer details including name, shipping address
    And user is aksed for payment details including credit card number and card holder name
