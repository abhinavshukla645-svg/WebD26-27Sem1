 width, height = self.get_size()

        coords = self.canvas.coords("target")

        if len(coords) != 4:
            self.generate_target()
            coords = self.canvas.coords("target")

        current_x = (coords[0] + coords[2]) / 2
        current_y = (coords[1] + coords[3]) / 2

        new_x = current_x + random.randint(-20, 20)
        new_y = current_y + random.randint(-0, 20)

        new_x = max(
            self.target_radius + 5,
            min(width - self.target_radius - 5, new_x)
        )

        new_y = max(
            65 + self.target_radius,
            min(height - self.target_radius - 5, new_y)
        )

        self.canvas.move(
            "target",
            new_x - current_x,
            new_y - current_y
        )

        self.target_position = (new_x, new_y)

        self.move_job = self.root.after(100, self.move_target)