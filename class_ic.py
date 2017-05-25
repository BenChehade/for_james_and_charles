"""
For James & Charles, so they can both laugh at me and call me noob
"""
import numpy as np


class SnookerTable(object):
    """
    Useage
    g = SnookerTable.Ball(color='green')
    r = SnookerTable.Ball()

    # no reason for this comment
    """

    class Ball(object):
        def __init__(self, pot=False, **kwargs):
            self.colour = kwargs.get('colour', 'red')
            self.location = kwargs.get('location', [np.random.random(), np.random.random()])
            self.velocity_profile = kwargs.get('velocity_profile',
                                               np.random.choice(np.array(['gaussian', 'uniform', 'log-normal'])))
            self.position_error = kwargs.get('position_error',
                                             np.random.choice(np.array(['gaussian', 'uniform', 'log-normal'])))
            self.velocity = self.starting_velocity(self.velocity_profile)
            self.direction = np.pi * 2 * np.random.random()
            self.potted = pot
            #
            print('Initialised at ', self.location, ' with velocity = ', format(self.velocity, '05.3f'),
                  ' and angle = ', format(self.direction, '05.3f'))

        def starting_velocity(self, velocity_profile):
            """
            Creates some crazy starting parameters, if you've not specified an appropriate 
            :param velocity_profile: 
            :return: velocity
            """
            if velocity_profile == 'gaussian':
                mean = np.random.randint(0, 5 + 1)
                stddev = np.random.random()
                velocity = np.random.normal(loc=mean, scale=stddev)
                # print('gaussian params')
                # print('mean = ', mean, ', stddev = ', stddev, ' and velocity = ', velocity)
            if velocity_profile == 'uniform':
                low_bar = 5
                high_bar = 10
                low = np.random.randint(low_bar)
                high = np.random.randint(low_bar, high_bar)
                velocity = np.random.random() * (high - low) + low_bar
                # print('uniform params')
                # print('low_bar = ', low, ', high_bar = ', high, ' and velocity = ', velocity)
            if velocity_profile == 'log-normal':
                mean = np.random.randint(0, 5 + 1)
                stddev = np.random.random()
                velocity = np.random.lognormal(mean=mean, sigma=stddev)
                # print('log-normal params')
                # print('mean = ', mean, ', stddev = ', stddev, ' and velocity = ', velocity)
            else:
                velocity = 0
            return velocity

        def __iter__(self):
            return self

        def __next__(self):
            return self

        def next(self):
            if not self.potted:
                self.location[0] += self.velocity * np.sin(self.direction)
                self.location[1] += self.velocity * np.cos(self.direction)
            else:
                return self.location
            return self.location
