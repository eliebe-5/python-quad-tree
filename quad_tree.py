

class quad_tree:
    ready = False
    
    def setup(self, width, height, start_x = 0, start_y = 0):
        if(not self.ready):
            self.w = width
            self.h = height
            self.x = start_x
            self.y = start_y
            self.ready = True
            self.size = 1
            self.data = []
            self.pre_ready_data = []
            for elmnt in self.pre_ready_data:
                self.insert_element(elmnt)

    def insert_element(self, elmnt):
        if(not self.ready):
            self.pre_ready_data.append(elmnt)
            return True
        elif(self.in_range(elmnt)):
            if(len(self.data) < self.size):
                self.data.append(elmnt)
                return True
            else:
                if(not hasattr(self, 'up_left')):
                    self.up_left = quad_tree()
                    self.up_right = quad_tree()
                    self.down_left = quad_tree()
                    self.down_right = quad_tree()
                    self.up_left.setup(self.w/2, self.h/2, self.x, self.y)
                    self.up_right.setup(self.w/2, self.h/2, self.x + self.w/2, self.y)
                    self.down_left.setup(self.w/2, self.h/2, self.x, self.y + self.h/2)
                    self.down_right.setup(self.w/2, self.h/2, self.x + self.w/2, self.y + self.h/2)

                if(self.up_left.insert_element(elmnt)):
                    return True
                if(self.up_right.insert_element(elmnt)):
                    return True
                if(self.down_left.insert_element(elmnt)):
                    return True
                if(self.down_right.insert_element(elmnt)):
                    return True
        else:
            return False

    def find_elements(self, xx, yy, width, height):
        output = []
        if(len(self.data) != 0):
            if((xx > (self.x + self.w) or self.x > (xx + width)) or (yy > (self.y + self.h) or self.y > (yy + height))):
                return output

            for elmnt in self.data:
                if(elmnt.x > xx and elmnt.x < (xx + width) and elmnt.y > yy and elmnt.y < (yy + height)):
                    output.append(elmnt)

            if(hasattr(self, 'up_left')):
                output += self.up_left.find_elements(xx, yy, width, height)
                output += self.up_right.find_elements(xx, yy, width, height)
                output += self.down_left.find_elements(xx, yy, width, height)
                output += self.down_right.find_elements(xx, yy, width, height)

        return output
            

    def in_range(self, elmnt):
        return (self.x < elmnt.x and elmnt.x <= (self.x + self.w) and self.y < elmnt.y and elmnt.y <= (self.y + self.h))

