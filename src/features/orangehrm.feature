Feature: OrangeHRM Feature
	Scenario: OrangeHRM Login Functionality
		Given I launched th default browser
		When I loaded OrangeHRM home page
		And I filled username "Admin" and password "admin123"
		And I clicked login button
		Then I verified whether "Dashboard" appears
		And I logged out from my account
		And I closed the browser
