# CaP-3

This code defines two classes: Bullet represents the bullets shot by a rocket in a game, each being a 20x20 rectangle. The Rocket class represents the player's rocket, which can shoot bullets. The shoot method of the rocket creates a new bullet and adds it to the shot_group only if a cooldown period has passed since the last shot.

For testing, the TestRocket class is created as a subclass of unittest.TestCase. The setUp method initializes Pygame and creates instances of the Rocket class for testing, while tearDown cleans up resources after each test.

There are several test methods within TestRocket:

test_shoot checks if shooting a bullet adds it to the shot_group.
test_another_method is a placeholder for another test method, currently checking if the shot_group is empty.
test_cooldown tests if the rocket can shoot within the specified cooldown time.
test_score_increment tests scoring points when bullets hit alien sprites. It initializes an alien and a bullet, adds them to groups, and checks if the score increments when the bullet collides with the alien.
The choice of using unittest is explained by its role as a testing framework in Python, providing tools for constructing and running test cases. It enables the organization of tests into logical units and offers various assertion methods like assertEqual for easy verification of expected behavior. The test suite's scalability ensures that as the project evolves, modifications to the code won't introduce unexpected issues. Overall, unittest is chosen for its simplicity, ease of use, and integration with the Python standard library, making it suitable for unit testing in this scenario.
