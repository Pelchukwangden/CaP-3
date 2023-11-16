import unittest
import pygame

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Rocket:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20, 20, 20)  
        self.last_shot_time = 0
        self.cooldown_time = 100
        self.shot_group = []  

    def shoot(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_shot_time > self.cooldown_time:
            bullet = Bullet(self.rect.centerx - 10, self.rect.top)
            self.shot_group.append(bullet)
            self.last_shot_time = current_time

class TestRocket(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.rocket = Rocket()
        self.test_rocket = Rocket()  

    def tearDown(self):
        pygame.quit()

    def test_shoot(self):
        self.rocket.shoot()
        self.assertEqual(len(self.rocket.shot_group), 1)

    def test_another_method(self):
        self.assertEqual(len(self.rocket.shot_group), 0)

    def test_cooldown(self):
        self.rocket.shoot()
        self.assertEqual(len(self.rocket.shot_group), 1)

        pygame.time.wait(self.rocket.cooldown_time - 10)
        self.rocket.shoot()
        self.assertEqual(len(self.rocket.shot_group), 1) 

        pygame.time.wait(20)
        self.rocket.shoot()
        self.assertEqual(len(self.rocket.shot_group), 2)


    def test_score_increment(self):
        rocket = Rocket()

    class Alien1(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            alien = Alien1()
            bullet = Bullet(rocket.rect.centerx, rocket.rect.top)
            alien_group1.add(alien)
            shot_group.add(bullet)
            self.assertEqual(score, 0)

            for bullet in shot_group:
                hit_list1 = pygame.sprite.spritecollide(bullet, alien_group1, True)
                if hit_list1:
                    bullet.kill()
                    score += 1
            self.assertEqual(score, 1)

if __name__ == '__main__':
    unittest.main()
