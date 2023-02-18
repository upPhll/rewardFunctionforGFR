    def _reward(self):
        if self._done():
            return -2

        car = self.state["car"]

        velocity = math.sqrt((self._last_x - car.x)**2 + (self._last_y - car.y)**2) / TIMESTEP
        self._last_x = car.x
        self._last_y = car.y

        # exponential rewards for higher speeds, also for speeds < 1
        reward = (velocity * 0.8 + 1)**2 - 1
        
        return reward
