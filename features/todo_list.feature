# to_do.feature

Feature: To-Do List Management

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task       |
      | Buy groceries |
      | Pay bills   |
    When the user lists all tasks
    Then the output should contain:
      """
      Tasks:
      - Buy groceries
      - Pay bills
      """

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task       |
      | Buy groceries |
      | Pay bills   |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Edit a task in the to-do list
    Given the to-do list contains tasks:
      | Task          | Description    | Status  |
      | Buy groceries | Grocery shopping | Pending |
    When the user edits task "Buy groceries" with name "Buy food" and description "Grocery shopping"
    Then the to-do list should show task "Buy food" with description "Grocery shopping" as pending

  Scenario: List only incomplete tasks in the to-do list
    Given the to-do list contains tasks:
      | Task          | Description    | Status  |
      | Buy groceries | Grocery shopping | Pending |
      | Pay bills     | Pay utility bills | Complete |
    When the user lists incomplete tasks
    Then the output should contain:
      """
      Incomplete Tasks:
      - Buy groceries - Grocery shopping
      """
