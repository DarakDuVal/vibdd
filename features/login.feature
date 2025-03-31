Feature: user can login to persist order details

  Scenario: user creates account
    Given any user
    When creating and account
    Then user is asked for unique username and password
    And optionally provide shipping address
    And optionally provide payment details including credit card number and cardholder details

  Scenario: user logs into account
    Given a revisiting user
    When logging in using username and password
    Then shipping address and payment information is available on order checkout
