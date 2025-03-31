Feature: browse articles for sale

  Scenario: list all articles in web shop
    Given any user is visiting the website
    When opening the articles page
    Then user will see a list of all articles with short name, description and price

  Scenario: filter articles
    Given any user is visiting the website
    And opening the articles page
    When applying filters on short name
    Then user will see a filtered list of articles matching or similar to filter statement on short name

  Scenario: add article to shopping cart
    Given any user on articles page
    When selecting an article to add to shopping cart
    Then cart will contain one item of chosen article
