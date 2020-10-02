def setup():
    size(555, 555)

    
def draw():
    background(0)
    fill(mouseX-70, mouseY, 255)
    circle(mouseX-70, mouseY, 100)
    fill(255)
    ellipse(mouseX-85, mouseY-15, 20, 40)
    fill(255)
    ellipse(mouseX-55, mouseY-15, 20, 40)
    fill(50, 157, 168)
    ellipse(mouseX-55, mouseY-15, 10, 15)
    fill(50, 157, 168)
    ellipse(mouseX-85, mouseY-15, 10, 15)
    fill(0)
    arc(mouseX-70, mouseY+10, 60, 50, 0, PI, CHORD)
