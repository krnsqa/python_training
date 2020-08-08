
Scenario Outline: Add new group

  Given a group list
  Given a group with <name>, <header>, <footer>
  When I add the group to the list
  Then the new group list is equal to old list with the added group

  Examples:
  | name  | header  | footer  |
  | name1 | header1 | footer1 |
  | name2 | header2 | footer2 |



Scenario Outline: Delete group

  Given a nonempty group list
  Given a random group from the list
  When I delete the group from the group list
  Then the new group list is equal to old list without the deleted group


