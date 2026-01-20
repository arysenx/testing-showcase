Feature: Login test

@web
 Scenario: User tries to log in - Log in successfull
    Given user goes to "[CONF:pages.saucedemo.url]"
      And the "login_page" page is loaded
     When write "[CONF:users.success.username]" into "username" field
      And write "[CONF:users.success.password]" into "password" field
      And click on "login_button" button
     Then "title" element has "Swag Labs" text

@web
 Scenario: User tries to log in - Log in failed
    Given user goes to "[CONF:pages.saucedemo.url]"
      And the "login_page" page is loaded
     When write "[CONF:users.failure.username]" into "username" field
      And write "[CONF:users.failure.password]" into "password" field
      And click on "login_button" button
     Then "error_container" element is visible
      And "error_container" element has "Epic sadface: Username and password do not match any user in this service" text