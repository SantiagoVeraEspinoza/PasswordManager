import graphic_engine as ge

class Window(ge.App): # Inheritates from App
    def update(self):
        # Fill the background with white
        self.fill(ge.WHITE)

        # # Draw a solid blue circle in the center
        self.rect(ge.Coord(150, 150), ge.Vector(250, 250), ge.Color(0, 0, 0))
        self.circle(ge.Coord(250, 250), 75, ge.Color(0, 0, 0, 200))
        self.circle(ge.Coord(250, 250), 60, ge.Color(255, 0, 0, 100))
        self.drawText(ge.Text("Hola!", ge.Coord(30, 10)))

if __name__ == '__main__':
    app = Window(500, 500)

    app.run()