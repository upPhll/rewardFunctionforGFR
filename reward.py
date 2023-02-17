def _reward(self):
        if self._done():
            return 0
        reward = 0
        car = self.state["car"]
        displacement = math.sqrt((self._track_start_pos_x - car.x)**2 + (self._track_start_pos_y - car.y)**2)
        delta_disp = (displacement - self._last_displacement)/TIMESTEP
        self._last_displacement = displacement
        left_cone = self.state["left-cones"]
        right_cone = self.state["right-cones"]
        track = self.state["track_outline"]
        end_state = max(delta_disp)
        left_cone_update = left_cone.get_state()
        right_cone_update = right_cone.get_state()
        if self._last_displacement == left_cone_update:
            reward -= 1*math.sqrt(car.a_x**2 + car.a_y**2)
        elif self._last_displacement == right_cone_update:
            reward -= 1*math.sqrt(car.a_x**2 + car.a_y**2)
        
        while car.x < TRACK_WIDTH:
            if car.x == TRACK_WIDTH/2:
                reward += 10*delta_disp / 20
            

        
        if end_state ==  track:
            reward += 100*delta_disp / 20
        # for i in range(len(left_cone))
        


        # reward = 0
        # reward += 0.5*displacement       # rewarded for how far we get away from starting
        reward += 1*delta_disp / 20        # rewarded for our speed in the forward direction
                                           #  as fraction of maximum speed
        # reward -= 1*math.sqrt(car.a_x**2 + car.a_y**2) # penalized for net acceleration 
        return reward